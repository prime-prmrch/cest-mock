#!/usr/bin/env python3
"""
Builds the unified modular item bank `data/bank.json` for the procedural exam generator.
Strictly calibrated to the Cambridge English Skills Test (General) 52-item specification:
- Reading: 33 Questions across Tasks 1–9
- Listening: 19 Questions across Tasks 1–6 (30 neural audio tracks)
- Writing: 2 Tasks (Task 1 Narrative & Task 2 Discursive)
"""

import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TEST_1 = json.loads((DATA_DIR / "test_1.json").read_text(encoding="utf-8"))
TEST_2 = json.loads((DATA_DIR / "test_2.json").read_text(encoding="utf-8"))
TEST_3 = json.loads((DATA_DIR / "test_3.json").read_text(encoding="utf-8"))

bank = {
    "version": "2.0.0",
    "title": "Cambridge English Skills Test (General) Modular Item Bank",
    "reading": {},
    "listening": {},
    "writing": {}
}

# ==============================================================================
# READING TASKS (33 ITEMS TOTAL)
# ==============================================================================

# Task 1: Notices (Pool of 5 variants, Q1)
bank["reading"]["task_1_notices"] = [
    next(tk for tk in TEST_1["reading"] if tk["task"] == 1),
    next(tk for tk in TEST_2["reading"] if tk["task"] == 1),
    next(tk for tk in TEST_3["reading"] if tk["task"] == 1),
    {
        "task": 1,
        "tag": "Task 1 • Notices & Messages",
        "title": "Corporate Facilities Advisory",
        "instruction": "Read the notice and answer the question.",
        "passage": "<strong>CORPORATE FACILITIES ADVISORY</strong><br><em>Annual acoustic testing of building alarm sounders will occur between 14:00 and 15:00 on Wednesday. Sirens will sound in ten-second intervals. Staff are NOT required to evacuate unless alarms ring continuously for over thirty seconds. Normal office work may proceed throughout the test window.</em>",
        "questions": [
            {
                "id": "r_q1", "num": 1, "type": "mc",
                "stem": "1. What should employees do during Wednesday's alarm testing?",
                "options": [
                    {"val": "A", "label": "[A] Evacuate the premises immediately when any siren sounds."},
                    {"val": "B", "label": "[B] Continue working unless the alarm sounds without interruption."},
                    {"val": "C", "label": "[C] Assemble in designated ground floor meeting rooms at 14:00."}
                ],
                "key": "B", "skill": "Factual Accuracy / Conditional Reading (A2-B1)",
                "trap": "[A] conflicts with 'NOT required to evacuate unless alarms ring continuously'; [C] meeting not mentioned."
            }
        ]
    },
    {
        "task": 1,
        "tag": "Task 1 • Notices & Messages",
        "title": "Station Platform Notice",
        "instruction": "Read the notice and answer the question.",
        "passage": "<strong>STATION PLATFORM ADVISORY</strong><br><em>The passenger waiting lounge on Platform 2 is temporarily closed for floor maintenance. Heated shelters remain accessible on Platforms 1 and 3. Complimentary beverage vouchers are available from the customer assistance counter upon presentation of a valid rail travel card.</em>",
        "questions": [
            {
                "id": "r_q1", "num": 1, "type": "mc",
                "stem": "1. What does this station notice announce to travellers?",
                "options": [
                    {"val": "A", "label": "[A] Waiting facilities remain accessible on alternative platforms."},
                    {"val": "B", "label": "[B] Free hot drinks are provided to all ticket holders on Platform 2."},
                    {"val": "C", "label": "[C] All platform shelters are closed until maintenance finishes."}
                ],
                "key": "A", "skill": "Gist & Detail Extraction (A2-B1)",
                "trap": "[B] vouchers available at customer counter, not platform; [C] only Platform 2 lounge closed."
            }
        ]
    }
]

# Task 2: Sentence Cloze (Pool of 5 variants, Q2)
bank["reading"]["task_2_sentence_cloze"] = [
    next(tk for tk in TEST_1["reading"] if tk["task"] == 2),
    next(tk for tk in TEST_2["reading"] if tk["task"] == 2),
    next(tk for tk in TEST_3["reading"] if tk["task"] == 2),
    {
        "task": 2,
        "tag": "Task 2 • Sentence Gap-Fill",
        "title": "Corporate Energy Efficiency",
        "instruction": "Choose the correct word to complete the sentence.",
        "questions": [
            {
                "id": "r_q2", "num": 2, "type": "mc",
                "stem": "2. Installing solar panels across the warehouse roof noticeably [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] the company's annual electricity expenditure.",
                "options": [
                    {"val": "A", "label": "[A] degraded"},
                    {"val": "B", "label": "[B] curtailed"},
                    {"val": "C", "label": "[C] suspended"},
                    {"val": "D", "label": "[D] declined"}
                ],
                "key": "B", "skill": "Formal Commercial Lexis (B2)",
                "trap": "'Curtailed' collocates with expenses/costs; 'declined' is intransitive here."
            }
        ]
    },
    {
        "task": 2,
        "tag": "Task 2 • Sentence Gap-Fill",
        "title": "Application Deadlines",
        "instruction": "Choose the correct word to complete the sentence.",
        "questions": [
            {
                "id": "r_q2", "num": 2, "type": "mc",
                "stem": "2. Job candidates are strongly urged to upload their portfolio well in [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] of the closing date to avoid system congestion.",
                "options": [
                    {"val": "A", "label": "[A] advance"},
                    {"val": "B", "label": "[B] anticipation"},
                    {"val": "C", "label": "[C] ahead"},
                    {"val": "D", "label": "[D] priority"}
                ],
                "key": "A", "skill": "Idiomatic Prepositional Phrase (B1-B2)",
                "trap": "The set phrase is 'in advance of'."
            }
        ]
    }
]

# Task 3: Open Cloze (Pool of 5 texts, Q3–Q7)
t3_texts = [
    next(tk for tk in TEST_1["reading"] if tk["task"] == 3),
    next(tk for tk in TEST_2["reading"] if tk["task"] == 3),
    next(tk for tk in TEST_3["reading"] if tk["task"] == 3),
    {
        "task": 3,
        "tag": "Task 3 • Open Gap-Fill",
        "title": "Airport Express Ticketing",
        "instruction": "Read the text below and think of the word which best fits each gap. Use only ONE word in each gap.",
        "passage": "Modern airport rail shuttles are designed for rapid passenger transit. Travellers who book tickets online prior [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] departure benefit from substantial fare discounts. In addition, digital barcode passes can be scanned directly from smartphone screens, ensuring that passengers spend less time queuing [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] ticket vending machines. Those travelling with oversized luggage are advised to board the middle carriages, [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] dedicated luggage racks are located. Although rail maintenance is scheduled periodically, replacement bus shuttles operate [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] order to guarantee uninterrupted connection to morning flight departures. Passengers should always check live departure screens [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] case platform reassignments occur at short notice.",
        "questions": [
            {"id": "r_q3", "num": 3, "type": "text", "stem": "Gap 3", "key": "to", "skill": "Prepositional Collocation (B2)", "trap": "'prior to'."},
            {"id": "r_q4", "num": 4, "type": "text", "stem": "Gap 4", "key": "at", "skill": "Locative Preposition (B1)", "trap": "Queuing 'at'."},
            {"id": "r_q5", "num": 5, "type": "text", "stem": "Gap 5", "key": "where", "skill": "Relative Adverb (B2)", "trap": "Locational antecedent."},
            {"id": "r_q6", "num": 6, "type": "text", "stem": "Gap 6", "key": "in", "skill": "Purpose Connector (B2)", "trap": "'in order to'."},
            {"id": "r_q7", "num": 7, "type": "text", "stem": "Gap 7", "key": "in", "skill": "Precautionary Idiom (B2)", "trap": "'in case'."}
        ]
    },
    {
        "task": 3,
        "tag": "Task 3 • Open Gap-Fill",
        "title": "Workplace Ergonomics",
        "instruction": "Read the text below and think of the word which best fits each gap. Use only ONE word in each gap.",
        "passage": "With the widespread expansion of hybrid office models, companies are paying closer attention [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] employee posture and workstation setup. Occupational therapists emphasize that prolonged sitting can lead to musculoskeletal fatigue unless monitors are positioned [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] eye level. Rather [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] remaining stationary for hours, workers are encouraged to take brief five-minute walking breaks. Employers who have introduced height-adjustable desks report significant drops in absenteeism, [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] well as marked improvements in daily concentration levels. Ultimately, ergonomics is not merely an optional perk, [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] a critical investment in long-term workplace vitality.",
        "questions": [
            {"id": "r_q3", "num": 3, "type": "text", "stem": "Gap 3", "key": "to", "skill": "Dependent Preposition (B2)", "trap": "'attention to'."},
            {"id": "r_q4", "num": 4, "type": "text", "stem": "Gap 4", "key": "at", "skill": "Preposition of Level (B1)", "trap": "'at eye level'."},
            {"id": "r_q5", "num": 5, "type": "text", "stem": "Gap 5", "key": "than", "skill": "Comparative Connector (B2)", "trap": "'rather than'."},
            {"id": "r_q6", "num": 6, "type": "text", "stem": "Gap 6", "key": "as", "skill": "Additive Phrase (B1)", "trap": "'as well as'."},
            {"id": "r_q7", "num": 7, "type": "text", "stem": "Gap 7", "key": "but", "skill": "Correlative Conjunction (B2)", "trap": "'not merely... but'."}
        ]
    }
]
bank["reading"]["task_3_open_cloze"] = t3_texts

# Task 4: Vocab Cloze (Pool of 5 texts, Q8–Q12)
t4_texts = [
    next(tk for tk in TEST_1["reading"] if tk["task"] == 4),
    next(tk for tk in TEST_2["reading"] if tk["task"] == 4),
    next(tk for tk in TEST_3["reading"] if tk["task"] == 4),
    {
        "task": 4,
        "tag": "Task 4 • Multiple-Choice Gap-Fill",
        "title": "Commercial Fleet Telematics",
        "instruction": "Read the text and choose the correct word for each space.",
        "passage": "Commercial delivery fleets are transforming logistics by adopting satellite telematics systems. By monitoring engine telemetry in real time, fleet managers can [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] mechanical malfunctions before vehicles break down on highways. This preventive approach has noticeably [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] maintenance expenditures across national logistics networks. Furthermore, telematics algorithms calculate optimized route detours that [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] severe congestion during peak morning hours. Drivers also receive constructive automated feedback designed to [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] fuel efficiency through smoother braking. Industry analysts predict that fleet telematics will soon become an essential [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] of corporate supply chain operations.",
        "questions": [
            {
                "id": "r_q8", "num": 8, "type": "mc", "stem": "8. Choose the best word:",
                "options": [{"val": "A", "label": "[A] diagnose"}, {"val": "B", "label": "[B] calculate"}, {"val": "C", "label": "[C] compose"}, {"val": "D", "label": "[D] inspect"}],
                "key": "A", "skill": "Technical Collocation (B2)", "trap": "One 'diagnoses' malfunctions."
            },
            {
                "id": "r_q9", "num": 9, "type": "mc", "stem": "9. Choose the best word:",
                "options": [{"val": "A", "label": "[A] curled"}, {"val": "B", "label": "[B] curtailed"}, {"val": "C", "label": "[C] compressed"}, {"val": "D", "label": "[D] ceased"}],
                "key": "B", "skill": "Formal Lexis (C1)", "trap": "'Curtailed' means reduced or restricted expenditures."
            },
            {
                "id": "r_q10", "num": 10, "type": "mc", "stem": "10. Choose the best word:",
                "options": [{"val": "A", "label": "[A] circumvent"}, {"val": "B", "label": "[B] postpone"}, {"val": "C", "label": "[C] discard"}, {"val": "D", "label": "[D] reject"}],
                "key": "A", "skill": "Logistical Collocation (C1)", "trap": "'Circumvent' means bypass congestion."
            },
            {
                "id": "r_q11", "num": 11, "type": "mc", "stem": "11. Choose the best word:",
                "options": [{"val": "A", "label": "[A] elevate"}, {"val": "B", "label": "[B] amplify"}, {"val": "C", "label": "[C] enhance"}, {"val": "D", "label": "[D] widen"}],
                "key": "C", "skill": "Qualitative Collocation (B2)", "trap": "'Enhance' collocates naturally with efficiency."
            },
            {
                "id": "r_q12", "num": 12, "type": "mc", "stem": "12. Choose the best word:",
                "options": [{"val": "A", "label": "[A] component"}, {"val": "B", "label": "[B] section"}, {"val": "C", "label": "[C] fraction"}, {"val": "D", "label": "[D] ingredient"}],
                "key": "A", "skill": "Categorization (B2)", "trap": "Essential 'component' of operations."
            }
        ]
    },
    {
        "task": 4,
        "tag": "Task 4 • Multiple-Choice Gap-Fill",
        "title": "Retail Customer Loyalty",
        "instruction": "Read the text and choose the correct word for each space.",
        "passage": "In an increasingly competitive retail sector, department stores are rethinking customer loyalty rewards. Traditional plastic reward cards are rapidly being replaced by mobile smartphone applications that [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] personalized discounts based on purchase history. Marketing research shows that shoppers [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] tailored offers far more positively than generic coupons. However, retailers must be cautious not to overwhelm users with excessive notification alerts that [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] their digital goodwill. Stores that preserve transparent privacy policies while delivering tangible value are most likely to [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] enduring relationships with discerning shoppers, thereby establishing a resilient commercial [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] in shifting markets.",
        "questions": [
            {
                "id": "r_q8", "num": 8, "type": "mc", "stem": "8. Choose the best word:",
                "options": [{"val": "A", "label": "[A] dispense"}, {"val": "B", "label": "[B] transmit"}, {"val": "C", "label": "[C] utter"}, {"val": "D", "label": "[D] render"}],
                "key": "A", "skill": "Functional Collocation (B2)", "trap": "Apps 'dispense' discounts."
            },
            {
                "id": "r_q9", "num": 9, "type": "mc", "stem": "9. Choose the best word:",
                "options": [{"val": "A", "label": "[A] regard"}, {"val": "B", "label": "[B] view"}, {"val": "C", "label": "[C] notice"}, {"val": "D", "label": "[D] perceive"}],
                "key": "D", "skill": "Cognitive Reception (C1)", "trap": "'Perceive' offers positively."
            },
            {
                "id": "r_q10", "num": 10, "type": "mc", "stem": "10. Choose the best word:",
                "options": [{"val": "A", "label": "[A] erode"}, {"val": "B", "label": "[B] dilute"}, {"val": "C", "label": "[C] shatter"}, {"val": "D", "label": "[D] decay"}],
                "key": "A", "skill": "Metaphorical Collocation (C1)", "trap": "Alerts 'erode' goodwill."
            },
            {
                "id": "r_q11", "num": 11, "type": "mc", "stem": "11. Choose the best word:",
                "options": [{"val": "A", "label": "[A] cultivate"}, {"val": "B", "label": "[B] nurture"}, {"val": "C", "label": "[C] fabricate"}, {"val": "D", "label": "[D] stimulate"}],
                "key": "A", "skill": "Relational Collocation (C1)", "trap": "'Cultivate' relationships with shoppers."
            },
            {
                "id": "r_q12", "num": 12, "type": "mc", "stem": "12. Choose the best word:",
                "options": [{"val": "A", "label": "[A] foothold"}, {"val": "B", "label": "[B] milestone"}, {"val": "C", "label": "[C] threshold"}, {"val": "D", "label": "[D] foundation"}],
                "key": "A", "skill": "Commercial Register (C1)", "trap": "Commercial 'foothold'."
            }
        ]
    }
]
bank["reading"]["task_4_vocab_cloze"] = t4_texts

# Tasks 5 through 9: Passages & Articles
bank["reading"]["task_5_extended_text"] = [
    next(tk for tk in TEST_1["reading"] if tk["task"] == 5),
    next(tk for tk in TEST_2["reading"] if tk["task"] == 5),
    next(tk for tk in TEST_3["reading"] if tk["task"] == 5)
]

bank["reading"]["task_6_short_article"] = [
    next(tk for tk in TEST_1["reading"] if tk["task"] == 6),
    next(tk for tk in TEST_2["reading"] if tk["task"] == 6),
    next(tk for tk in TEST_3["reading"] if tk["task"] == 6)
]

bank["reading"]["task_7_gapped_sentences"] = [
    next(tk for tk in TEST_1["reading"] if tk["task"] == 7),
    next(tk for tk in TEST_2["reading"] if tk["task"] == 7),
    next(tk for tk in TEST_3["reading"] if tk["task"] == 7)
]

bank["reading"]["task_8_gapped_paragraphs"] = [
    next(tk for tk in TEST_1["reading"] if tk["task"] == 8),
    next(tk for tk in TEST_2["reading"] if tk["task"] == 8),
    next(tk for tk in TEST_3["reading"] if tk["task"] == 8)
]

bank["reading"]["task_9_multiple_matching"] = [
    next(tk for tk in TEST_1["reading"] if tk["task"] == 9),
    next(tk for tk in TEST_2["reading"] if tk["task"] == 9),
    next(tk for tk in TEST_3["reading"] if tk["task"] == 9)
]


# ==============================================================================
# LISTENING: 5 VARIANTS PER TASK (30 TRACKS TOTAL)
# ==============================================================================

# Task 1: 5 Short Transactional Dialogues (Q1)
bank["listening"]["task_1_short_dialogue_1"] = [
    {
        "variant": 1,
        "title": "Train Connection & Replacement Coach",
        "audioTrack": "audio/task1_v1.mp3",
        "instruction": "Listen to the conversation between a passenger and a station ticket agent. (2 plays maximum)",
        "question": {
            "id": "l_q1", "num": 1, "type": "mc",
            "stem": "1. Which travel option does the passenger decide to take?",
            "options": [
                {"val": "A", "label": "[A] The replacement express coach leaving from Bay 4"},
                {"val": "B", "label": "[B] A train service operating via another route"},
                {"val": "C", "label": "[C] A later direct express train arriving at seven o'clock"}
            ],
            "key": "B",
            "skill": "Evaluating Travel Trade-offs (B2)",
            "trap": "[A] leaves sooner but rejected due to motorway traffic; [C] seven o'clock is coach arrival time."
        }
    },
    {
        "variant": 2,
        "title": "Audio Hardware Warranty Return",
        "audioTrack": "audio/task1_v2.mp3",
        "instruction": "Listen to the conversation between a customer and an audio store representative. (2 plays maximum)",
        "question": {
            "id": "l_q1", "num": 1, "type": "mc",
            "stem": "1. Why does the customer request a replacement rather than a refund?",
            "options": [
                {"val": "A", "label": "[A] His 30-day warranty coverage is close to expiring."},
                {"val": "B", "label": "[B] He wishes to avoid the diagnostic testing delay."},
                {"val": "C", "label": "[C] The store refuses to credit his account for opened hardware."}
            ],
            "key": "B",
            "skill": "Identifying Underlying Motivation (B2)",
            "trap": "[A] time limit mentioned but not the deciding factor; [C] store credit was offered immediately."
        }
    },
    {
        "variant": 3,
        "title": "Urgent Freight Depot Redirection",
        "audioTrack": "audio/task1_v3.mp3",
        "instruction": "Listen to the conversation between an office manager and a freight logistics dispatcher. (2 plays maximum)",
        "question": {
            "id": "l_q1", "num": 1, "type": "mc",
            "stem": "1. What arrangement do they agree on to ensure the display stands arrive in time?",
            "options": [
                {"val": "A", "label": "[A] Waiting for the scheduled Friday afternoon delivery shuttle"},
                {"val": "B", "label": "[B] Collecting the shipment directly from a regional depot on Thursday"},
                {"val": "C", "label": "[C] Paying an extra courier fee for expedited direct delivery"}
            ],
            "key": "B",
            "skill": "Listening for Transactional Resolution (B1-B2)",
            "trap": "[A] Friday afternoon misses the setup cutoff; [C] fee is not mentioned."
        }
    },
    {
        "variant": 4,
        "title": "Bespoke Office Furniture Modification",
        "audioTrack": "audio/task1_v4.mp3",
        "instruction": "Listen to the conversation between a facilities coordinator and a furniture manufacturer rep. (2 plays maximum)",
        "question": {
            "id": "l_q1", "num": 1, "type": "mc",
            "stem": "1. Why does the customer need to modify the furniture order?",
            "options": [
                {"val": "A", "label": "[A] The rectangular tables would block a designated emergency exit."},
                {"val": "B", "label": "[B] The joinery workshop reported a shortage of rectangular birch timber."},
                {"val": "C", "label": "[C] She wants to take advantage of a newly announced discount on circular tables."}
            ],
            "key": "A",
            "skill": "Understanding Operational Constraints (B2)",
            "trap": "[B] joinery workshop hadn't cut yet; [C] discount was an unexpected bonus, not the motive."
        }
    },
    {
        "variant": 5,
        "title": "Corporate Conference Room Hire Waiver",
        "audioTrack": "audio/task1_v5.mp3",
        "instruction": "Listen to the conversation between an event organizer and a hotel events coordinator. (2 plays maximum)",
        "question": {
            "id": "l_q1", "num": 1, "type": "mc",
            "stem": "1. How does the organizer qualify for the room hire fee waiver?",
            "options": [
                {"val": "A", "label": "[A] By booking their event on an off-peak weekday afternoon"},
                {"val": "B", "label": "[B] By purchasing the hotel's delegate lunch package"},
                {"val": "C", "label": "[C] By providing their own audiovisual projection equipment"}
            ],
            "key": "B",
            "skill": "Filtering Contingent Pricing Terms (B1-B2)",
            "trap": "[A] weekday timing not mentioned; [C] AV is included with the suite, not external."
        }
    }
]

# Task 2: 5 Short Collaborative Workplace Dialogues (Q2)
bank["listening"]["task_2_short_dialogue_2"] = [
    {
        "variant": 1,
        "title": "Software Deployment Crunch & Data Sync",
        "audioTrack": "audio/task2_v1.mp3",
        "instruction": "Listen to the discussion between two project leads. (2 plays maximum)",
        "question": {
            "id": "l_q2", "num": 2, "type": "mc",
            "stem": "2. What do the project leads agree to do regarding the delayed data module?",
            "options": [
                {"val": "A", "label": "[A] Postpone the public release date until all testing passes"},
                {"val": "B", "label": "[B] Hire temporary staff to assist with the manual workload"},
                {"val": "C", "label": "[C] Request an emergency budget extension from corporate executives"}
            ],
            "key": "B",
            "skill": "Listening for Mutual Consensus (B2)",
            "trap": "[A] rejected because budget authority would expire; [C] budget authorization was the constraint."
        }
    },
    {
        "variant": 2,
        "title": "Store Shift Coverage & Overtime Management",
        "audioTrack": "audio/task2_v2.mp3",
        "instruction": "Listen to the discussion between two retail supervisors. (2 plays maximum)",
        "question": {
            "id": "l_q2", "num": 2, "type": "mc",
            "stem": "2. How do the supervisors decide to cover the weekend inventory audit?",
            "options": [
                {"val": "A", "label": "[A] By authorizing mandatory overtime for weekday retail employees"},
                {"val": "B", "label": "[B] By exchanging shifts with weekday staff who will take time off later"},
                {"val": "C", "label": "[C] By postponing the audit until seasonal flu absences decline"}
            ],
            "key": "B",
            "skill": "Identifying Collaborative Solutions (B2)",
            "trap": "[A] rejected to avoid payroll penalties; [C] audit date cannot be moved."
        }
    },
    {
        "variant": 3,
        "title": "Marketing Budget & Industry Newsletter Pivot",
        "audioTrack": "audio/task2_v3.mp3",
        "instruction": "Listen to the discussion between two marketing specialists. (2 plays maximum)",
        "question": {
            "id": "l_q2", "num": 2, "type": "mc",
            "stem": "2. What is the colleagues' shared conclusion regarding digital display advertising?",
            "options": [
                {"val": "A", "label": "[A] It fails to produce meaningful sales conversions despite high impressions."},
                {"val": "B", "label": "[B] It is more cost-effective than developing specialized technical newsletters."},
                {"val": "C", "label": "[C] It should be expanded across additional online search networks."}
            ],
            "key": "A",
            "skill": "Extracting Shared Conclusions (B2)",
            "trap": "[B] the newsletter converts better; [C] ad spend is being reallocated away."
        }
    },
    {
        "variant": 4,
        "title": "Office Reusable Mug Scheme & Hygiene Protocols",
        "audioTrack": "audio/task2_v4.mp3",
        "instruction": "Listen to the discussion between an office manager and a facilities coordinator. (2 plays maximum)",
        "question": {
            "id": "l_q2", "num": 2, "type": "mc",
            "stem": "2. Why does the facilities coordinator ultimately endorse the reusable mug initiative?",
            "options": [
                {"val": "A", "label": "[A] Staff will be individually responsible for handwashing their own mugs."},
                {"val": "B", "label": "[B] Commercial dishwashers and frequent bin collections resolve hygiene worries."},
                {"val": "C", "label": "[C] The £2 deposit fee will directly fund building maintenance repairs."}
            ],
            "key": "B",
            "skill": "Analyzing Concession & Resolution (B2)",
            "trap": "[A] catering apprentices clear bins and use dishwashers; [C] deposit is refundable."
        }
    },
    {
        "variant": 5,
        "title": "Software Licensing Terms & Headcount Flexibility",
        "audioTrack": "audio/task2_v5.mp3",
        "instruction": "Listen to the discussion between a procurement officer and an IT director. (2 plays maximum)",
        "question": {
            "id": "l_q2", "num": 2, "type": "mc",
            "stem": "2. Why do they decline the vendor's multi-year discounted contract?",
            "options": [
                {"val": "A", "label": "[A] Projected departmental restructuring could leave them paying for unused licenses."},
                {"val": "B", "label": "[B] The software application lacks compatibility with automated ticketing tools."},
                {"val": "C", "label": "[C] The vendor demanded immediate payment for eighty seats upfront."}
            ],
            "key": "A",
            "skill": "Evaluating Strategic Business Decisions (B2-C1)",
            "trap": "[B] automated ticketing causes headcount drop, not incompatibility; [C] payment schedule not the issue."
        }
    }
]

# Task 3: Extended Interviews (5 variants, Q3–Q7)
t3_existing = [
    next(tk for tk in TEST_1["listening"] if tk["task"] == 3),
    next(tk for tk in TEST_2["listening"] if tk["task"] == 3),
    next(tk for tk in TEST_3["listening"] if tk["task"] == 3)
]
for idx, item in enumerate(t3_existing, 1):
    item["variant"] = idx
    item["audioTrack"] = f"audio/task3_v{idx}.mp3"

t3_new = [
    {
        "variant": 4,
        "task": 3,
        "tag": "Task 3 • Extended Interview",
        "title": "Rachel Vance • Cold-Chain Logistics",
        "instruction": "You will hear an interview with Rachel Vance, operations director for a nationwide cold-chain distribution network. (2 plays maximum)",
        "audioTrack": "audio/task3_v4.mp3",
        "questions": [
            {
                "id": "l_q3", "num": 3, "type": "mc",
                "stem": "3. What first attracted Rachel to cold-chain distribution rather than standard dry warehousing?",
                "options": [
                    {"val": "A", "label": "[A] The financial incentives offered by international pharmaceutical shippers"},
                    {"val": "B", "label": "[B] The rigorous operational precision required by strict temperature tolerances"},
                    {"val": "C", "label": "[C] The ability to avoid unpredictable transit delays on regional motorways"}
                ],
                "key": "B", "skill": "Speaker Motivation (B2)", "trap": "[A] finances not stated; [C] delays happen and are critical."
            },
            {
                "id": "l_q4", "num": 4, "type": "mc",
                "stem": "4. Rachel explains that the main hurdle with electric refrigerated delivery lorries is:",
                "options": [
                    {"val": "A", "label": "[A] The heavy power drain of cooling compressors during hot weather congestion"},
                    {"val": "B", "label": "[B] The unreliability of vehicle propulsion batteries in sub-zero winter temperatures"},
                    {"val": "C", "label": "[C] The shortage of high-voltage charging points at regional customer delivery sites"}
                ],
                "key": "A", "skill": "Identifying Technical Challenges (B2-C1)", "trap": "[B] propulsion works well; [C] compressor draw during heatwaves is the stated issue."
            },
            {
                "id": "l_q5", "num": 5, "type": "mc",
                "stem": "5. How did warehouse automation at the Northampton facility affect floor workers?",
                "options": [
                    {"val": "A", "label": "[A] It forced management to reduce total employee numbers by a third."},
                    {"val": "B", "label": "[B] It enabled staff to transition from heavy manual lifting to robotics supervision."},
                    {"val": "C", "label": "[C] It caused widespread dissatisfaction due to increased hourly picking quotas."}
                ],
                "key": "B", "skill": "Factual Understanding of Workplace Change (B2)", "trap": "[A] headcount remained stable; [C] dissatisfaction not reported."
            },
            {
                "id": "l_q6", "num": 6, "type": "mc",
                "stem": "6. How does Rachel's team manage sudden spikes in supermarket grocery demand?",
                "options": [
                    {"val": "A", "label": "[A] By purchasing excess safety stock based on previous seasonal sales data"},
                    {"val": "B", "label": "[B] By combining real-time checkout telemetry with regional weather forecasts"},
                    {"val": "C", "label": "[C] By requiring retail stores to submit delivery requisitions a week in advance"}
                ],
                "key": "B", "skill": "Operational Strategy (B2-C1)", "trap": "[A] historical averages explicitly rejected; [C] real-time 24h rebalancing used."
            },
            {
                "id": "l_q7", "num": 7, "type": "mc",
                "stem": "7. What advice does Rachel impart to graduates entering the supply chain sector?",
                "options": [
                    {"val": "A", "label": "[A] Focus immediately on mastering executive data analytics software."},
                    {"val": "B", "label": "[B] Gain practical experience on loading bays and depot floors first."},
                    {"val": "C", "label": "[C] Seek management opportunities exclusively with international freight carriers."}
                ],
                "key": "B", "skill": "Concluding Advice (B2)", "trap": "[A] warns against staying behind dashboards in head office."
            }
        ]
    },
    {
        "variant": 5,
        "task": 3,
        "tag": "Task 3 • Extended Interview",
        "title": "David Cho • Sustainable Consumer Hardware",
        "instruction": "You will hear an interview with industrial designer David Cho regarding repairable domestic appliances. (2 plays maximum)",
        "audioTrack": "audio/task3_v5.mp3",
        "questions": [
            {
                "id": "l_q3", "num": 3, "type": "mc",
                "stem": "3. Why did David leave traditional consumer electronics manufacturing?",
                "options": [
                    {"val": "A", "label": "[A] Frustration with adhesive construction that forced premature product disposal"},
                    {"val": "B", "label": "[B] An inability to source sustainable bio-based plastics for appliance casings"},
                    {"val": "C", "label": "[C] Increasing competition from low-cost overseas assembly factories"}
                ],
                "key": "A", "skill": "Professional Philosophy (B2)", "trap": "[B] adhesives were the issue, not bio-plastics; [C] overseas competition not stated."
            },
            {
                "id": "l_q4", "num": 4, "type": "mc",
                "stem": "4. What was the greatest engineering hurdle in designing modular appliances?",
                "options": [
                    {"val": "A", "label": "[A] Creating standardized screw fasteners without adding excessive external bulk"},
                    {"val": "B", "label": "[B] Ensuring electrical components met international waterproof certifications"},
                    {"val": "C", "label": "[C] Reducing the total weight of the modular internal chassis"}
                ],
                "key": "A", "skill": "Engineering Analysis (B2-C1)", "trap": "[B] water ingress was a factor, but standardized modular assembly without bulk was primary."
            },
            {
                "id": "l_q5", "num": 5, "type": "mc",
                "stem": "5. What unexpected user behavior emerged after the modular appliances were launched?",
                "options": [
                    {"val": "A", "label": "[A] Owners felt empowered diagnosing faults using open-source mobile diagnostics."},
                    {"val": "B", "label": "[B] Consumers frequently damaged delicate wiring when attempting home repairs."},
                    {"val": "C", "label": "[C] Most customers still preferred taking broken appliances to professional repair shops."}
                ],
                "key": "A", "skill": "Consumer Sentiment Inferences (B2)", "trap": "[B] feared intimidation, but reality was empowering; [C] home app diagnosis was popular."
            },
            {
                "id": "l_q6", "num": 6, "type": "mc",
                "stem": "6. How does David's company supply spare parts without long shipping waits?",
                "options": [
                    {"val": "A", "label": "[A] By stocking components in decentralized regional hubs and local workshops"},
                    {"val": "B", "label": "[B] By relying on express international air freight from their central factory"},
                    {"val": "C", "label": "[C] By requiring customers to 3D-print replacement parts in their own homes"}
                ],
                "key": "A", "skill": "Supply Chain Logistics (B2)", "trap": "[B] air freight explicitly avoided; [C] CAD shared with certified workshops, not home 3D printers."
            },
            {
                "id": "l_q7", "num": 7, "type": "mc",
                "stem": "7. What does David anticipate will be the main effect of right-to-repair legislation?",
                "options": [
                    {"val": "A", "label": "[A] Manufacturers will be forced to compete on durability and ease of repair."},
                    {"val": "B", "label": "[B] Retail prices of household appliances will drop across all market tiers."},
                    {"val": "C", "label": "[C] Many smaller electronics companies will struggle to remain financially viable."}
                ],
                "key": "A", "skill": "Evaluating Policy Impact (B2-C1)", "trap": "[B] build quality improves; prices dropping not stated."
            }
        ]
    }
]
bank["listening"]["task_3_extended_interview"] = t3_existing + t3_new

# Task 4: Discussions (5 variants, Q8–Q9)
t4_existing = [
    next(tk for tk in TEST_1["listening"] if tk["task"] == 4),
    next(tk for tk in TEST_2["listening"] if tk["task"] == 4),
    next(tk for tk in TEST_3["listening"] if tk["task"] == 4)
]
for idx, item in enumerate(t4_existing, 1):
    item["variant"] = idx
    item["audioTrack"] = f"audio/task4_v{idx}.mp3"

t4_new = [
    {
        "variant": 4,
        "task": 4,
        "tag": "Task 4 • Extended Audio Discussion",
        "title": "Office Attendance Policies vs Remote Work",
        "instruction": "Listen to two colleagues discussing a corporate return-to-office policy. (2 plays maximum)",
        "audioTrack": "audio/task4_v4.mp3",
        "questions": [
            {
                "id": "l_q8", "num": 8, "type": "mc",
                "stem": "8. What is the woman's primary objection to mandatory office attendance?",
                "options": [
                    {"val": "A", "label": "[A] The financial expense of daily public transport commuting"},
                    {"val": "B", "label": "[B] The noisy open-plan environment that disrupts deep analytical tasks"},
                    {"val": "C", "label": "[C] The lack of suitable communal spaces for informal team meetings"}
                ],
                "key": "B", "skill": "Listening for Individual Perspective (B2)", "trap": "[A] transit cost not mentioned; [C] communal space is available, quiet space is lacking."
            },
            {
                "id": "l_q9", "num": 9, "type": "mc",
                "stem": "9. Both speakers agree that in-person office days are valuable for:",
                "options": [
                    {"val": "A", "label": "[A] Spontaneous problem-solving that rarely happens on scheduled calls"},
                    {"val": "B", "label": "[B] Allowing executive managers to closely supervise junior employees"},
                    {"val": "C", "label": "[C] Accelerating formal performance review processes across departments"}
                ],
                "key": "A", "skill": "Identifying Mutual Agreement (B2-C1)", "trap": "[B] managerial surveillance explicitly criticized; [C] formal reviews not discussed."
            }
        ]
    },
    {
        "variant": 5,
        "task": 4,
        "tag": "Task 4 • Extended Audio Discussion",
        "title": "Self-Checkout Automation in Supermarkets",
        "audioTrack": "audio/task4_v5.mp3",
        "instruction": "Listen to two shoppers discussing automated retail checkout systems. (2 plays maximum)",
        "audioTrack": "audio/task4_v5.mp3",
        "questions": [
            {
                "id": "l_q8", "num": 8, "type": "mc",
                "stem": "8. Why does the man find self-checkout frustrating when doing full weekly groceries?",
                "options": [
                    {"val": "A", "label": "[A] Store attendants are unavailable to assist customers with bagging."},
                    {"val": "B", "label": "[B] Barcode scanning glitches and automated weight alerts negate time savings."},
                    {"val": "C", "label": "[C] Self-service payment kiosks do not accept contactless smartphone cards."}
                ],
                "key": "B", "skill": "Analyzing Personal Critiques (B2)", "trap": "[A] attendants are present to override alerts; [C] card payment is standard."
            },
            {
                "id": "l_q9", "num": 9, "type": "mc",
                "stem": "9. What do both speakers conclude about the future of grocery retail?",
                "options": [
                    {"val": "A", "label": "[A] Supermarkets should maintain a balanced blend of self-service and staffed lanes."},
                    {"val": "B", "label": "[B] Staffed checkout counters will be completely phased out within five years."},
                    {"val": "C", "label": "[C] Retailers should charge premium prices to customers using human cashiers."}
                ],
                "key": "A", "skill": "Synthesizing Shared Outlooks (B2)", "trap": "[B] total automation warned against as damaging customer rapport."
            }
        ]
    }
]
bank["listening"]["task_4_discussion"] = t4_existing + t4_new

# Task 5: 5 Speakers Multiple Matching (5 variants, Q10–Q14)
t5_existing = [
    next(tk for tk in TEST_1["listening"] if tk["task"] == 5),
    next(tk for tk in TEST_2["listening"] if tk["task"] == 5),
    next(tk for tk in TEST_3["listening"] if tk["task"] == 5)
]
for idx, item in enumerate(t5_existing, 1):
    item["variant"] = idx
    item["audioTrack"] = f"audio/task5_v{idx}.mp3"

t5_new = [
    {
        "variant": 4,
        "task": 5,
        "tag": "Task 5 • Multiple Matching",
        "title": "Reasons for Changing Daily Commute Modes",
        "instruction": "Listen to five people explaining why they changed their daily journey to work. Match each speaker to their primary reason. (2 plays maximum)",
        "audioTrack": "audio/task5_v4.mp3",
        "questions": [
            {
                "id": "l_q10", "num": 10, "type": "mc", "stem": "10. Speaker 1 (Ryan):",
                "options": [
                    {"val": "A", "label": "[A] To establish a healthy mental buffer between work and home"},
                    {"val": "B", "label": "[B] To avoid extortionate municipal car parking charges"},
                    {"val": "C", "label": "[C] To share travel costs and enjoy morning social interaction"},
                    {"val": "D", "label": "[D] To relieve sensory anxiety triggered by overcrowded transit"},
                    {"val": "E", "label": "[E] To take advantage of quieter off-peak rail carriages with workspace"}
                ],
                "key": "A", "skill": "Identifying Personal Well-being Motivations (B2)", "trap": "E-bike exercise creates a mental boundary after work."
            },
            {
                "id": "l_q11", "num": 11, "type": "mc", "stem": "11. Speaker 2 (Natasha):",
                "options": [
                    {"val": "A", "label": "[A] To establish a healthy mental buffer between work and home"},
                    {"val": "B", "label": "[B] To avoid extortionate municipal car parking charges"},
                    {"val": "C", "label": "[C] To share travel costs and enjoy morning social interaction"},
                    {"val": "D", "label": "[D] To relieve sensory anxiety triggered by overcrowded transit"},
                    {"val": "E", "label": "[E] To take advantage of quieter off-peak rail carriages with workspace"}
                ],
                "key": "B", "skill": "Financial Decision-Making (B2)", "trap": "Park-and-ride bus saved £35/day on hospital parking."
            },
            {
                "id": "l_q12", "num": 12, "type": "mc", "stem": "12. Speaker 3 (Jenny):",
                "options": [
                    {"val": "A", "label": "[A] To establish a healthy mental buffer between work and home"},
                    {"val": "B", "label": "[B] To avoid extortionate municipal car parking charges"},
                    {"val": "C", "label": "[C] To share travel costs and enjoy morning social interaction"},
                    {"val": "D", "label": "[D] To relieve sensory anxiety triggered by overcrowded transit"},
                    {"val": "E", "label": "[E] To take advantage of quieter off-peak rail carriages with workspace"}
                ],
                "key": "C", "skill": "Social & Economic Motivation (B2)", "trap": "Carpooling cut fuel bills by two-thirds with cheerful company."
            },
            {
                "id": "l_q13", "num": 13, "type": "mc", "stem": "13. Speaker 4 (Guy):",
                "options": [
                    {"val": "A", "label": "[A] To establish a healthy mental buffer between work and home"},
                    {"val": "B", "label": "[B] To avoid extortionate municipal car parking charges"},
                    {"val": "C", "label": "[C] To share travel costs and enjoy morning social interaction"},
                    {"val": "D", "label": "[D] To relieve sensory anxiety triggered by overcrowded transit"},
                    {"val": "E", "label": "[E] To take advantage of quieter off-peak rail carriages with workspace"}
                ],
                "key": "D", "skill": "Emotional Well-being (B2)", "trap": "Walking 3.5 miles avoided claustrophobic metro carriages."
            },
            {
                "id": "l_q14", "num": 14, "type": "mc", "stem": "14. Speaker 5 (Thomas):",
                "options": [
                    {"val": "A", "label": "[A] To establish a healthy mental buffer between work and home"},
                    {"val": "B", "label": "[B] To avoid extortionate municipal car parking charges"},
                    {"val": "C", "label": "[C] To share travel costs and enjoy morning social interaction"},
                    {"val": "D", "label": "[D] To relieve sensory anxiety triggered by overcrowded transit"},
                    {"val": "E", "label": "[E] To take advantage of quieter off-peak rail carriages with workspace"}
                ],
                "key": "E", "skill": "Productivity & Schedule Flexibility (B2)", "trap": "9:15 train has tables and sockets for early work."
            }
        ]
    },
    {
        "variant": 5,
        "task": 5,
        "tag": "Task 5 • Multiple Matching",
        "title": "Reasons for Relocating from Cities to Small Towns",
        "instruction": "Listen to five people discussing why they moved away from a major city. Match each speaker to their primary reason. (2 plays maximum)",
        "audioTrack": "audio/task5_v5.mp3",
        "questions": [
            {
                "id": "l_q10", "num": 10, "type": "mc", "stem": "10. Speaker 1 (Sonia):",
                "options": [
                    {"val": "A", "label": "[A] Securing an affordable family home with outdoor garden space"},
                    {"val": "B", "label": "[B] Living close enough to assist elderly parents with everyday care"},
                    {"val": "C", "label": "[C] Having immediate access to wilderness and outdoor hiking trails"},
                    {"val": "D", "label": "[D] Leasing affordable premises to establish an independent local business"},
                    {"val": "E", "label": "[E] Eliminating an exhausting multi-hour daily transit commute"}
                ],
                "key": "A", "skill": "Housing & Family Motivation (B2)", "trap": "Detached home with garden for half the London price."
            },
            {
                "id": "l_q11", "num": 11, "type": "mc", "stem": "11. Speaker 2 (William):",
                "options": [
                    {"val": "A", "label": "[A] Securing an affordable family home with outdoor garden space"},
                    {"val": "B", "label": "[B] Living close enough to assist elderly parents with everyday care"},
                    {"val": "C", "label": "[C] Having immediate access to wilderness and outdoor hiking trails"},
                    {"val": "D", "label": "[D] Leasing affordable premises to establish an independent local business"},
                    {"val": "E", "label": "[E] Eliminating an exhausting multi-hour daily transit commute"}
                ],
                "key": "B", "skill": "Family Caregiving Motivation (B2)", "trap": "Parents entering eighties; 5 minutes away for errands."
            },
            {
                "id": "l_q12", "num": 12, "type": "mc", "stem": "12. Speaker 3 (Jenny):",
                "options": [
                    {"val": "A", "label": "[A] Securing an affordable family home with outdoor garden space"},
                    {"val": "B", "label": "[B] Living close enough to assist elderly parents with everyday care"},
                    {"val": "C", "label": "[C] Having immediate access to wilderness and outdoor hiking trails"},
                    {"val": "D", "label": "[D] Leasing affordable premises to establish an independent local business"},
                    {"val": "E", "label": "[E] Eliminating an exhausting multi-hour daily transit commute"}
                ],
                "key": "C", "skill": "Lifestyle & Environmental Preference (B2)", "trap": "Cumbria mountain trails start right outside front doorstep."
            },
            {
                "id": "l_q13", "num": 13, "type": "mc", "stem": "13. Speaker 4 (Ryan):",
                "options": [
                    {"val": "A", "label": "[A] Securing an affordable family home with outdoor garden space"},
                    {"val": "B", "label": "[B] Living close enough to assist elderly parents with everyday care"},
                    {"val": "C", "label": "[C] Having immediate access to wilderness and outdoor hiking trails"},
                    {"val": "D", "label": "[D] Leasing affordable premises to establish an independent local business"},
                    {"val": "E", "label": "[E] Eliminating an exhausting multi-hour daily transit commute"}
                ],
                "key": "D", "skill": "Entrepreneurial Opportunity (B2)", "trap": "Leased old cooperage warehouse for artisan coffee roastery."
            },
            {
                "id": "l_q14", "num": 14, "type": "mc", "stem": "14. Speaker 5 (Libby):",
                "options": [
                    {"val": "A", "label": "[A] Securing an affordable family home with outdoor garden space"},
                    {"val": "B", "label": "[B] Living close enough to assist elderly parents with everyday care"},
                    {"val": "C", "label": "[C] Having immediate access to wilderness and outdoor hiking trails"},
                    {"val": "D", "label": "[D] Leasing affordable premises to establish an independent local business"},
                    {"val": "E", "label": "[E] Eliminating an exhausting multi-hour daily transit commute"}
                ],
                "key": "E", "skill": "Work-Life Quality (B2)", "trap": "Saved 15 hours a week by eliminating grueling 3-hour transit."
            }
        ]
    }
]
bank["listening"]["task_5_multiple_matching"] = t5_existing + t5_new

# Task 6: Monologue Sentence Completion (5 variants, Q15–Q19)
t6_existing = [
    next(tk for tk in TEST_1["listening"] if tk["task"] == 6),
    next(tk for tk in TEST_2["listening"] if tk["task"] == 6),
    next(tk for tk in TEST_3["listening"] if tk["task"] == 6)
]
for idx, item in enumerate(t6_existing, 1):
    item["variant"] = idx
    item["audioTrack"] = f"audio/task6_v{idx}.mp3"

t6_new = [
    {
        "variant": 4,
        "task": 6,
        "tag": "Task 6 • Sentence Completion",
        "title": "Airport Automated Baggage Handling Systems",
        "instruction": "Listen to the briefing on airport automated baggage logistics. Complete each sentence with a word or short phrase from the recording. (2 plays maximum)",
        "audioTrack": "audio/task6_v4.mp3",
        "questions": [
            {
                "id": "l_q15", "num": 15, "type": "text",
                "stem": "15. Modern luggage tags embed high-frequency [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] microchips to ensure accurate automated tracking.",
                "key": "RFID", "skill": "Technical Term Extraction (B2)", "trap": "Audio: 'RFID microchips embedded alongside traditional barcodes'."
            },
            {
                "id": "l_q16", "num": 16, "type": "text",
                "stem": "16. Automated conveyor networks direct bags through 3D [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] scanners for non-intrusive security inspection.",
                "key": "computed tomography", "skill": "Noun Phrase Recognition (B2-C1)", "trap": "Audio: 'three-dimensional computed tomography scanners'."
            },
            {
                "id": "l_q17", "num": 17, "type": "text",
                "stem": "17. During flight delays, luggage is stored within high-density [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] facilities instead of open tarmac carts.",
                "key": "racking", "skill": "Industrial Facility Term (B2)", "trap": "Audio: 'dynamic high-density racking facilities'."
            },
            {
                "id": "l_q18", "num": 18, "type": "text",
                "stem": "18. Apron electric tug vehicles utilize [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] sensors to calculate the most efficient transit path to the aircraft.",
                "key": "telematics", "skill": "Operational Lexis (B2-C1)", "trap": "Audio: 'equipped with telematics sensors that optimize baggage transit'."
            },
            {
                "id": "l_q19", "num": 19, "type": "text",
                "stem": "19. The overarching metric of ground handling efficiency is reducing aircraft [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] time at airport gates.",
                "key": "turnaround", "skill": "Commercial Metric (B2)", "trap": "Audio: 'commercial benchmark of ground logistics efficiency is aircraft turnaround time'."
            }
        ]
    },
    {
        "variant": 5,
        "task": 6,
        "tag": "Task 6 • Sentence Completion",
        "title": "Municipal Wastewater Recycling Infrastructure",
        "instruction": "Listen to the presentation on municipal wastewater recycling systems. Complete each sentence with a word or short phrase from the recording. (2 plays maximum)",
        "audioTrack": "audio/task6_v5.mp3",
        "questions": [
            {
                "id": "l_q15", "num": 15, "type": "text",
                "stem": "15. Incoming wastewater first flows across rotary [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] screens to extract coarse debris and plastics.",
                "key": "mesh", "skill": "Filtration Equipment (B2)", "trap": "Audio: 'rotary mesh screens to eliminate insoluble plastics'."
            },
            {
                "id": "l_q16", "num": 16, "type": "text",
                "stem": "16. Microbial breakdown of organic compounds takes place inside membrane [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] tanks.",
                "key": "bioreactor", "skill": "Scientific Compound Word (B2)", "trap": "Audio: 'membrane bioreactor chambers, where dense colonies of aerobic microbes'."
            },
            {
                "id": "l_q17", "num": 17, "type": "text",
                "stem": "17. During reverse osmosis, dissolved salts are extracted by forcing effluent across [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] membranes.",
                "key": "polyamide", "skill": "Materials Vocabulary (C1)", "trap": "Audio: 'through dense polyamide membranes during reverse osmosis'."
            },
            {
                "id": "l_q18", "num": 18, "type": "text",
                "stem": "18. The secondary disinfection stage combines ultraviolet light with hydrogen [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] to destroy lingering impurities.",
                "key": "peroxide", "skill": "Chemical Collocation (B2)", "trap": "Audio: 'ultraviolet irradiation combined with hydrogen peroxide'."
            },
            {
                "id": "l_q19", "num": 19, "type": "text",
                "stem": "19. The resulting high-grade recycled water is largely supplied to industrial power station [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] towers.",
                "key": "cooling", "skill": "Industrial Facility Term (B1-B2)", "trap": "Audio: 'heavy power station cooling towers, preserving millions of litres'."
            }
        ]
    }
]
bank["listening"]["task_6_monologue_gaps"] = t6_existing + t6_new


# ==============================================================================
# WRITING TASKS (5 PROMPTS PER TASK)
# ==============================================================================

bank["writing"]["task_1_narrative"] = [
    TEST_1["writing"][0],
    TEST_2["writing"][0],
    TEST_3["writing"][0],
    {
        "id": "w_t1_v4",
        "task": 1,
        "title": "Part 1 • Narrative Dispatch (Workplace Reorganization)",
        "prompt": "You recently supervised a complex weekend office relocation or systems upgrade that encountered unexpected complications. Write a formal dispatch report (150–180 words) to your department director detailing the unforeseen logistical challenge, how your team improvised to overcome it, and your recommendations to prevent similar occurrences in future operational transitions."
    },
    {
        "id": "w_t1_v5",
        "task": 1,
        "title": "Part 1 • Narrative Letter (Travel Delay & Hospitality)",
        "prompt": "While traveling on business, severe weather caused your flight to be diverted to an unfamiliar regional city overnight. Write a personal letter (150–180 words) to a friend recounting the initial travel frustration, the unexpected warmth or helpfulness of a local resident or hotel worker, and how the detour gave you a fresh perspective on the region."
    }
]

bank["writing"]["task_2_discursive"] = [
    TEST_1["writing"][1],
    TEST_2["writing"][1],
    TEST_3["writing"][1],
    {
        "id": "w_t2_v4",
        "task": 2,
        "title": "Part 2 • Discursive Article (Cashless Commerce & Digital Equity)",
        "prompt": "Many modern businesses and transit networks are transitioning to entirely cashless payments. Write a critical feature article (220–260 words) evaluating whether the convenience and accounting efficiency of a cashless society outweigh the risks of financial exclusion for vulnerable demographics and dependence on digital banking infrastructure."
    },
    {
        "id": "w_t2_v5",
        "task": 2,
        "title": "Part 2 • Feature Essay (The 15-Minute City & Urban Mobility)",
        "prompt": "Urban planners are increasingly advocating for '15-minute cities,' where residents can access all essential amenities—work, retail, healthcare, and education—within a short walk or bicycle ride. Write an evaluative essay (220–260 words) examining the benefits for environmental sustainability and civic community versus the practical challenges of retrofitting existing suburban sprawl."
    }
]

out_file = DATA_DIR / "bank.json"
out_file.write_text(json.dumps(bank, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Successfully generated {out_file} ({out_file.stat().st_size} bytes)")
