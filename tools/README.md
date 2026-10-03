# Cambridge Audio Synthesis Tooling

This directory provides neural voice generation utilities for Cambridge/IELTS listening simulations, monologues, and multi-speaker dialogues powered by `edge-tts`.

## Prerequisites

```bash
pip install -r requirements.txt
```

## Tools

### 1. `generate_mock_audio.py`
Regenerates or updates the 18 listening audio tracks across Mock Tests 1, 2, and 3.

```bash
# Verify / generate missing tracks
python generate_mock_audio.py

# Force overwrite all tracks
python generate_mock_audio.py --force

# Generate only Mock Test 2 tracks
python generate_mock_audio.py --test 2 --force
```

### 2. `voice_gen.py`
General-purpose CLI for synthesizing single statements, monologues, and multi-speaker scripted dialogues.

```bash
# List available English neural voices
python voice_gen.py list --locale en-GB

# Synthesize a single statement
python voice_gen.py speak --text "Welcome to the listening test." --voice en-GB-SoniaNeural --output test.mp3

# Synthesize a multi-speaker dialogue script
python voice_gen.py dialogue --file script.txt --output dialogue.mp3
```

Dialogue scripts follow standard speaker tagging:
```text
[uk_female]: Excuse me, did anyone find a sketchbook?
[uk_male]: Let me check the lost property box.
```
