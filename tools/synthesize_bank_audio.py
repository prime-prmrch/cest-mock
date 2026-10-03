#!/usr/bin/env python3
"""
Synthesize 18 new audio tracks for the expanded Cambridge Listening Bank.
Covers:
- Task 1 (5 variants): Short transactional dialogues (travel, hardware, logistics, furniture, catering)
- Task 2 (5 variants): Short collaborative workplace dialogues (systems rollout, shift swap, marketing, eco-cups, licensing)
- Task 3 (2 variants): Extended interviews (V4: Cold-Chain Logistics, V5: Electronics Repairability)
- Task 4 (2 variants): Discussions (V4: Office Mandates vs Remote, V5: Self-Checkout Automation)
- Task 5 (2 variants): 5-Speaker Multiple Matching (V4: Commute Changes, V5: Relocating to Small Towns)
- Task 6 (2 variants): Monologues/Lectures (V4: Aviation Baggage Logistics, V5: Municipal Water Recycling)
"""

import asyncio
import io
import sys
from pathlib import Path
from typing import List, Tuple
import edge_tts

AUDIO_DIR = Path(__file__).resolve().parent.parent / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)


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
    """Build multi-speaker track by concatenating MP3 frames."""
    if not force and output_path.exists() and output_path.stat().st_size > 1000:
        print(f"  [SKIP] {output_path.name} already exists ({output_path.stat().st_size} bytes).")
        return

    combined = io.BytesIO()
    for voice, text in segments:
        data = await synthesize_bytes(text, voice, rate=rate, pitch=pitch)
        combined.write(data)
    output_path.write_bytes(combined.getvalue())
    print(f"  [OK] Generated {output_path.name} ({len(combined.getvalue())} bytes)")


# ==============================================================================
# TASK 1: SHORT TRANSACTIONAL DIALOGUES (5 VARIANTS)
# ==============================================================================

TASK1_V1 = [
    ("en-GB-SoniaNeural", "Excuse me, the indicator board shows the 17:15 express to Bristol Parkway has been replaced by a coach, but I hold a seat reservation on the through train."),
    ("en-GB-RyanNeural", "Yes, engineering crews are conducting urgent overhead wire repairs past Didcot. The replacement express coach departs from Bay 4 outside in ten minutes, though with Friday motorway congestion you won't pull in until after seven o'clock. Alternatively, you could take the 17:28 service routed via Gloucester. It's a slightly longer orbital loop, but it stays on the rails and arrives at 18:45."),
    ("en-GB-SoniaNeural", "I really cannot face sitting in motorway gridlock, even if the coach leaves sooner. I'll take the rail detour via Gloucester."),
    ("en-GB-RyanNeural", "Right then. Head down to Platform 3; that service is already boarding."),
]

TASK1_V2 = [
    ("en-GB-RyanNeural", "Good morning. I bought a multi-channel USB audio interface here three weeks ago, but the phantom power switch on Channel 2 has failed completely."),
    ("en-GB-SoniaNeural", "I can pull up your invoice on the terminal. Under our standard 30-day guarantee, we can either issue a direct replacement unit or credit your store account. However, if you prefer an outright refund to your bank card, our diagnostic workshop must test the hardware first, which usually takes around ten working days."),
    ("en-GB-RyanNeural", "I have client recording sessions scheduled starting next Monday, so waiting two weeks for workshop testing and a bank transfer isn't viable. Please just give me a fresh replacement unit from the shelf."),
    ("en-GB-SoniaNeural", "Certainly. I'll fetch a sealed box from the stockroom right away."),
]

TASK1_V3 = [
    ("en-US-JennyNeural", "Hello, dispatch desk? I'm tracking order 408 for our regional showroom opening on Friday morning. The tracker shows the display stands are still sitting at your central hub."),
    ("en-US-GuyNeural", "Let me check the freight manifest. Yes, our standard freight shuttle to your downtown premises doesn't run until Friday afternoon, which would miss your morning setup cutoff."),
    ("en-US-JennyNeural", "Is there any way we can collect the crates ourselves first thing Thursday?"),
    ("en-US-GuyNeural", "If you have a transport van, I can reroute the pallet to our Westside industrial depot overnight. You'll be able to sign for it at the cargo loading bay as early as 7:30 Thursday morning."),
    ("en-US-JennyNeural", "That solves our problem entirely. Please reroute it to Westside depot."),
]

TASK1_V4 = [
    ("en-GB-SoniaNeural", "Hello, I'm calling regarding our pending bespoke order for six birch conference tables. We just measured the renovated meeting pod, and the rectangular 2.4-meter tables will obstruct the emergency fire exit door."),
    ("en-GB-RyanNeural", "Our joinery workshop hasn't begun cutting the timber yet, so we can still amend the specifications without a cancellation fee. What dimensions do you require?"),
    ("en-GB-SoniaNeural", "Can we switch them to circular tables with a 1.6-meter diameter? That would leave ample clearance around the perimeter."),
    ("en-GB-RyanNeural", "Circular birch tables are actually standard stock. Switching the profile will also reduce the unit price by fifteen percent, which I'll credit against your initial invoice."),
    ("en-GB-SoniaNeural", "That's wonderful news. Let's make that adjustment."),
]

TASK1_V5 = [
    ("en-AU-NatashaNeural", "Good afternoon. We're looking into hosting a full-day executive development workshop for thirty attendees next month. Does the room hire charge include audiovisual projection facilities?"),
    ("en-AU-WilliamMultilingualNeural", "The standard hire fee for the Somerville Suite is £450 per day, which includes high-definition projection and podium microphones. However, if your party books our corporate buffet lunch package at £25 per delegate, the entire £450 room hire charge is waived automatically."),
    ("en-AU-NatashaNeural", "With thirty delegates, the buffet comes to £750, whereas hire plus external catering would exceed £900. Let's lock in the buffet package and take advantage of the room waiver."),
    ("en-AU-WilliamMultilingualNeural", "Excellent choice. I'll prepare and email your booking confirmation."),
]


# ==============================================================================
# TASK 2: SHORT COLLABORATIVE WORKPLACE DIALOGUES (5 VARIANTS)
# ==============================================================================

TASK2_V1 = [
    ("en-GB-RyanNeural", "Elena, the third-party database connector won't pass penetration testing before the 15th. Do we postpone the team rollout?"),
    ("en-GB-SoniaNeural", "If we push back the deployment date again, our fiscal year budget authorization expires. Why not roll out the front-end interface as planned, and allow back-end records to sync across the subsequent weekend?"),
    ("en-GB-RyanNeural", "Management would be satisfied, but our frontline agents will have to manually re-enter customer queries for five days. They will be completely overwhelmed."),
    ("en-GB-SoniaNeural", "Fair point. Let's draft in two temporary contract administrators from central pool to absorb the manual entry backlog rather than delaying the release."),
    ("en-GB-RyanNeural", "Agreed. I'll notify HR to source the contractors."),
]

TASK2_V2 = [
    ("en-GB-SoniaNeural", "Marcus, three of our weekend inventory team have called in sick with seasonal flu, and we have the annual stock audit starting at dawn on Saturday."),
    ("en-GB-RyanNeural", "If we authorize mandatory weekend overtime for the weekday team, we'll breach our quarterly payroll allowance and face corporate penalties."),
    ("en-GB-SoniaNeural", "What if we swap shifts with next Tuesday's restocking crew? They can cover Saturday's audit at standard hourly rates, and take compensatory time off next week when foot traffic is low."),
    ("en-GB-RyanNeural", "That keeps payroll within limits and ensures the audit is completed by experienced hands. Let's draft the revised roster right away."),
]

TASK2_V3 = [
    ("en-US-JennyNeural", "Looking at our third-quarter conversion data, our digital display ad campaigns are generating impressions, but our actual subscription sales are flatlining."),
    ("en-US-GuyNeural", "I've been warning that prospective clients find banner ads intrusive and tune them out. In contrast, our bi-weekly industry insights newsletter has a 42% open rate and accounts for most qualified inquiries."),
    ("en-US-JennyNeural", "So you recommend reallocating the remainder of the ad budget into expanding our content team to produce specialized industry briefs?"),
    ("en-US-GuyNeural", "Precisely. Delivering high-value technical analysis directly to subscribers builds authority and drives organic conversions without paying ad networks."),
    ("en-US-JennyNeural", "Let's reallocate the funds starting next month."),
]

TASK2_V4 = [
    ("en-AU-NatashaNeural", "We're launching our reusable coffee cup scheme next Monday. Staff pay a £2 deposit for a branded travel mug, which is refunded when they return it to any café station."),
    ("en-AU-WilliamMultilingualNeural", "I support reducing single-use paper waste, but has anyone considered the sanitization logistics? If staff dump unrinsed mugs in return bins over the weekend, our facilities staff will be dealing with hygiene complaints."),
    ("en-AU-NatashaNeural", "We've installed commercial high-temperature dishwashers on every floor that sanitize each batch in three minutes. Our catering apprentices will clear the collection bins three times daily."),
    ("en-AU-WilliamMultilingualNeural", "In that case, the hygiene risk is mitigated. Count on facilities to install the drop-off signage."),
]

TASK2_V5 = [
    ("en-GB-SoniaNeural", "The vendor is offering a 20% discount if we commit to a three-year enterprise software agreement for eighty seats."),
    ("en-GB-RyanNeural", "A 20% saving sounds attractive on paper, but our department is restructuring next quarter, and our headcount may drop to fifty once automated ticketing takes over."),
    ("en-GB-SoniaNeural", "If we're locked into eighty seats, that 20% discount turns into a heavy financial liability within six months."),
    ("en-GB-RyanNeural", "Exactly. It's much safer to negotiate a quarterly rolling agreement at the standard tier. We retain the flexibility to scale down seat licenses as our team composition evolves."),
    ("en-GB-SoniaNeural", "Sensible approach. I'll instruct the vendor that we require flexible quarterly terms."),
]


# ==============================================================================
# TASK 3: EXTENDED INTERVIEWS (VARIANTS 4 & 5)
# ==============================================================================

TASK3_V4 = [
    ("en-GB-SoniaNeural", "Welcome to Commerce and Logistics. Today we speak with Rachel Vance, operations director for a nationwide cold-chain distribution network. Rachel, having managed standard dry warehousing for years, what pulled you toward cold-chain logistics?"),
    ("en-GB-LibbyNeural", "In ambient freight, a few hours' delay rarely compromises the cargo. But in cold-chain distribution, you are operating within razor-thin thermal tolerances where a two-degree deviation can ruin thousands of pounds of pharmaceuticals or fresh produce. That unforgiving operational precision fascinated me."),
    ("en-GB-SoniaNeural", "Fleet operators are rapidly adopting electric refrigerated lorries. What has been the primary engineering hurdle in real-world deployment?"),
    ("en-GB-LibbyNeural", "Propulsion batteries perform reliably. The real challenge is the enormous parasitic draw of the onboard refrigeration compressors during peak summer heatwaves. If a driver is caught in severe highway congestion, the thermal cooling system can deplete up to forty percent of vehicle range before reaching the delivery depot."),
    ("en-GB-SoniaNeural", "Your company recently automated its central sorting facility in Northampton. How did this transformation affect warehouse floor personnel?"),
    ("en-GB-LibbyNeural", "Many feared massive job losses, but our headcount actually remained stable. Floor operatives were retrained from grueling manual pallet lifting into supervisory technicians overseeing autonomous mobile robots and verifying telemetry logs."),
    ("en-GB-SoniaNeural", "Supermarkets often experience sudden demand spikes during unexpected bank holiday weather. How does your team adapt without accumulating excess inventory?"),
    ("en-GB-LibbyNeural", "Rather than relying on historical quarterly sales averages, we integrated live point-of-sale store telemetry with regional meteorological forecasting models. This allows us to rebalance stock between regional hubs twenty-four hours before retail shelves empty."),
    ("en-GB-SoniaNeural", "Finally, what counsel would you give young professionals considering a career in commercial logistics?"),
    ("en-GB-LibbyNeural", "Resist the urge to stay behind central analytics dashboards in head office. Spend your first two years on the loading bays, dispatching trailers and speaking with drivers. Experiencing the physical realities of supply friction on the ground makes you a far sharper strategist later."),
]

TASK3_V5 = [
    ("en-US-GuyNeural", "Welcome to Technology in Practice. Today we are joined by David Cho, an industrial appliance engineer whose designs for modular domestic electronics have challenged consumer electronics manufacturing. David, why did you decide to leave prominent manufacturing firms to advocate for modular appliances?"),
    ("en-US-JennyNeural", "I spent a decade watching manufacturers deliberately glue components together so that a trivial broken plastic gear rendered an entire three-hundred-dollar washing machine or food processor obsolete. That calculated wastefulness contradicted every principle of sustainable engineering I held."),
    ("en-US-GuyNeural", "Designing products that consumers can disassemble at home must introduce major engineering challenges."),
    ("en-US-JennyNeural", "Without question. Standard mass production relies on snap-fits and chemical adhesives because they save manufacturing assembly seconds. Designing modular, screw-fastened chassis with standardized connectors without making the exterior housing bulky or vulnerable to water ingress required four years of structural prototyping."),
    ("en-US-GuyNeural", "What has been the most surprising consumer reaction since releasing your modular kitchen appliances?"),
    ("en-US-JennyNeural", "We anticipated consumers might find home repairs intimidating. Instead, customer telemetry revealed that owners found diagnosing faults through our open-source smartphone diagnostic app surprisingly satisfying. It restored a sense of ownership that modern sealed electronics had eroded."),
    ("en-US-GuyNeural", "Supplying replacement parts across multiple countries often proves logistically prohibitive. How do you manage your spare components inventory?"),
    ("en-US-JennyNeural", "Rather than shipping minute replacement parts by air freight from an overseas central factory, we partnered with localized micro-distribution hubs and shared standard CAD files with certified regional repair workshops. Ninety percent of replacement parts reach customer doorsteps within twenty-four hours."),
    ("en-US-GuyNeural", "Finally, how do you view upcoming international right-to-repair legislation?"),
    ("en-US-JennyNeural", "Legal mandates requiring manufacturers to supply spare parts and schematics for ten years will fundamentally transform the industry. When companies can no longer rely on premature product obsolescence for recurring revenue, build quality and reparability will become primary competitive advantages."),
]


# ==============================================================================
# TASK 4: MULTI-SPEAKER DISCUSSIONS (VARIANTS 4 & 5)
# ==============================================================================

TASK4_V4 = [
    ("en-GB-RyanNeural", "Have you reviewed the executive announcement mandating that all department staff attend the corporate office at least three days each week?"),
    ("en-GB-SoniaNeural", "I have, and I find the blanket mandate frustrating. When I'm in our open-plan office, the constant phone chatter and desk foot traffic make in-depth financial drafting virtually impossible. I achieve twice as much analytical work from my home study."),
    ("en-GB-RyanNeural", "I recognize the acoustic distractions, but we cannot ignore how fragmented cross-departmental coordination has become. When teams only collaborate over scheduled thirty-minute video calls, spontaneous troubleshooting and informal mentoring completely vanish."),
    ("en-GB-SoniaNeural", "I concede that impromptu collaboration is far more natural when sharing the same physical whiteboard. But unless management introduces dedicated quiet zones alongside communal desks, demanding three days in the office simply trades cognitive productivity for visible attendance."),
]

TASK4_V5 = [
    ("en-US-JennyNeural", "I noticed our local supermarket just removed four staffed checkout lanes and replaced them with twelve self-service touch terminals."),
    ("en-US-GuyNeural", "I find self-service convenient if I'm grabbing a sandwich and a coffee during lunch. But when doing a full weekly grocery run with fresh produce and fragile bakery items, the frequent barcode recognition glitches and automated weight warnings negate any speed advantage. You spend half your time waiting for an attendant to scan an override card."),
    ("en-US-JennyNeural", "That's my main grievance as well. Retailers promote automated checkout as a convenience for shoppers, but in reality, they are shifting manual cashier labor directly onto paying customers while reducing store staffing costs."),
    ("en-US-GuyNeural", "Exactly. A balanced hybrid layout where self-service handles small basket transactions while staffed lanes manage complex trolley shops is ideal. Eliminating human cashiers entirely degrades customer goodwill."),
]


# ==============================================================================
# TASK 5: 5 SPEAKERS MULTIPLE MATCHING (VARIANTS 4 & 5)
# ==============================================================================

TASK5_V4 = [
    ("en-GB-LibbyNeural", "Speaker 1 (Ryan)."),
    ("en-GB-RyanNeural", "I used to spend fifty minutes sitting in stationary traffic on the motorway bypass every morning. Six months ago, I invested in an electric commuter bicycle. Cycling through the riverside parkway not only cut my journey time in half, but having that forty minutes of light aerobic exercise creates a clear mental barrier between high-pressure client meetings and arriving home."),
    ("en-GB-LibbyNeural", "Speaker 2 (Natasha)."),
    ("en-AU-NatashaNeural", "Driving all the way into the central medical quarter was bankrupting me financially. Municipal car parking rates increased twice in one year, reaching thirty-five pounds a day. Switching to the suburban park-and-ride bus took a week to get used to, but the monthly savings paid for our family holiday."),
    ("en-GB-LibbyNeural", "Speaker 3 (Jenny)."),
    ("en-US-JennyNeural", "Commuting alone in my car used to feel intensely monotonous. When two colleagues in my neighborhood suggested forming a carpooling rota, I was hesitant about coordinating schedules. But alternating driving duties each week has cut our fuel expenses by two-thirds, and our morning conversations set a cheerful tone for the workday."),
    ("en-GB-LibbyNeural", "Speaker 4 (Guy)."),
    ("en-US-GuyNeural", "After five years of cramming onto packed underground carriages during peak rush hour, I began experiencing acute sensory claustrophobia. One spring morning, I decided to walk the three-and-a-half miles instead. It requires waking forty minutes earlier, but striding across the city bridges completely cleared my morning anxiety."),
    ("en-GB-LibbyNeural", "Speaker 5 (Thomas)."),
    ("en-GB-ThomasNeural", "When our company moved to flexible core working hours, I stopped catching the crowded 7:45 morning train. Traveling on the 9:15 off-peak service means I always get a comfortable table seat with a power socket, allowing me to complete my email correspondence before I even reach the office."),
]

TASK5_V5 = [
    ("en-GB-LibbyNeural", "Speaker 1 (Sonia)."),
    ("en-GB-SoniaNeural", "In London, our growing family was cramped in a two-bedroom terrace with no outdoor space, and upgrading to a larger home was financially impossible. Relocating to a market town in Shropshire allowed us to purchase a detached home with a generous garden for half the price of our London mortgage."),
    ("en-GB-LibbyNeural", "Speaker 2 (William)."),
    ("en-AU-WilliamMultilingualNeural", "Both of my parents were entering their eighties, and managing their doctor visits from three hours away was becoming untenable. When my employer approved permanent remote working, moving back to their small coastal town was an easy choice. Being five minutes away to help with daily errands brings immense peace of mind."),
    ("en-GB-LibbyNeural", "Speaker 3 (Jenny)."),
    ("en-US-JennyNeural", "I spent fifteen years in metropolitan advertising, but every free weekend was spent driving four hours to national parks. Eventually I asked myself why I was spending five days a week in traffic to enjoy two days of fresh air. Moving to Cumbria means mountain trails start right outside my front doorstep."),
    ("en-GB-LibbyNeural", "Speaker 4 (Ryan)."),
    ("en-GB-RyanNeural", "In central Birmingham, commercial rental costs for independent hospitality were astronomical. Moving to a small harbour town gave me the opportunity to lease an old cooperage warehouse at modest rates and open an independent artisan coffee roastery. The local community has been extraordinarily loyal."),
    ("en-GB-LibbyNeural", "Speaker 5 (Libby)."),
    ("en-GB-LibbyNeural", "My daily routine used to involve two connecting commuter trains and a bus ride, totaling nearly three hours every single day. The chronic physical exhaustion was draining my health. Taking a role at a regional council and living two miles away gave me back fifteen hours of my life each week."),
]


# ==============================================================================
# TASK 6: MONOLOGUES / LECTURES (VARIANTS 4 & 5)
# ==============================================================================

TASK6_V4 = [
    ("en-GB-RyanNeural", """Good afternoon. In this industry briefing, I will explain the engineering and logistics infrastructure behind automated baggage handling systems at modern international airports.

When a passenger checks in luggage, the bag tag utilizes high-frequency RFID microchips embedded alongside traditional barcodes, achieving over ninety-nine percent automated tracking accuracy across high-speed sortation networks.

From the check-in hall, conveyor belts route luggage through three-dimensional computed tomography scanners, which inspect internal contents for security hazards without requiring manual unzipping by security personnel.

During flight delays or early check-ins, bags are routed into dynamic high-density racking facilities rather than sitting exposed on outdoor tarmac trolleys, shielding delicate baggage from severe weather.

Out on the apron, ground handling teams deploy electric tug vehicles equipped with telematics sensors that optimize baggage transit routing directly to aircraft cargo holds.

Ultimately, the commercial benchmark of ground logistics efficiency is aircraft turnaround time, ensuring planes do not incur costly airport gate parking surcharges. Thank you."""),
]

TASK6_V5 = [
    ("en-GB-SoniaNeural", """Good morning, delegates. In this presentation, I will examine the multi-stage purification processes utilized in municipal water recycling facilities for industrial cooling and environmental sustainability.

Raw municipal wastewater initially passes through rotary mesh screens to eliminate insoluble plastics and grit before entering primary clarification tanks.

Biological purification occurs within advanced membrane bioreactor chambers, where dense colonies of aerobic microbes digest dissolved organic pollutants.

High-pressure multistage pumps then force the pre-treated effluent through dense polyamide membranes during reverse osmosis, filtering out microscopic salts, pathogens, and pharmaceutical compounds.

Prior to discharge into municipal supply networks, the water undergoes intensive disinfection via ultraviolet irradiation combined with hydrogen peroxide to destroy any lingering trace contaminants.

The purified recycled water is primarily distributed to industrial clients for heavy power station cooling towers, preserving millions of litres of potable drinking water reservoirs annually. Thank you."""),
]


async def run_all_bank_audio():
    print("================================================================")
    print("SYNTHESIZING EXPANDED 18 AUDIO TRACKS FOR LISTENING BANK")
    print(f"Output Directory: {AUDIO_DIR}")
    print("================================================================\n")

    tasks = [
        # Task 1 (5 variants)
        ("Task 1 V1 (Transit Re-routing)", TASK1_V1, AUDIO_DIR / "task1_v1.mp3"),
        ("Task 1 V2 (Hardware Warranty Return)", TASK1_V2, AUDIO_DIR / "task1_v2.mp3"),
        ("Task 1 V3 (Depot Delivery Redirection)", TASK1_V3, AUDIO_DIR / "task1_v3.mp3"),
        ("Task 1 V4 (Furniture Order Adjustment)", TASK1_V4, AUDIO_DIR / "task1_v4.mp3"),
        ("Task 1 V5 (Catering Room Hire Waiver)", TASK1_V5, AUDIO_DIR / "task1_v5.mp3"),

        # Task 2 (5 variants)
        ("Task 2 V1 (Systems Rollout Data Migration)", TASK2_V1, AUDIO_DIR / "task2_v1.mp3"),
        ("Task 2 V2 (Retail Shift Swap)", TASK2_V2, AUDIO_DIR / "task2_v2.mp3"),
        ("Task 2 V3 (Marketing ROI Newsletter Pivot)", TASK2_V3, AUDIO_DIR / "task2_v3.mp3"),
        ("Task 2 V4 (Eco Cup Deposit Scheme)", TASK2_V4, AUDIO_DIR / "task2_v4.mp3"),
        ("Task 2 V5 (Software License Tier)", TASK2_V5, AUDIO_DIR / "task2_v5.mp3"),

        # Task 3 (V4, V5)
        ("Task 3 V4 (Rachel Vance Cold-Chain Logistics)", TASK3_V4, AUDIO_DIR / "task3_v4.mp3"),
        ("Task 3 V5 (David Cho Appliance Repairability)", TASK3_V5, AUDIO_DIR / "task3_v5.mp3"),

        # Task 4 (V4, V5)
        ("Task 4 V4 (Office Presence Policy)", TASK4_V4, AUDIO_DIR / "task4_v4.mp3"),
        ("Task 4 V5 (Supermarket Self-Checkout)", TASK4_V5, AUDIO_DIR / "task4_v5.mp3"),

        # Task 5 (V4, V5)
        ("Task 5 V4 (Changing Commute Modes)", TASK5_V4, AUDIO_DIR / "task5_v4.mp3"),
        ("Task 5 V5 (Relocating to Small Towns)", TASK5_V5, AUDIO_DIR / "task5_v5.mp3"),

        # Task 6 (V4, V5)
        ("Task 6 V4 (Aviation Baggage Logistics)", TASK6_V4, AUDIO_DIR / "task6_v4.mp3"),
        ("Task 6 V5 (Municipal Water Recycling)", TASK6_V5, AUDIO_DIR / "task6_v5.mp3"),
    ]

    for title, segments, out_path in tasks:
        print(f"--> Generating: {title}...")
        await build_multi_speaker_track(segments, out_path, force=True)

    print("\n[COMPLETE] All 18 new bank audio tracks synthesized successfully.")


if __name__ == "__main__":
    asyncio.run(run_all_bank_audio())
