#!/usr/bin/env python3
"""
Voice Generation Utility powered by edge-tts.
Produces natural neural audio synthesis for Cambridge/IELTS listening simulations,
monologues, and multi-speaker dialogues.
"""

import argparse
import asyncio
import io
import re
import sys
import time
from pathlib import Path
from typing import Dict, List, Tuple
import edge_tts

# Standard preset voice profiles calibrated for standardized listening exams
VOICE_PRESETS: Dict[str, str] = {
    # British RP
    "uk_male": "en-GB-RyanNeural",
    "uk_female": "en-GB-SoniaNeural",
    "uk_female_narrator": "en-GB-LibbyNeural",
    "uk_male_narrator": "en-GB-ThomasNeural",
    # Australian
    "au_female": "en-AU-NatashaNeural",
    "au_male": "en-AU-WilliamMultilingualNeural",
    # American
    "us_female": "en-US-JennyNeural",
    "us_male": "en-US-GuyNeural",
    "us_academic_male": "en-US-ChristopherNeural",
    # Regional UK
    "uk_regional_male": "en-GB-ThomasNeural",
}


def resolve_voice(voice_name_or_preset: str) -> str:
    """Resolve a preset name or return the exact voice identifier."""
    return VOICE_PRESETS.get(voice_name_or_preset.lower(), voice_name_or_preset)


async def synthesize_segment(
    text: str,
    voice: str,
    rate: str = "+0%",
    pitch: str = "+0Hz",
    volume: str = "+0%",
    max_retries: int = 4,
) -> bytes:
    """Synthesize a single text string into MP3 bytes in memory with retry backoff."""
    resolved_voice = resolve_voice(voice)
    for attempt in range(max_retries):
        try:
            communicate = edge_tts.Communicate(
                text=text,
                voice=resolved_voice,
                rate=rate,
                pitch=pitch,
                volume=volume,
            )
            buffer = io.BytesIO()
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    buffer.write(chunk["data"])
            data = buffer.getvalue()
            if data:
                await asyncio.sleep(0.35)
                return data
            raise RuntimeError("Empty audio payload received from edge-tts.")
        except Exception as exc:
            if attempt == max_retries - 1:
                print(f"  [ERROR] Synthesis failed for voice '{resolved_voice}': {exc}", file=sys.stderr)
                raise exc
            wait_time = (attempt + 1) * 1.5
            print(f"  [WARN] Retrying '{resolved_voice}' in {wait_time:.1f}s after error: {exc}", file=sys.stderr)
            await asyncio.sleep(wait_time)
    return b""


async def synthesize_file(
    text: str,
    output_path: Path,
    voice: str = "uk_female",
    rate: str = "+0%",
    pitch: str = "+0Hz",
    volume: str = "+0%",
) -> None:
    """Synthesize text directly to a file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    audio_data = await synthesize_segment(
        text=text,
        voice=voice,
        rate=rate,
        pitch=pitch,
        volume=volume,
    )
    output_path.write_bytes(audio_data)


def parse_dialogue_script(script_text: str) -> List[Tuple[str, str]]:
    """
    Parse a dialogue script with speaker headers like:
    [Speaker1]: text
    [uk_female]: Good morning.
    [uk_male]: Good morning, doctor.
    """
    pattern = re.compile(r"^\[([a-zA-Z0-9_\-]+)\]:\s*(.+)$", re.MULTILINE)
    segments = []
    for match in pattern.finditer(script_text):
        speaker = match.group(1).strip()
        utterance = match.group(2).strip()
        if utterance:
            segments.append((speaker, utterance))
    return segments


async def synthesize_dialogue(
    script_text: str,
    output_path: Path,
    speaker_map: Dict[str, str] = None,
    rate: str = "+0%",
    pitch: str = "+0Hz",
) -> None:
    """
    Synthesize multi-speaker dialogue and concatenate binary MP3 streams.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    segments = parse_dialogue_script(script_text)
    if not segments:
        raise ValueError("No speaker segments found matching '[Speaker]: utterance' format.")

    speaker_map = speaker_map or {}
    combined_audio = io.BytesIO()

    for speaker_tag, text in segments:
        voice = speaker_map.get(speaker_tag, speaker_tag)
        segment_bytes = await synthesize_segment(
            text=text,
            voice=voice,
            rate=rate,
            pitch=pitch,
        )
        combined_audio.write(segment_bytes)

    output_path.write_bytes(combined_audio.getvalue())


async def list_available_voices(filter_locale: str = "en") -> None:
    """Print available voices filtered by language code."""
    voices = await edge_tts.list_voices()
    filtered = [v for v in voices if v["Locale"].startswith(filter_locale)]
    print(f"\nAvailable voices ({len(filtered)} found for locale prefix '{filter_locale}'):\n")
    print(f"{'Short Name':<35} {'Gender':<8} {'Locale':<10} {'Suggested Roles'}")
    print("-" * 80)
    for v in sorted(filtered, key=lambda x: x["ShortName"]):
        roles = ", ".join(v.get("VoiceTag", {}).get("VoicePersonalities", []))
        print(f"{v['ShortName']:<35} {v['Gender']:<8} {v['Locale']:<10} {roles}")


def main() -> None:
    parser = argparse.ArgumentParser(description="High-fidelity voice synthesis utility via edge-tts.")
    subparsers = parser.add_subparsers(dest="command")

    # Single text synthesis
    speak_parser = subparsers.add_parser("speak", help="Synthesize single speaker audio.")
    speak_parser.add_argument("--text", "-t", type=str, required=True, help="Text to speak.")
    speak_parser.add_argument("--output", "-o", type=Path, required=True, help="Output MP3 file path.")
    speak_parser.add_argument("--voice", "-v", type=str, default="uk_female", help="Voice preset or exact name.")
    speak_parser.add_argument("--rate", type=str, default="+0%", help="Rate adjustment (e.g., '+5%' or '-10%').")
    speak_parser.add_argument("--pitch", type=str, default="+0Hz", help="Pitch adjustment (e.g., '+2Hz').")

    # Dialogue synthesis
    dialogue_parser = subparsers.add_parser("dialogue", help="Synthesize multi-speaker dialogue.")
    dialogue_parser.add_argument("--file", "-f", type=Path, required=True, help="Path to dialogue script file.")
    dialogue_parser.add_argument("--output", "-o", type=Path, required=True, help="Output MP3 file path.")
    dialogue_parser.add_argument("--rate", type=str, default="+0%", help="Rate adjustment.")
    dialogue_parser.add_argument("--pitch", type=str, default="+0Hz", help="Pitch adjustment.")

    # Voice listing
    list_parser = subparsers.add_parser("list", help="List available Edge TTS voices.")
    list_parser.add_argument("--locale", "-l", type=str, default="en", help="Locale filter (e.g., 'en-GB', 'en-US').")

    args = parser.parse_args()

    if args.command == "speak":
        asyncio.run(
            synthesize_file(
                text=args.text,
                output_path=args.output,
                voice=args.voice,
                rate=args.rate,
                pitch=args.pitch,
            )
        )
        print(f"Generated: {args.output}")

    elif args.command == "dialogue":
        script_content = args.file.read_text(encoding="utf-8")
        asyncio.run(
            synthesize_dialogue(
                script_text=script_content,
                output_path=args.output,
                rate=args.rate,
                pitch=args.pitch,
            )
        )
        print(f"Generated dialogue: {args.output}")

    elif args.command == "list":
        asyncio.run(list_available_voices(filter_locale=args.locale))

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
