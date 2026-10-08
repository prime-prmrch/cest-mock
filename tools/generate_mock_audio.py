#!/usr/bin/env python3
"""
Regenerate all 18 listening audio tracks for Cambridge Mock Tests 1, 2, and 3
using edge-tts high-fidelity neural voices.
"""

import argparse
import asyncio
import io
import os
import sys
import time
from pathlib import Path
from typing import List, Tuple
import edge_tts

REPO_ROOT = Path(__file__).resolve().parent.parent
MOCK_DIR = REPO_ROOT


async def synthesize_bytes(
    text: str,
    voice: str,
    rate: str = "+0%",
    pitch: str = "+0Hz",
    max_retries: int = 4,
) -> bytes:
    """Synthesize text into MP3 bytes in memory with retry and rate-limit backoff."""
    for attempt in range(max_retries):
        try:
            communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate, pitch=pitch)
            buf = io.BytesIO()
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    buf.write(chunk["data"])
            data = buf.getvalue()
            if data:
                await asyncio.sleep(0.35)
                return data
            raise RuntimeError("Empty audio payload received.")
        except Exception as exc:
            if attempt == max_retries - 1:
                print(f"  [ERROR] Synthesis failed for voice {voice} on text snippet '{text[:30]}...': {exc}", file=sys.stderr)
                raise exc
            wait_time = (attempt + 1) * 1.5
            print(f"  [WARN] Retrying {voice} in {wait_time:.1f}s after error: {exc}", file=sys.stderr)
            await asyncio.sleep(wait_time)
    return b""


async def build_multi_speaker_track(
    segments: List[Tuple[str, str]],
    output_path: Path,
    rate: str = "+0%",
    pitch: str = "+0Hz",
    force: bool = False,
) -> None:
    """Build multi-speaker track by concatenating MP3 frames with brief acoustic pauses."""
    if not force and output_path.exists() and output_path.stat().st_size > 1000:
        print(f"  [SKIP] {output_path.relative_to(REPO_ROOT)} already exists ({output_path.stat().st_size} bytes). Use --force to overwrite.")
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)
    combined = io.BytesIO()
    for voice, text in segments:
        data = await synthesize_bytes(text, voice, rate=rate, pitch=pitch)
        combined.write(data)
    output_path.write_bytes(combined.getvalue())
    print(f"  [OK] Generated {output_path.relative_to(REPO_ROOT)} ({len(combined.getvalue())} bytes)")


# ==============================================================================
# MOCK TEST 1 SCRIPTS
# ==============================================================================

MOCK_1_Q1 = [
    ("en-GB-SoniaNeural", "Excuse me, did anyone hand in something left behind on table four?"),
    ("en-GB-RyanNeural", "Let me check the lost property box. Was it an umbrella or a smartphone? Someone left a black umbrella by the door earlier."),
    ("en-GB-SoniaNeural", "No, I had my phone and umbrella with me when I left. But when I got to my car, I realised my car keys were missing. I must have set them down next to my coffee mug."),
    ("en-GB-RyanNeural", "Ah, yes! Here they are. A silver keyring with two keys."),
    ("en-GB-SoniaNeural", "Oh, wonderful! Thank you so much."),
]

MOCK_1_Q2 = [
    ("en-GB-RyanNeural", "What did you think of the morning training session?"),
    ("en-GB-SoniaNeural", "The presenter was full of energy, and the collaborative roleplay was engaging enough. But what really stood out for you?"),
    ("en-GB-RyanNeural", "For me, the interactive software demo in the second half was genuinely eye-opening. I hadn't realized how much time those automated scheduling tools could save us."),
    ("en-GB-SoniaNeural", "Absolutely. Seeing that workflow in action made the whole morning worthwhile. That's definitely something our team should adopt straight away."),
    ("en-GB-RyanNeural", "Completely agree with you there."),
]

MOCK_1_Q3_Q7 = [
    ("en-GB-SoniaNeural", "Welcome to Design Horizons. Today we are speaking with Marcus Thorne, an acoustic engineer whose urban soundscape projects have won international acclaim. Marcus, what first motivated you to specialize in environmental acoustics rather than traditional concert halls?"),
    ("en-GB-RyanNeural", "Well, earlier in my career I focused on auditoriums. But when I realized how chaotic city soundscapes were becoming, I felt driven to apply acoustic principles outdoors. Chronic urban noise isn't just an annoyance; it causes elevated stress hormones and cognitive fatigue."),
    ("en-GB-SoniaNeural", "Many cities try to combat this by erecting solid highway noise walls. Are they effective?"),
    ("en-GB-RyanNeural", "Not as much as people assume. In fact, solid barriers often bounce sound elsewhere, creating echo chambers for adjacent neighborhoods. They treat sound merely as a physical projectile rather than understanding how sonic waves interact with urban microclimates."),
    ("en-GB-SoniaNeural", "So what is your principal critique of modern municipal planning?"),
    ("en-GB-RyanNeural", "Planners often treat acoustic design as an afterthought, an aesthetic luxury rather than a public health necessity. Cities allocate huge budgets for visual architecture, while entirely neglecting the acoustic environment people must inhabit daily."),
    ("en-GB-SoniaNeural", "You recently completed a redesign of St. Jude's Civic Plaza. How did you alter its acoustic character?"),
    ("en-GB-RyanNeural", "We installed a stepped water feature with a tailored broadband flow. It masks surrounding traffic hum without being overpowering, allowing people to hold conversations at a whisper. We also introduced porous limestone pavings that absorb high-frequency tyre friction."),
    ("en-GB-SoniaNeural", "Fascinating. Finally, what advice would you impart to aspiring soundscape designers?"),
    ("en-GB-RyanNeural", "Spend hours sitting in urban squares, listening actively. Your ears detect subtleties that algorithms easily overlook. You must develop an intuitive, somatic understanding of sonic textures before you begin drafting blueprints."),
]

MOCK_1_Q8_Q9 = [
    ("en-US-GuyNeural", "I noticed you've stopped purchasing formal clothes and switched to a rental subscription service."),
    ("en-US-JennyNeural", "Honestly, I used to spend a fortune buying designer outfits for weddings that I'd only ever wear once. It felt so wasteful financially and materially. Renting allows me to wear high-quality garments without cluttering my wardrobe."),
    ("en-US-GuyNeural", "That makes total sense. But do you think it's as green as marketing claims suggest?"),
    ("en-US-JennyNeural", "That's my main hesitation. The delivery and dry-cleaning logistics create their own carbon footprint, which defeats the environmental purpose if garments are shuttled back and forth across the country by courier every three days."),
    ("en-US-GuyNeural", "I agree completely. Until the transport packaging and chemical cleaning methods become truly circular, the net ecological gain remains questionable."),
]

MOCK_1_Q10_Q14 = [
    ("en-GB-LibbyNeural", "Speaker 1."),
    ("en-GB-RyanNeural", "Running is fundamentally my escape from a hyper-connected workday. When I'm out on the trail along the riverbank, my phone is switched off, and my mind completely decompresses. It's my daily meditation, where the constant barrage of emails evaporates."),
    ("en-GB-LibbyNeural", "Speaker 2."),
    ("en-AU-NatashaNeural", "I never considered myself athletic in my twenties. But three years ago, my physician gave me a serious wake-up call regarding my cholesterol and cardiovascular risks. Taking up jogging was non-negotiable medical prevention, and it turned my health around."),
    ("en-GB-LibbyNeural", "Speaker 3."),
    ("en-US-JennyNeural", "For me, running alone always felt tedious. Joining a weekend running club introduced me to people from completely different walks of life. We push each other through the final kilometers and share breakfast afterwards. That social camaraderie keeps me going."),
    ("en-GB-LibbyNeural", "Speaker 4."),
    ("en-GB-LibbyNeural", "I am intensely motivated by measurable performance data. Chasing my personal best on the clock provides a tangible sense of achievement that nothing else matches. Every split second shaved off my marathon time validates months of structured discipline."),
    ("en-GB-LibbyNeural", "Speaker 5."),
    ("en-US-GuyNeural", "My job involves constant international travel. Whenever I visit a new city for conferences, I wake up at dawn and run ten kilometers through historic residential neighborhoods. It gives you an intimate perspective on a place you never get from a tour bus or taxi window."),
]

MOCK_1_Q15_Q19 = [
    ("en-GB-SoniaNeural", """Good afternoon, and welcome to this symposium on marine conservation engineering. Today, I'll be outlining our three-year coral reef micro-fragmentation initiative off the southern barrier shoals.

Before launching the project, the research team spent eighteen months surveying damaged barrier reefs, identifying resilient coral colonies that possessed natural thermal tolerance. These parent colonies had survived two successive bleaching episodes without necrotic collapse.

Once these parent colonies were selected, we transported fragments to our shore nursery. Here, we implemented a technique known as micro-fragmentation. By cutting the coral into tiny one-centimeter pieces, we stimulated an innate healing mechanism that accelerated their growth rate up to forty times faster than normal.

After six months of nursery cultivation, the mature fragments were transported by divers and affixed to degraded reef substrates using a non-toxic marine adhesive. This secured them against heavy storm surges.

However, newly transplanted corals are easily smothered by aggressive turf algae. To solve this, we introduced native herbivorous sea urchins, which acted as natural cleaners, grazing the surrounding rock surfaces clean of competing macro-algae.

Looking forward, the true benchmark of our success won't merely be total reef acreage, but genetic diversity, ensuring these restored reefs can withstand future marine heatwaves and pathogen outbreaks. Thank you."""),
]


# ==============================================================================
# MOCK TEST 2 SCRIPTS
# ==============================================================================

MOCK_2_Q1 = [
    ("en-GB-SoniaNeural", "Excuse me, Station Master, I was on the 8:15 express from Edinburgh. I think I left a personal belonging on the luggage rack in Coach B."),
    ("en-GB-ThomasNeural", "Let me check the registry. Several items were logged from that service—a woollen scarf, an electronic tablet, and an artist's portfolio."),
    ("en-GB-SoniaNeural", "No, I had my tablet and scarf securely in my backpack. But when I reached the platform, I realised my vintage leather sketchbook was gone. It contains three months of hand-drawn coastal maps."),
    ("en-GB-ThomasNeural", "Ah! Bound with brown calfskin and an embossed brass clasp? The guard handed that in ten minutes ago. Right here, safe and sound."),
    ("en-GB-SoniaNeural", "What a relief! Thank you ever so much."),
]

MOCK_2_Q2 = [
    ("en-GB-SoniaNeural", "What an evening service! When the main electrical junction blew during the dinner rush, I thought we'd have to refund everyone and shut the doors."),
    ("en-GB-RyanNeural", "Switching instantly to the wood-fired hearth outside seemed completely reckless at first. But looking back, working by candlelight and simplifying the menu on the fly pushed us out of our comfort zone."),
    ("en-GB-SoniaNeural", "Learning to calibrate cooking temperatures solely by flame rather than digital dials taught us more in three hours than a month in culinary school."),
    ("en-GB-RyanNeural", "Couldn't agree more. That forced pivot gave the whole brigade a real surge of confidence."),
]

MOCK_2_Q3_Q7 = [
    ("en-GB-LibbyNeural", "Welcome to Exploration Quarterly. With us is Dr. Julian Croft, an exploratory cave diver who recently charted twelve kilometers of submerged passages beneath the Yucatan peninsula. Julian, having climbed alpine summits for years, what pulled you towards flooded cave systems?"),
    ("en-GB-RyanNeural", "On mountains, satellite topography has already charted every ridge. In a submerged labyrinth, however, you enter a domain of absolute sensory deprivation where human eyes have never witnessed the geology. That sheer absence of pre-existing maps proved irresistible."),
    ("en-GB-LibbyNeural", "It must be extraordinarily demanding physically."),
    ("en-GB-RyanNeural", "Physical fitness is baseline, but the true trial was navigating the ultra-narrow silt restrictions—passages where you must unclip your tanks, push them ahead of you, and wriggle through blind without stirring up fine limestone sediment."),
    ("en-GB-LibbyNeural", "Your expedition made global headlines after stumbling upon prehistoric paleontological remains."),
    ("en-GB-RyanNeural", "Indeed. Discovering Pleistocene giant sloth skeletons over twelve kilometers inland proves that these cave systems were bone-dry valleys during the last glacial maximum, before catastrophic sea level rise engulfed them twelve thousand years ago."),
    ("en-GB-LibbyNeural", "Microbiologists are also analyzing your water samples. Why are these secluded environments so medically significant?"),
    ("en-GB-RyanNeural", "Over millions of years of evolutionary isolation, cave bacteria have synthesized unique antimicrobial compounds to outcompete rivals—compounds that demonstrate potent efficacy against drug-resistant hospital superbugs."),
    ("en-GB-LibbyNeural", "Julian, what core philosophy would you impart to aspiring cave researchers?"),
    ("en-GB-RyanNeural", "Never mistake technological sophistication for wilderness competence. Drones and rebreathers are helpful, but if you cannot read rock strata intuitively with your fingertips and stay calm when all digital instruments fail, technology won't save you."),
]

MOCK_2_Q8_Q9 = [
    ("en-US-GuyNeural", "I've been playing that new wilderness survival title, and I was struck by how little pre-scripted cinematic storytelling it uses."),
    ("en-US-JennyNeural", "That's deliberate emergent narrative design. When a player loses an irreplaceable companion because of a risky tactical decision they made during a blizzard, that personal grief resonates ten times deeper than watching a pre-rendered death animation."),
    ("en-US-GuyNeural", "I agree the emotional stakes feel authentic. But isn't there a risk that player freedom causes the overarching narrative to lose momentum?"),
    ("en-US-JennyNeural", "Absolutely. If you give players total systemic freedom without narrative anchors, they often wander aimlessly without any sense of pacing or climax. The craft lies in creating dynamic constraints."),
]

MOCK_2_Q10_Q14 = [
    ("en-GB-LibbyNeural", "Speaker 1 (Julian)."),
    ("en-GB-RyanNeural", "I spent fifteen years as a corporate merger banker in the City of London, earning high salaries but feeling profoundly detached from physical reality. Stepping away to establish an offshore sailing academy in Cornwall was terrifying initially, but being buffeted by Atlantic squalls and reading tide charts brought a grounded mental calm that high finance never offered."),
    ("en-GB-LibbyNeural", "Speaker 2 (Natasha)."),
    ("en-AU-NatashaNeural", "As a pediatric surgeon, I lived on adrenaline and four hours of sleep for nearly two decades. Then, at forty-eight, I suffered a stress-induced cardiac scare. My physician told me plainly that if I didn't change my lifestyle, I wouldn't see my grandchildren grow up. I retrained as a landscape designer specializing in sensory memory gardens."),
    ("en-GB-LibbyNeural", "Speaker 3 (Guy)."),
    ("en-US-GuyNeural", "I was a lead algorithm engineer for a prominent ad-tech firm. One morning, looking at our engagement telemetry, I felt this profound moral emptiness knowing my code was deliberately designed to maximize compulsive screen addiction among teenagers. I resigned that week and now teach physics at an inner-city school."),
    ("en-GB-LibbyNeural", "Speaker 4 (Sonia)."),
    ("en-GB-SoniaNeural", "In central government, the bureaucratic lethargy was paralyzing. Every creative initiative drowned in committee red tape and defensive memos. Opening an artisan sourdough bakery gave me full autonomy over every loaf, connecting directly with our local neighborhood every dawn."),
    ("en-GB-LibbyNeural", "Speaker 5 (William)."),
    ("en-AU-WilliamMultilingualNeural", "My entire week used to be corporate accounting, but whenever I took annual leave, I vanished into remote archives studying seventeenth-century maritime records. Eventually, I realized life was too brief to keep my passion confined to weekends. I completed an archival conservation master's degree and now work as a rare book conservator."),
]

MOCK_2_Q15_Q19 = [
    ("en-GB-LibbyNeural", """Good morning, delegates. In this lecture, I will discuss the marine archaeology of the Kronan-Nord, a seventeenth-century Baltic warship wrecked in sixteen-seventy-six.

Unlike wooden wrecks in warmer oceans, the Baltic sea bed provides exceptional preservation. The ship timbers survived virtually intact due to low water salinity combined with complete anoxic sediments that prevent the proliferation of shipworm, which usually devours submerged wood within decades.

To excavate the delicate interior cabins without damaging brittle parchment and navigation tools, the underwater team deployed a specialized gentle water-dredge that operated via controlled hydrostatic suction, lifting silt grain by grain.

Chemical testing of recovered caulking delivered surprising insights: the pitch was infused with pine resin and juniper oils, showcasing an unexpected level of botanical chemistry applied to extend hull resilience against ice friction.

Once recovered, waterlogged oak timbers require delicate stabilization. They were immersed in an aqueous bath of polyethylene glycol, a synthetic wax that gradually displaces trapped water molecules over twelve months, preventing cell collapse when exposed to dry air.

Ultimately, this site is historically invaluable because the cargo contained coins, spices, and textiles offering material evidence of undocumented maritime trade networks between Scandinavia and the Levant. Thank you."""),
]


# ==============================================================================
# MOCK TEST 3 SCRIPTS
# ==============================================================================

MOCK_3_Q1 = [
    ("en-GB-SoniaNeural", "Pardon me, Visitor Services desk? I was sketching in the Victorian Fernery about twenty minutes ago, and I seem to have left a family heirloom behind on the iron bench."),
    ("en-GB-RyanNeural", "Let's see. Several visitors handed in items this morning. Someone just brought in a pair of reading glasses, a silk umbrella, and an ornate pocket compass."),
    ("en-GB-SoniaNeural", "An ornate compass! Yes, it's an eighteen-nineties maritime brass compass engraved with nautical coordinates on the casing."),
    ("en-GB-RyanNeural", "That matches the description on our log perfectly. A brass compass with coordinates. Here you are!"),
    ("en-GB-SoniaNeural", "What an incredible relief. Thank you so much for your assistance!"),
]

MOCK_3_Q2 = [
    ("en-GB-RyanNeural", "Now that our architectural firm has completed the six-month pilot of the four-day working week, how has it affected your project delivery?"),
    ("en-GB-SoniaNeural", "Honestly, having Friday entirely free has completely transformed my cognitive recovery. When Monday rolls around, I no longer feel that chronic mental fog. Our team's architectural drafts are sharper, and we've actually cut iterative revision cycles in half."),
    ("en-GB-RyanNeural", "I agree. We used to spend Mondays endlessly correcting errors caused by Friday afternoon fatigue. Being well-rested makes the design process far more decisive."),
]

MOCK_3_Q3_Q7 = [
    ("en-GB-RyanNeural", "Welcome to Sound and Ecology. Today we are joined by Dr. Naomi Chen, an acoustic ecologist who records pristine acoustic environments in the Patagonian ice fields. Naomi, you began your career as a classical percussionist. What led you to acoustic ecology?"),
    ("en-AU-NatashaNeural", "As a musician, you listen for rhythm, frequency density, and timbre. While recording wilderness soundscapes in graduate school, I realized that measuring natural acoustic balance is the most sensitive diagnostic tool for ecosystem vitality. Long before species visibly disappear, their vocal balance unravels."),
    ("en-GB-RyanNeural", "Operating microphones in sub-polar conditions must pose extreme technical difficulties."),
    ("en-AU-NatashaNeural", "The cold is manageable with insulated casing. The true enemy is low-frequency infrasound turbulence generated by katabatic winds roaring off the ice sheet, which can overload microphone preamps without human ears even hearing the wind directly."),
    ("en-GB-RyanNeural", "Your hydrophone recordings beneath glacial terminal faces have generated significant glaciological interest. What do they tell us?"),
    ("en-AU-NatashaNeural", "Before a major glacial calving event occurs, the internal ice fabric emits high-frequency micro-fracture acoustic bursts. By analyzing these acoustic pulses, we can forecast structural collapse days before surface fissures appear from orbit."),
    ("en-GB-RyanNeural", "You also noted worrying changes among sub-Antarctic migratory songbirds."),
    ("en-AU-NatashaNeural", "Yes, what alarmed us was the rapid acoustic homogenization and collapse of vocal frequency diversity. What used to be an intricate multi-layered counterpoint across different elevations is collapsing into acoustic monoculture as climate shifts displace specialist species."),
    ("en-GB-RyanNeural", "Finally, how should environmental scientists communicate these sonic crises to the public?"),
    ("en-AU-NatashaNeural", "Don't rely merely on sterile decibel charts and spreadsheets. Let people immerse their ears directly in the soundscape. When people hear the visceral groan of a dying glacier or an eerie dawn chorus silence, emotional comprehension happens instantly."),
]

MOCK_3_Q8_Q9 = [
    ("en-GB-LibbyNeural", "Have you noticed how many historic city squares in central London have been purchased and designated as privately owned public spaces?"),
    ("en-GB-RyanNeural", "It's pervasive. The moment private security notices someone sitting without buying an expensive espresso, or attempting to distribute a community leaflet, they are discreetly escorted away."),
    ("en-GB-LibbyNeural", "Precisely. Corporate management replaces genuine civic life with sanitized commercial hygiene. True civic spaces must tolerate social friction, spontaneous public assembly, and demographic diversity."),
    ("en-GB-RyanNeural", "I couldn't agree more. If public space is conditional on continuous consumer spending, it ceases to be public in any meaningful democratic sense."),
]

MOCK_3_Q10_Q14 = [
    ("en-GB-LibbyNeural", "Speaker 1 (Mountain Dog)."),
    ("en-GB-RyanNeural", "I was trekking along a remote ridge in the High Pyrenees during a career sabbatical from corporate consulting. Out of nowhere, an injured stray border collie appeared, limping heavily. I carried him twelve miles down to safety, and nursing him back to health sparked a passion that led me to establish a wildlife rescue sanctuary in North Yorkshire."),
    ("en-GB-LibbyNeural", "Speaker 2 (Tuscan Cello)."),
    ("en-US-JennyNeural", "I was travelling across Italy when a rail strike left me completely stranded in a tiny Tuscan village for two days. Wandering through the cobbled backstreets, I heard resonant cello scales and stumbled upon an open luthier workshop. Watching the master carve spruce soundboards completely captivated me. I apprenticed there and now build bespoke cellos."),
    ("en-GB-LibbyNeural", "Speaker 3 (Botanist Letter)."),
    ("en-AU-WilliamMultilingualNeural", "A courier misdelivered a package of antique correspondence to my flat in Manchester. While returning it to the postal depot, I glanced at a fragile eighteen-eighties envelope addressed to an alpine botanist discussing cryo-preserved high-altitude seeds. That single accidental glimpse ignited a fascination that led to my current career in alpine seed banking."),
    ("en-GB-LibbyNeural", "Speaker 4 (Newcastle Printmaker)."),
    ("en-GB-SoniaNeural", "I was caught in an intense sudden hailstorm in Newcastle and ducked under the awning of a traditional letterpress print shop. The printer invited me inside to dry off and let me pull the heavy cast-iron lever of an eighteen-sixties Albion press. The sensory beauty of inked metal type on rag paper convinced me to leave public relations and launch a literary poetry press."),
    ("en-GB-LibbyNeural", "Speaker 5 (Hebrides Dialect)."),
    ("en-GB-ThomasNeural", "I was waiting for a delayed ferry on the Isle of Lewis when I overheard two elderly crofters conversing in an archaic Hebridean dialect, full of poetic maritime terminology I had never encountered. Realizing this linguistic heritage was vanishing unrecorded spurred me to leave accounting and retrain as a descriptive field linguist."),
]

MOCK_3_Q15_Q19 = [
    ("en-GB-RyanNeural", """Good afternoon. In this lecture, I will discuss the conservation ecology of Britain's temperate Celtic rainforests, often referred to as Atlantic woodland.

These rare oceanic ecosystems depend upon hyper-humid microclimates shaped by the Gulf Stream, characterized by mild winters, heavy precipitation, and high annual cloud cover.

The primary ecological glory of these woods lies in their epiphytic lower plants. Lichens and bryophytes are exceptionally sensitive because they lack roots and absorb nutrients directly from atmospheric moisture, making them extraordinary bio-indicators.

However, sensitive ancient woodland species are experiencing severe declines due to chronic nitrogen pollution from agricultural runoff and vehicular exhaust, which favors fast-growing nitrophilic algae over delicate lichen thalli.

Furthermore, natural recolonization across fragmented valley woodlands is severely impeded because many temperate lichen species possess heavy spores with very limited dispersal radii, rarely travelling beyond fifty to one hundred meters from parent trees.

To bridge these isolated habitats, our research station is actively trialling micro-translocation strategies: gently affixing minute lichen thalli onto suitable host trees in regenerating woodland corridors using biodegradable botanical gums. Early survival rates exceed eighty percent. Thank you."""),
]


async def run_all_generation(force: bool = False, test_id: int = 0):
    print("================================================================")
    print("REGENERATING CAMBRIDGE MOCK TEST LISTENING AUDIO VIA EDGE-TTS")
    print(f"Target Directory: {MOCK_DIR}")
    print("================================================================\n")

    tasks = [
        # Mock Test 1
        ("Mock Test 1: Task 1 (Cafe Lost Keys)", 1, MOCK_1_Q1, MOCK_DIR / "audio/task1_v1.mp3"),
        ("Mock Test 1: Task 2 (Workshop Software Demo)", 1, MOCK_1_Q2, MOCK_DIR / "audio/task2_v1.mp3"),
        ("Mock Test 1: Task 3 (Marcus Thorne Interview)", 1, MOCK_1_Q3_Q7, MOCK_DIR / "audio/task3_v1.mp3"),
        ("Mock Test 1: Task 4 (Fashion Rental Discussion)", 1, MOCK_1_Q8_Q9, MOCK_DIR / "audio/task4_v1.mp3"),
        ("Mock Test 1: Task 5 (Running Perspectives)", 1, MOCK_1_Q10_Q14, MOCK_DIR / "audio/task5_v1.mp3"),
        ("Mock Test 1: Task 6 (Coral Reef Restoration)", 1, MOCK_1_Q15_Q19, MOCK_DIR / "audio/task6_v1.mp3"),

        # Mock Test 2
        ("Mock Test 2: Task 1 (Edinburgh Express Sketchbook)", 2, MOCK_2_Q1, MOCK_DIR / "audio/task1_v2.mp3"),
        ("Mock Test 2: Task 2 (Apprentice Chefs Fire Kitchen)", 2, MOCK_2_Q2, MOCK_DIR / "audio/task2_v2.mp3"),
        ("Mock Test 2: Task 3 (Julian Croft Speleology Interview)", 2, MOCK_2_Q3_Q7, MOCK_DIR / "audio/task3_v2.mp3"),
        ("Mock Test 2: Task 4 (Game Storytelling Discussion)", 2, MOCK_2_Q8_Q9, MOCK_DIR / "audio/task4_v2.mp3"),
        ("Mock Test 2: Task 5 (Mid-Life Career Transitions)", 2, MOCK_2_Q10_Q14, MOCK_DIR / "audio/task5_v2.mp3"),
        ("Mock Test 2: Task 6 (Kronan-Nord Baltic Shipwreck)", 2, MOCK_2_Q15_Q19, MOCK_DIR / "audio/task6_v2.mp3"),

        # Mock Test 3
        ("Mock Test 3: Task 1 (Fernery Brass Compass)", 3, MOCK_3_Q1, MOCK_DIR / "audio/task1_v3.mp3"),
        ("Mock Test 3: Task 2 (4-Day Week Architects)", 3, MOCK_3_Q2, MOCK_DIR / "audio/task2_v3.mp3"),
        ("Mock Test 3: Task 3 (Naomi Chen Acoustic Ecology)", 3, MOCK_3_Q3_Q7, MOCK_DIR / "audio/task3_v3.mp3"),
        ("Mock Test 3: Task 4 (Privatized Plazas Discussion)", 3, MOCK_3_Q8_Q9, MOCK_DIR / "audio/task4_v3.mp3"),
        ("Mock Test 3: Task 5 (Serendipitous Life Pivots)", 3, MOCK_3_Q10_Q14, MOCK_DIR / "audio/task5_v3.mp3"),
        ("Mock Test 3: Task 6 (Celtic Rainforest Lichens)", 3, MOCK_3_Q15_Q19, MOCK_DIR / "audio/task6_v3.mp3"),
    ]

    filtered_tasks = [t for t in tasks if (test_id == 0 or t[1] == test_id)]
    for title, tid, segments, out_path in filtered_tasks:
        print(f"--> Generating: {title}...")
        await build_multi_speaker_track(segments, out_path, force=force)

    print("\n[COMPLETE] Audio synthesis task finished.")


def main():
    parser = argparse.ArgumentParser(description="Generate mock test listening audio using Edge TTS.")
    parser.add_argument("--force", action="store_true", help="Force overwrite existing audio files.")
    parser.add_argument("--test", type=int, default=0, choices=[0, 1, 2, 3], help="Generate only specified test (1, 2, or 3). Default 0 (all).")
    args = parser.parse_args()
    asyncio.run(run_all_generation(force=args.force, test_id=args.test))


if __name__ == "__main__":
    main()
