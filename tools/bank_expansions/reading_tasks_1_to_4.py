# Reading tasks 1-4 expansion (20 items for task 1, 20 for task 2, 20 for task 3, 20 for task 4)

TASK_1_EXPANSIONS = [
    {
        "task": 1,
        "tag": "Task 1 • Notices & Messages",
        "title": title,
        "instruction": "Read the notice and answer the question.",
        "passage": passage,
        "questions": [
            {
                "id": "r_q1",
                "num": 1,
                "type": "mc",
                "stem": "1. What does this notice tell readers?",
                "options": [
                    {"val": "A", "label": f"[A] {opt_a}"},
                    {"val": "B", "label": f"[B] {opt_b}"},
                    {"val": "C", "label": f"[C] {opt_c}"}
                ],
                "key": key,
                "skill": "Gist & Factual Extraction (A2-B1)",
                "trap": trap
            }
        ]
    }
    for title, passage, opt_a, opt_b, opt_c, key, trap in [
        ("Bicycle Shelter Regulations", "<strong>COMMUTER BIKE STATION</strong><br><em>All bicycles stored in the shelter must be registered with station security. Unregistered bicycles remaining in bays after 22:00 on Fridays will be impounded. Overnight parking is permitted only in designated bays on Level 2 with a valid electronic commuter permit.</em>", "Bicycles left on weekends must have proper registration and permits.", "Any bicycle parked overnight will be permanently confiscated.", "Registration is optional for cyclists parking on Level 2.", "A", "[B] is too extreme; [C] registration is mandatory for all."),
        ("Swimming Gala Closure Notice", "<strong>COUNTY AQUATICS COMPLEX</strong><br><em>Due to the Regional Masters Swimming Gala, the 50m competition pool will be reserved for competitive heats from 08:00 to 16:00 this Saturday. The 25m recreational training pool and sauna suite remain open to public season pass holders throughout the day.</em>", "The entire aquatics complex is closed to the public on Saturday.", "Public lane swimming is available in the 25m pool on Saturday.", "The swimming gala concludes on Sunday afternoon.", "B", "[A] recreational pool is open; [C] gala is Saturday only."),
        ("Allotment Water Restrictions", "<strong>RIVERSIDE ALLOTMENT ASSOCIATION</strong><br><em>In compliance with municipal hosepipe bans during current dry conditions, watering with automatic sprinkler systems is strictly prohibited until further notice. Plot holders may use handheld watering cans filled from rainwater collection barrels located beside Shed 4.</em>", "Sprinkler irrigation is permitted during early morning hours.", "Plot holders must bring tap water from their own homes.", "Gardeners may only water crops using cans from rainwater barrels.", "C", "[A] sprinklers prohibited; [B] rainwater barrels provided on site."),
        ("Print Exhibition Extension", "<strong>CONTEMPORARY PRINT WORKSHOP</strong><br><em>Owing to exceptional visitor interest, the retrospective woodcut exhibition by artist Mei Lin has been extended through 15 November. Advance timed-entry ticket reservation is recommended for weekend visits, though weekday entry remains available at reception without booking.</em>", "Visitors must book tickets online for all exhibition dates.", "Mei Lin's exhibition has been prolonged beyond its original dates.", "The gallery will be closed to visitors during weekday afternoons.", "B", "[A] weekday walk-in available; [C] weekdays remain open."),
        ("Chemistry Lab Safety Memo", "<strong>SYNTHESIS LAB B-4 SAFETY ADVISORY</strong><br><em>All postgraduate researchers handling volatile organic solvents must verify that fume extraction hoods are switched on prior to beginning synthesis. Protective nitrile gloves and splash goggles must be worn at all times in this zone. Food and beverage containers are strictly forbidden.</em>", "Solvents may be handled outside fume hoods if goggles are worn.", "Eating and drinking are strictly banned inside the synthesis laboratory.", "Goggles are required only when manipulating heating mantles.", "B", "[A] fume hood mandatory; [C] goggles required at all times."),
        ("Metro Track Engineering Notice", "<strong>METROPOLITAN TRANSIT ADVISORY</strong><br><em>Line 3 trains will terminate at West Park station from Monday through Wednesday to allow scheduled rail replacement. Free shuttle buses will operate every six minutes between West Park and Central Square. Passengers connecting to the airport line should allow twenty additional minutes.</em>", "Line 3 trains will run direct to Central Square without stops.", "Replacement shuttle buses require an additional cash fare.", "Passengers heading toward the airport should anticipate longer journeys.", "C", "[A] trains terminate at West Park; [B] shuttle buses are free."),
        ("Medieval Vault Photography Rules", "<strong>MEDIEVAL ARMS & ARMOR VAULT</strong><br><em>Flash photography is strictly prohibited inside the vaulted armory gallery, as intense light frequencies cause photo-degradation to antique textile linings. Monopods and mobile phone filming without flash are permitted provided visitors do not obstruct walkways.</em>", "Visitors are allowed to film using mobile phones if flash is deactivated.", "All photography and videography are entirely prohibited in the vault.", "Flash photography is permitted on weekdays with museum staff approval.", "A", "[B] filming without flash permitted; [C] flash strictly prohibited."),
        ("Apartment Cardboard Disposal", "<strong>RIVERVIEW APARTMENTS WASTE RECYCLING</strong><br><em>Cardboard boxes placed in the communal basement recycling depot must be flattened before disposal in the blue recycling skips. Whole boxes left on the depot floor will not be collected by municipal refuse teams and may incur communal penalty charges.</em>", "Residents should flatten cardboard before placing it into blue skips.", "Cardboard boxes may be left intact on the depot concrete floor.", "Refuse teams collect unflattened boxes every Tuesday morning.", "A", "[B] prohibited; [C] unflattened boxes will not be collected."),
        ("Examination Hall ID Requirement", "<strong>EXAMINATION HALL RULES: NORTH AUDITORIUM</strong><br><em>Candidates must present physical student identification cards at the entry turnstile. Digital identity credentials on smartphone screens cannot be accepted by invigilators. All wristwatches, smart devices, and opaque pencil cases must be deposited in the cloakroom.</em>", "Students may display digital identity cards on their mobile phones.", "Only physical identity cards are accepted for examination room admission.", "Wristwatches of any style are permitted on candidates' desks.", "B", "[A] digital cards rejected; [C] wristwatches must be deposited."),
        ("Public Library Census Terminals", "<strong>COUNTY REFERENCE LIBRARY</strong><br><em>Access to digitized local census records from 1841 to 1911 is complimentary for all library cardholders on terminals in Room 3. Print copies of archival certificates may be ordered from the reference desk for a nominal fee of two pounds per facsimile sheet.</em>", "Archival census digital browsing is free of charge for cardholders.", "Searching digital census records requires a two-pound hourly fee.", "Printed certificates are provided without charge upon request.", "A", "[B] searching is complimentary; [C] prints cost two pounds."),
        ("Winter Glasshouse Operating Hours", "<strong>BOTANICAL WINTER GLASS-HOUSE</strong><br><em>From 1 November, the tropical conservatory will observe winter operating hours, opening at 10:00 and closing at 16:00 daily. The exterior rose gardens and arboretum remain open during daylight hours from sunrise to dusk without charge.</em>", "The tropical conservatory remains accessible until sunset in winter.", "Public access to the outdoor rose gardens remains free throughout winter.", "Guided tours through the glass-house continue daily at 10:00.", "B", "[A] closes at 16:00; [C] outdoor gardens free."),
        ("Baggage Reclaim Conveyor Advisory", "<strong>BAGGAGE RECLAIM CAROUSEL 4</strong><br><em>Oversized luggage, including skis, golf bags, and musical instruments, will not appear on this conveyor belt. Passengers holding claim tags for oversized items should proceed directly to Gate B Baggage Service Counter located beside customs exit.</em>", "Oversized bags should be collected from the separate service counter.", "Ski bags and instruments will emerge on Carousel 4 after suitcases.", "Passengers must pay an oversized luggage clearance fee at customs.", "A", "[B] will not appear on carousel; [C] fee not mentioned."),
        ("Gymnasium Locker Overstay Policy", "<strong>FITNESS CLUB LOCKER MAINTENANCE</strong><br><em>Lockers are intended solely for temporary day use while members are exercising. Any locker remaining locked after 22:30 closing time will be opened by facility staff and contents placed in lost property. Personal padlocks will be clipped and not replaced by club management.</em>", "Members may rent lockers overnight by purchasing a club padlock.", "Lockers left locked after closing will be forcibly opened by staff.", "Club management will compensate members for clipped padlocks.", "B", "[A] overnight storage banned; [C] padlocks will not be replaced."),
        ("Civic Center Event Parking Policy", "<strong>MUNICIPAL CIVIC CENTER</strong><br><em>Underground visitor parking bays are reserved exclusively for attendees of the Regional Environmental Summit on Thursday morning. Regular public library and clinic visitors should use the multi-storey facility on St. Peter's Street, where standard hourly tariffs apply.</em>", "Civic center underground parking is reserved for summit delegates on Thursday.", "Environmental summit attendees must park on St. Peter's Street.", "Free parking on St. Peter's Street is available for all library users.", "A", "[B] summit delegates park underground; [C] standard tariffs apply."),
        ("Nature Reserve Boardwalk Closure", "<strong>MARSHLAND BIRD SANCTUARY</strong><br><em>Due to seasonal nesting of marsh harriers along the reed beds, the boardwalk trail between Observation Hides 2 and 4 is closed until mid-July. Visitors are asked to remain strictly on the western perimeter path and keep all domestic dogs on short leads.</em>", "Dogs are permitted off-lead on the western perimeter path.", "The boardwalk between Hides 2 and 4 is accessible to quiet visitors.", "Nesting season has caused a temporary closure of part of the trail.", "C", "[A] dogs on short leads; [B] boardwalk closed."),
        ("Choir Rehearsal Hall Relocation", "<strong>ST. CLEMENT CHORAL SOCIETY</strong><br><em>Rehearsals on Tuesday evenings will temporarily move from the church crypt to the high school music auditorium while heating pipes are replaced. Choir members should enter through the side stage door on High Street rather than the main school reception.</em>", "Tuesday rehearsals will take place in the high school for the time being.", "Choir members should assemble outside the main school reception.", "Rehearsals have been cancelled while church heating is repaired.", "A", "[B] enter side stage door; [C] venue changed, not cancelled."),
        ("Book Exchange Buyback Terms", "<strong>CAMPUS BOOK EXCHANGE</strong><br><em>The student bookshop is purchasing used academic textbooks for semester 2 courses until Friday afternoon. Textbooks must have clean binding with no missing pages or heavy highlighting. Store credit vouchers receive a ten percent bonus over cash payouts.</em>", "Students receive higher value if they accept store credit instead of cash.", "Any textbook will be accepted regardless of physical condition.", "The buyback scheme operates throughout the entire semester.", "A", "[B] clean binding required; [C] ends Friday afternoon."),
        ("Hospital Ward Visiting Regulations", "<strong>ST. JUDE'S HOSPITAL: WARD 4A</strong><br><em>Visiting hours are strictly between 14:00 and 19:00 daily. To prevent patient fatigue, a maximum of two visitors are permitted at the bedside at any one time. Children under twelve years of age are not permitted into post-surgical units without nursing approval.</em>", "Up to four family members may visit a patient simultaneously.", "Young children require special approval to enter post-surgical units.", "Visitors are welcome at any hour provided they remain quiet.", "B", "[A] maximum two visitors; [C] hours 14:00 to 19:00."),
        ("Station Elevator Maintenance", "<strong>CENTRAL METRO: PLATFORM 3</strong><br><em>The passenger elevator serving Platform 3 is out of service for mechanical repairs until Thursday noon. Passengers requiring step-free access to northbound commuter services should speak to station staff at the main gate to arrange accessible road transfer.</em>", "Northbound commuter trains will not stop at Central Metro.", "The Platform 3 elevator will be repaired by Wednesday evening.", "Staff can arrange alternative transport for passengers needing step-free access.", "C", "[A] trains stop; [B] out of service until Thursday noon."),
        ("Tower Fire Evacuation Exercise", "<strong>OAKRIDGE TOWER MANAGEMENT</strong><br><em>A mandatory building-wide evacuation drill will take place on Wednesday at 10:30. When alarms sound, all occupants must exit via designated emergency stairwells; elevators will be grounded at the lobby. Assemble in Car Park C until wardens give the all-clear.</em>", "Office workers should take elevators down to the ground floor.", "Occupants must evacuate via stairwells when the drill begins.", "The emergency evacuation drill is voluntary for senior staff.", "B", "[A] elevators grounded; [C] mandatory for all occupants.")
    ]
]

TASK_2_EXPANSIONS = [
    {
        "task": 2,
        "tag": "Task 2 • Sentence Gap-Fill",
        "title": title,
        "instruction": "Choose the correct word to complete the sentence.",
        "questions": [
            {
                "id": "r_q2",
                "num": 2,
                "type": "mc",
                "stem": f"2. {stem}",
                "options": [
                    {"val": "A", "label": f"[A] {opt_a}"},
                    {"val": "B", "label": f"[B] {opt_b}"},
                    {"val": "C", "label": f"[C] {opt_c}"},
                    {"val": "D", "label": f"[D] {opt_d}"}
                ],
                "key": key,
                "skill": skill,
                "trap": trap
            }
        ]
    }
    for title, stem, opt_a, opt_b, opt_c, opt_d, key, skill, trap in [
        ("Laboratory Safety Protocol", "Researchers must strictly [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] to the chemical handling guidelines established by the biosafety panel.", "adhere", "comply", "conform", "agree", "A", "Dependent Preposition (B2)", "'Adhere' takes 'to'; 'comply' takes 'with'."),
        ("Aviation Fuel Efficiency", "The airline's newly introduced jet engines [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] fuel consumption by nearly fifteen percent on long-haul routes.", "curtailed", "curbed", "reduced", "dropped", "C", "Transitive Verb Selection (B1-B2)", "'Reduced' is the standard commercial/engineering collocate here."),
        ("Architectural Planning Approval", "The planning board granted conditional approval on the [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] that the developer preserves the facade of the Victorian warehouse.", "provision", "condition", "stipulation", "agreement", "B", "Idiomatic Prepositional Phrase (B2)", "The standard set phrase is 'on the condition that'."),
        ("Commercial Real Estate Leases", "Commercial tenants are legally required to give three months' [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] before vacating retail premises.", "warning", "attention", "notice", "alert", "C", "Fixed Commercial Lexis (B1-B2)", "Collocation: give three months' 'notice'."),
        ("Public Transit Fare Integration", "The unified transit pass allows commuters to switch between trains and ferries without paying an [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] tariff.", "excess", "additional", "added", "extraordinary", "B", "Adjective Collocation (B1-B2)", "'Additional' collocates formally with tariff/fee."),
        ("Agricultural Frost Precautions", "Fruit farmers deployed warm air blowers across orchards in an effort to [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] frost damage to early blossoming cherry trees.", "avert", "evade", "dodge", "refuse", "A", "Formal Lexical Selection (B2)", "One 'averts' damage or disaster; evade is physical/avoidance."),
        ("University Scholarship Eligibility", "Undergraduate candidates who [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] both academic criteria will be invited for an interview with the awards committee.", "fulfil", "reach", "achieve", "obtain", "A", "Verb-Noun Collocation (B2)", "One 'fulfils' criteria or requirements."),
        ("Archaeological Site Conservation", "Persistent rainfall has caused the ancient limestone masonry to gradually [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] over the past century.", "decay", "erode", "collapse", "decline", "B", "Geological/Preservation Lexis (B2)", "Stone 'erodes' from moisture/weathering."),
        ("Urban Noise Ordinance", "Municipal bylaws [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] loud construction activities between 20:00 and 07:00 in residential areas.", "ban", "prohibit", "reject", "suppress", "B", "Formal Legal Lexis (B2)", "Laws formally 'prohibit' activities."),
        ("Museum Artifact Provenance", "Curators carried out extensive archival checks to [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] the authentic provenance of the 16th-century silver chalice.", "ascertain", "assure", "insure", "secure", "A", "Formal Inquiry Verb (B2-C1)", "'Ascertain' means to find out or verify with certainty."),
        ("Marine Environmental Monitoring", "Scientists observed that warming coastal currents have [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] the seasonal migration patterns of native Atlantic salmon.", "altered", "swapped", "converted", "reformed", "A", "Natural Science Collocation (B2)", "Currents 'alter' migration patterns."),
        ("Pharmaceutical Cold Chain", "Temperature-sensitive vaccines must be maintained within a [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] thermal range during transit.", "narrow", "tight", "slight", "lean", "A", "Technical Collocation (B2)", "Scientific/technical contexts use 'a narrow range'."),
        ("Corporate Governance Standards", "The board of directors agreed to [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] an independent review into workplace safety procedures.", "commission", "charge", "employ", "command", "A", "Corporate Register Collocation (B2)", "Boards 'commission' an independent review."),
        ("Renewable Energy Transmission", "Constructing offshore wind farms requires heavy capital investment in submarine cables to [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] electrical power to the national grid.", "conduct", "transmit", "convey", "dispatch", "B", "Technical Lexical Selection (B2)", "Electrical energy is 'transmitted' to a grid."),
        ("Historical Document Authentication", "Paleographers examined the watermark in the handmade paper to [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] the manuscript to the mid-fourteenth century.", "date", "period", "chronicle", "time", "A", "Scholarly Collocation (B2-C1)", "Experts 'date' an artifact to a time period."),
        ("Civic Infrastructure Renewal", "Urban transit authorities decided to [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] priority to light rail extensions over highway widening projects.", "give", "accord", "assign", "grant", "A", "Collocation (B1-B2)", "Idiomatic: 'give priority to' (or 'accord', but give is standard)."),
        ("Wildfire Prevention Measures", "Forestry rangers cleared dry undergrowth along forest fringes to create firebreaks that [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] the spread of blazes.", "impede", "hinder", "deter", "delay", "A", "Physical Obstruction Lexis (B2)", "Firebreaks 'impede' the spread of fires."),
        ("Hospital Surgical Hygiene", "Stringent sterilization routines are enforced to minimize the [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] of postoperative bacterial infections.", "incidence", "occurrence", "event", "happening", "A", "Medical Statistics Register (B2)", "'Incidence' collocates with diseases and infections."),
        ("Library Special Collections", "Rare illuminated manuscripts are housed in vault cabinets that maintain an [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] relative humidity of fifty percent.", "optimum", "extreme", "idealistic", "exquisite", "A", "Scientific Storage Lexis (B2)", "'Optimum' relative humidity."),
        ("Autonomous Navigational Sensors", "The driverless vehicle's infrared sensors can [ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ] small obstacles in dense fog up to two hundred meters ahead.", "detect", "discern", "distinguish", "perceive", "A", "Technical Instrumentation Lexis (B1-B2)", "Sensors 'detect' obstacles.")
    ]
]

TASK_3_EXPANSIONS = [
    {
        "task": 3,
        "tag": "Task 3 • Open Gap-Fill",
        "title": title,
        "instruction": "Read the text below and think of the word which best fits each gap. Use only ONE word in each gap.",
        "passage": passage,
        "questions": [
            {
                "id": f"r_q{num}",
                "num": num,
                "type": "text",
                "stem": f"Gap {num}",
                "key": key,
                "skill": skill,
                "trap": trap,
                "variants": variants
            }
            for num, key, skill, trap, variants in q_specs
        ]
    }
    for title, passage, q_specs in [
        (
            "The Revival of Dark Sky Reserves",
            "<p>In our hyper-electrified modern world, true nocturnal darkness has become an endangered commodity. Over eighty percent of the global population now lives <strong>(3)</strong> _________ skies heavily polluted by artificial illumination. In response, astronomers and conservationists have banded together to establish international Dark Sky Reserves, remote geographical zones <strong>(4)</strong> _________ outdoor lighting is strictly managed.</p><p>By shielding streetlights and directing beams downward rather <strong>(5)</strong> _________ letting light spill skyward, these sanctuaries preserve the pristine majesty of the Milky Way. Biologists emphasize that artificial skyglow disrupts the migration routes of nocturnal birds <strong>(6)</strong> _________ well as the pollination cycles of night-blooming flowers. Protecting the night sky is therefore not merely an aesthetic luxury, <strong>(7)</strong> _________ a critical ecological imperative.</p>",
            [
                (3, "under", "Preposition of Place (B1)", "Living 'under' polluted skies.", ["under"]),
                (4, "where", "Relative Adverb (B1-B2)", "Geographical zones 'where' lighting is managed.", ["where"]),
                (5, "than", "Comparative Connector (B1)", "Rather 'than' letting light spill.", ["than"]),
                (6, "as", "Correlative Conjunction (B1)", "'as well as' nocturnal birds.", ["as"]),
                (7, "but", "Contrastive Conjunction (B1-B2)", "Not merely X, 'but' Y.", ["but"])
            ]
        ),
        (
            "The Ancient Craft of Dry-Stone Walling",
            "<p>Across the windswept uplands of northern Britain, dry-stone walls have divided pastures <strong>(3)</strong> _________ centuries. What makes these rugged barriers remarkable is that they are constructed entirely <strong>(4)</strong> _________ the use of mortar or cement. Experienced wallers select and interlock native stones so skillfully that gravity and friction hold the structure together against fierce Atlantic gales.</p><p>Each wall incorporates two outer faces leaning slightly inward, with smaller rubble stones packed tightly into the central cavity <strong>(5)</strong> _________ order to absorb ground movement. Every few feet, long through-stones span the entire thickness, tying both sides firmly <strong>(6)</strong> _________ one another. When built correctly, a dry-stone wall can easily endure <strong>(7)</strong> _________ over two hundred years with minimal maintenance.</p>",
            [
                (3, "for", "Duration Preposition (A2-B1)", "Divided pastures 'for' centuries.", ["for"]),
                (4, "without", "Preposition of Exclusion (B1)", "Constructed 'without' the use of mortar.", ["without"]),
                (5, "in", "Purpose Connector (B1-B2)", "'in' order to absorb movement.", ["in"]),
                (6, "to", "Dependent Preposition (B1)", "Tying sides firmly 'to' one another.", ["to", "into"]),
                (7, "for", "Preposition of Duration (B1)", "Endure 'for' over two hundred years.", ["for"])
            ]
        ),
        (
            "Alpine Seed Banks and Climate Resilience",
            "<p>Perched high in the Swiss Alps, a specialized botanical research station is collecting thousands of alpine plant seeds before warming temperatures push them <strong>(3)</strong> _________ extinction. As mountain glaciers retreat, high-altitude plant species face severe competition from lowland flora migrating upward. Because alpine plants are uniquely adapted <strong>(4)</strong> _________ extreme cold and thin soils, they have nowhere higher to go.</p><p>Botanists meticulously dry the gathered seeds before storing them at minus twenty degrees Celsius, a temperature at <strong>(5)</strong> _________ seeds can remain viable for centuries. The project aims not only to preserve genetic biodiversity, but also to identify resilient genes <strong>(6)</strong> _________ could help agricultural crops withstand future climatic volatility. In the words of the project director, each glass vial represents an insurance policy <strong>(7)</strong> _________ botanical catastrophe.</p>",
            [
                (3, "into", "Directional Preposition (B1)", "Push them 'into' extinction (or toward).", ["into", "toward", "towards"]),
                (4, "to", "Dependent Preposition (B2)", "Adapted 'to' extreme cold.", ["to"]),
                (5, "which", "Prepositional Relative (B2)", "Temperature at 'which' seeds remain viable.", ["which"]),
                (6, "that", "Relative Pronoun (B1)", "Resilient genes 'that' could help (or which).", ["that", "which"]),
                (7, "against", "Preposition of Protection (B2)", "Insurance policy 'against' catastrophe.", ["against"])
            ]
        ),
        (
            "The Physics of Murmurations",
            "<p>At dusk during the autumn months, thousands of European starlings assemble across reed beds, sweeping through the twilight sky in colossal, undulating clouds known <strong>(3)</strong> _________ murmurations. To observers on the ground, the flock appears to move as a single sentient super-organism, twisting and turning with breath-taking synchronization.</p><p>For decades, naturalists wondered <strong>(4)</strong> _________ individual birds could coordinate these rapid evasive maneuvers without colliding. High-speed video analysis has revealed that each starling tracks the position and velocity of precisely seven neighboring birds, regardless <strong>(5)</strong> _________ how far apart they fly. When one bird turns to evade an incoming peregrine falcon, this directional signal ripples through the entire flock <strong>(6)</strong> _________ a speed of nearly forty meters per second, allowing the murmuration to morph almost instantaneously <strong>(7)</strong> _________ an impenetrable fluid shield.</p>",
            [
                (3, "as", "Passive Identifier (B1)", "Known 'as' murmurations.", ["as"]),
                (4, "how", "Interrogative Connective (B1)", "Wondered 'how' individual birds coordinate.", ["how"]),
                (5, "of", "Dependent Preposition (B1-B2)", "Regardless 'of' how far apart.", ["of"]),
                (6, "at", "Preposition of Speed/Rate (B1)", "'at' a speed of nearly forty meters.", ["at"]),
                (7, "into", "Preposition of Transformation (B1-B2)", "Morph almost instantaneously 'into'.", ["into"])
            ]
        ),
        (
            "The History of the Greenwich Meridian",
            "<p>Every time you set your wristwatch or check an international time zone, you are paying homage <strong>(3)</strong> _________ a brass line embedded in the cobblestones of the Royal Observatory in Greenwich, London. In 1884, representatives from twenty-five nations gathered in Washington D.C. to agree <strong>(4)</strong> _________ a single standardized zero-degree meridian from which all world longitude and time would be calculated.</p><p>Before this historic consensus, almost every maritime nation measured nautical charts from <strong>(5)</strong> _________ own capital city, resulting in perilous navigational confusion across global shipping lanes. Greenwich was chosen largely <strong>(6)</strong> _________ over seventy percent of the world's commercial merchant fleet was already relying on British admiralty charts. Today, the Prime Meridian stands as a monumental landmark dividing the Eastern and Western hemispheres <strong>(7)</strong> _________ two equal halves.</p>",
            [
                (3, "to", "Dependent Preposition (B2)", "Pay homage 'to' a brass line.", ["to"]),
                (4, "on", "Prepositional Verb (B2)", "Agree 'on' a standardized meridian (or upon).", ["on", "upon"]),
                (5, "its", "Possessive Determiner (A2-B1)", "From 'its' own capital city.", ["its", "their"]),
                (6, "because", "Causal Conjunction (A2-B1)", "Chosen largely 'because' merchant fleet.", ["because", "since", "as"]),
                (7, "into", "Preposition of Division (B1)", "Dividing hemispheres 'into' two halves.", ["into"])
            ]
        ),
        (
            "Bioluminescent Waves and Dinoflagellates",
            "<p>On warm summer nights along certain tropical coastlines, breaking ocean waves suddenly glow with an eerie neon-blue radiance. This breathtaking phenomenon is caused <strong>(3)</strong> _________ microscopic single-celled marine plankton known as dinoflagellates. When agitated by physical turbulence—such as a crashing wave or a swimming dolphin—these tiny organisms trigger an enzymatic chemical reaction <strong>(4)</strong> _________ emits a brilliant flash of cold light.</p><p>Scientists believe this flash acts <strong>(5)</strong> _________ a defensive alarm designed to startle predators or attract larger fish to devour the plankton's attackers. While witnessing a glowing sea is unforgettable, dense blooms can occasionally deplete oxygen levels in sheltered bays, posing risks <strong>(6)</strong> _________ local fish populations. Understanding these blooms helps oceanographers monitor coastal water health <strong>(7)</strong> _________ greater precision.</p>",
            [
                (3, "by", "Passive Agent (A2-B1)", "Caused 'by' microscopic plankton.", ["by"]),
                (4, "that", "Relative Pronoun (B1)", "Enzymatic reaction 'that' emits cold light (or which).", ["that", "which"]),
                (5, "as", "Role Preposition (B1)", "Acts 'as' a defensive alarm.", ["as"]),
                (6, "to", "Preposition after Noun (B1-B2)", "Posing risks 'to' local fish.", ["to"]),
                (7, "with", "Preposition of Manner (B1-B2)", "Monitor health 'with' greater precision.", ["with"])
            ]
        ),
        (
            "The Rediscovery of Forgotten Apples",
            "<p>Walk into a modern supermarket today and you are likely to find fewer <strong>(3)</strong> _________ half a dozen standardized apple varieties on display. Yet a century ago, orchards across Europe and North America cultivated thousands of distinct heritage cultivars, each bred <strong>(4)</strong> _________ specific regional soils, winter hardiness, or distinct cider-making qualities.</p><p>In recent years, dedicated botanical historians have traveled through abandoned farmsteads in search <strong>(5)</strong> _________ gnarled antique trees that have survived untended for decades. When a forgotten variety is identified, researchers graft scion twigs onto healthy rootstocks to preserve the genetic lineage. These heirloom varieties possess natural resistances to fungal diseases <strong>(6)</strong> _________ could prove vital as commercial orchards confront shifting weather patterns brought <strong>(7)</strong> _________ by global climate change.</p>",
            [
                (3, "than", "Comparative Particle (A2-B1)", "Fewer 'than' half a dozen.", ["than"]),
                (4, "for", "Preposition of Purpose (B1)", "Bred 'for' specific regional soils.", ["for"]),
                (5, "of", "Fixed Idiom (B1)", "In search 'of' gnarled antique trees.", ["of"]),
                (6, "that", "Relative Pronoun (B1)", "Resistances 'that' could prove vital (or which).", ["that", "which"]),
                (7, "about", "Phrasal Verb Particle (B2)", "Brought 'about' by climate change (or on).", ["about", "on"])
            ]
        ),
        (
            "The Architecture of Underground Cisterns",
            "<p>Beneath the bustling streets of Istanbul lies the Basilica Cistern, an immense subterranean cavern constructed in the sixth century <strong>(3)</strong> _________ Emperor Justinian. Supported by more than three hundred towering marble columns, this colossal reservoir was engineered to supply freshwater to the imperial palace in times <strong>(4)</strong> _________ siege.</p><p>Freshwater was transported from mountain reservoirs over nineteen kilometers away <strong>(5)</strong> _________ a complex network of Roman aqueducts. The cistern's brick walls were coated with an exceptionally durable waterproof mortar formulated from crushed tiles and lime. Even today, walking across the wooden raised walkways above shallow water, visitors cannot help <strong>(6)</strong> _________ marvel at the sheer scale of Byzantine hydraulic engineering, which functioned reliably <strong>(7)</strong> _________ centuries without modern electric pumps.</p>",
            [
                (3, "by", "Passive Agent (A2-B1)", "Constructed 'by' Emperor Justinian.", ["by", "under"]),
                (4, "of", "Fixed Prepositional Phrase (B1-B2)", "In times 'of' siege.", ["of"]),
                (5, "via", "Preposition of Means/Route (B2)", "Aqueducts 'via' or through a network.", ["via", "through"]),
                (6, "but", "Idiomatic Structure (B2)", "Cannot help 'but' marvel.", ["but"]),
                (7, "for", "Duration Preposition (A2-B1)", "Functioned reliably 'for' centuries.", ["for"])
            ]
        ),
        (
            "The Psychology of Urban Tree Canopies",
            "<p>Public health researchers have long recognized that green foliage in city parks offers psychological relief, but recent empirical studies demonstrate that tree canopies provide far greater benefits <strong>(3)</strong> _________ previously measured. Neighborhoods with dense street tree coverage report significantly lower rates of cardiovascular illness and chronic stress compared <strong>(4)</strong> _________ treeless districts.</p><p>Beyond shading concrete pavements and reducing localized heat island effects, mature trees release aromatic chemical compounds called phytoncides into the air. When inhaled, these organic aerosols boost the human immune system <strong>(5)</strong> _________ well as lowering blood pressure. Municipal city planners are therefore beginning to treat street trees not <strong>(6)</strong> _________ mere decorative street furniture, but as indispensable public healthcare infrastructure <strong>(7)</strong> _________ yields measurable economic dividends.</p>",
            [
                (3, "than", "Comparative Particle (A2-B1)", "Greater benefits 'than' previously measured.", ["than"]),
                (4, "to", "Dependent Preposition (B1-B2)", "Compared 'to' or with treeless districts.", ["to", "with"]),
                (5, "as", "Correlative Conjunction (B1)", "'as' well as lowering blood pressure.", ["as"]),
                (6, "as", "Role Preposition (B1)", "Not 'as' mere decorative furniture.", ["as"]),
                (7, "that", "Relative Pronoun (B1)", "Infrastructure 'that' yields dividends (or which).", ["that", "which"])
            ]
        ),
        (
            "The Migratory Feat of the Arctic Tern",
            "<p>No creature on Earth undertakes a more staggering annual migration <strong>(3)</strong> _________ the Arctic tern. Breeding during the brief Arctic summer in Greenland and northern Canada, this modest seabird embarks each autumn <strong>(4)</strong> _________ an epic southward voyage that terminates on the ice pack of Antarctica.</p><p>By traveling from pole to pole, the tern experiences two summers every year, basking in more daylight <strong>(5)</strong> _________ any other living animal. Miniaturized geolocator tags attached to individual birds have revealed that terns do not fly in direct straight lines, <strong>(6)</strong> _________ instead follow sweeping zigzag trajectories across ocean trade winds to conserve energy. Over a single lifetime spanning thirty years, an Arctic tern flies roughly two million kilometers—the equivalent <strong>(7)</strong> _________ flying to the Moon and back three times.</p>",
            [
                (3, "than", "Comparative Particle (A2-B1)", "More staggering migration 'than' Arctic tern.", ["than"]),
                (4, "on", "Preposition of Journey (B1)", "Embarks 'on' an epic voyage (or upon).", ["on", "upon"]),
                (5, "than", "Comparative Particle (A2-B1)", "More daylight 'than' any other living animal.", ["than"]),
                (6, "but", "Contrastive Conjunction (B1)", "Not direct, 'but' instead follow.", ["but"]),
                (7, "of", "Prepositional Equivalence (B1-B2)", "Equivalent 'of' flying to Moon.", ["of"])
            ]
        ),
        (
            "The Secret Life of Lichen",
            "<p>Clinging to windswept granite boulders and the trunks of ancient oaks, lichen appears at first glance to be a single primitive plant. In reality, it represents one of nature's <strong>(3)</strong> _________ extraordinary collaborative partnerships. Lichen is not an individual organism, <strong>(4)</strong> _________ a composite composite alliance between a fungus and an alga or cyanobacterium.</p><p>The fungal partner constructs a protective cellular shelter that retains moisture and extracts mineral nutrients from rock surfaces, <strong>(5)</strong> _________ the photosynthetic algal partner produces sugars and carbohydrates using sunlight. Because neither organism could survive alone in such desolate habitats, this mutualistic symbiosis allows lichens to thrive in places <strong>(6)</strong> _________ virtually nothing else can grow, from scorched desert rocks to frozen polar nunataks, enduring harsh ultraviolet radiation <strong>(7)</strong> _________ ease.</p>",
            [
                (3, "most", "Superlative Form (A2-B1)", "One of nature's 'most' extraordinary.", ["most"]),
                (4, "but", "Contrastive Conjunction (B1)", "Not X, 'but' a composite alliance.", ["but"]),
                (5, "while", "Contrastive Conjunction (B1-B2)", "'while' or whilst the algal partner produces.", ["while", "whilst"]),
                (6, "where", "Relative Adverb (B1)", "Places 'where' virtually nothing else can grow.", ["where"]),
                (7, "with", "Preposition of Manner (B1-B2)", "Enduring radiation 'with' ease.", ["with"])
            ]
        ),
        (
            "The Acoustic Architecture of Ancient Amphitheaters",
            "<p>At the ancient Greek theater of Epidaurus, constructed in the fourth century BCE, an actor speaking in an ordinary conversational whisper at the center of the circular orchestra <strong>(3)</strong> _________ be heard clearly by spectators sitting in the highest stone row, over sixty meters away.</p><p>For centuries, historians attributed this acoustic phenomenon <strong>(4)</strong> _________ mystical architectural genius or favorable prevailing hillside breezes. Modern acoustic researchers have finally solved the puzzle: the tiered limestone seating acts <strong>(5)</strong> _________ a sophisticated acoustic filter. The carved stone benches reflect and amplify high-frequency speech consonants <strong>(6)</strong> _________ simultaneously suppressing low-frequency background noise like rustling foliage or wind. Spectators were thus able to absorb complex dramatic verse without straining <strong>(7)</strong> _________ hear a single syllable.</p>",
            [
                (3, "can", "Modal Verb (A2-B1)", "Actor 'can' be heard clearly (or could).", ["can", "could"]),
                (4, "to", "Dependent Preposition (B2)", "Attributed this 'to' mystical genius.", ["to"]),
                (5, "as", "Role Preposition (B1)", "Acts 'as' a sophisticated filter.", ["as"]),
                (6, "while", "Conjunction of Simultaneous Contrast (B1-B2)", "'while' simultaneously suppressing.", ["while", "whilst"]),
                (7, "to", "Infinitive Marker (A2-B1)", "Straining 'to' hear a single syllable.", ["to"])
            ]
        ),
        (
            "The Restoration of Peat Bogs",
            "<p>Covering just three percent of the planet's land surface, peatlands store twice <strong>(3)</strong> _________ much carbon as all the world's forests combined. However, centuries of draining bogs for agriculture and commercial peat extraction <strong>(4)</strong> _________ turned these vital carbon vaults into major sources of greenhouse gas emissions.</p><p>When peat dries out, exposed carbon reacts with atmospheric oxygen and decomposes rapidly. Conservation charities are now actively rewetting drained bogs <strong>(5)</strong> _________ building low peat dams across drainage ditches. Within months of restoring water levels, specialized sphagnum mosses begin to recolonize the surface, trapping moisture and locking carbon back into the soggy ground. Scientists estimate that restoring degraded peatlands represents one of the <strong>(6)</strong> _________ cost-effective nature-based solutions to climate warming available <strong>(7)</strong> _________ humanity today.</p>",
            [
                (3, "as", "Comparative Structure (A2-B1)", "Twice 'as' much carbon as forests.", ["as"]),
                (4, "have", "Present Perfect Auxiliary (B1)", "Extraction 'have' turned these vaults.", ["have"]),
                (5, "by", "Preposition of Method (B1)", "Rewetting bogs 'by' building dams.", ["by"]),
                (6, "most", "Superlative Form (A2-B1)", "One of the 'most' cost-effective.", ["most"]),
                (7, "to", "Preposition after Adjective (B1-B2)", "Available 'to' humanity today.", ["to"])
            ]
        ),
        (
            "The History of the Mechanical Clock",
            "<p>Before the invention of the mechanical escapement in medieval Europe, human civilization measured time using water clocks, sundials, and burning incense sticks. None of these early devices, however, <strong>(3)</strong> _________ maintain precision during harsh winter freezes or cloudy days.</p><p>The breakthrough occurred in fourteenth-century monasteries, <strong>(4)</strong> _________ monks required punctual timekeeping to observe strict nocturnal prayer schedules. Early verge-and-foliot clocks converted the falling force of a heavy suspended weight into regular, oscillating mechanical ticks. For the first time in human history, time was divided <strong>(5)</strong> _________ abstract, uniform hours rather than stretching and shrinking with seasonal daylight. This mechanical revolution fundamentally transformed European commerce and navigation, paving the <strong>(6)</strong> _________ for the scientific and industrial revolutions <strong>(7)</strong> _________ followed.</p>",
            [
                (3, "could", "Past Ability Modal (B1)", "None of these 'could' maintain precision.", ["could"]),
                (4, "where", "Relative Adverb (B1)", "In fourteenth-century monasteries, 'where' monks.", ["where"]),
                (5, "into", "Preposition of Division (B1)", "Divided 'into' abstract uniform hours.", ["into"]),
                (6, "way", "Fixed Idiom (B2)", "Paving the 'way' for revolutions.", ["way"]),
                (7, "that", "Relative Pronoun (B1)", "Revolutions 'that' followed (or which).", ["that", "which"])
            ]
        ),
        (
            "The Resilience of Seagrass Meadows",
            "<p>Beneath the gentle swells of shallow coastal bays, expansive underwater meadows of seagrass ripple in the tides. Though often mistaken <strong>(3)</strong> _________ seaweeds, seagrasses are true flowering plants complete with roots, stems, leaves, and tiny blossoms pollinated underwater.</p><p>These submerged prairies play an indispensable role in coastal ecology. Their dense root rhizomes bind seabed sediments, preventing storm erosion and keeping coastal waters clear. Furthermore, seagrass meadows can capture carbon up to thirty-five times faster <strong>(4)</strong> _________ tropical rainforests, locking it safely in underwater soil layers for thousands of years. Marine biologists warn that losing these meadows threatens not <strong>(5)</strong> _________ coastal fisheries, but global climate balance. Today, coastal restoration groups are carefully planting millions of seeds <strong>(6)</strong> _________ order to revive damaged meadows around the world, proving that nature can heal when given <strong>(7)</strong> _________ chance.</p>",
            [
                (3, "for", "Prepositional Collocation (B1-B2)", "Mistaken 'for' seaweeds.", ["for"]),
                (4, "than", "Comparative Particle (A2-B1)", "Faster 'than' tropical rainforests.", ["than"]),
                (5, "only", "Correlative Conjunction (B1-B2)", "Not 'only' coastal fisheries (or merely).", ["only", "merely"]),
                (6, "in", "Purpose Connector (B1-B2)", "'in' order to revive damaged meadows.", ["in"]),
                (7, "a", "Indefinite Article (A2)", "Given 'a' chance.", ["a"])
            ]
        ),
        (
            "The Intelligence of Octopuses",
            "<p>Among marine invertebrates, the octopus stands out as an astonishing intellectual anomaly. With two-thirds of its neurons distributed throughout its eight flexible arms rather <strong>(3)</strong> _________ concentrated exclusively in its brain, an octopus can taste, touch, and manipulate objects semi-autonomously.</p><p>Laboratory trials have demonstrated that these cephalopods possess remarkable problem-solving capabilities. They can unscrew child-proof medicine jars, navigate complex mazes, and use discarded coconut shells <strong>(4)</strong> _________ portable armor against predatory sharks. Furthermore, octopuses exhibit playful behaviors and can distinguish individual human handlers, squirting jets of water <strong>(5)</strong> _________ people they dislike. Because octopuses evolved intelligence along an evolutionary branch completely separate <strong>(6)</strong> _________ mammals, studying their nervous system offers scientists an unprecedented glimpse into <strong>(7)</strong> _________ an alternative form of mind can function.</p>",
            [
                (3, "than", "Comparative Particle (B1)", "Rather 'than' concentrated in brain.", ["than"]),
                (4, "as", "Role Preposition (B1)", "Coconut shells 'as' portable armor.", ["as"]),
                (5, "at", "Directional Preposition (B1)", "Squirting jets of water 'at' people.", ["at"]),
                (6, "from", "Preposition of Separation (B2)", "Separate 'from' mammals.", ["from"]),
                (7, "how", "Interrogative Connective (B1-B2)", "Glimpse into 'how' an alternative mind functions.", ["how"])
            ]
        ),
        (
            "The Preservation of Historic Timber Ships",
            "<p>When historic wooden warships like the Mary Rose or the Vasa were raised from muddy sea beds after centuries of submersion, marine archaeologists faced an immediate crisis. The moment ancient waterlogged timber dries <strong>(3)</strong> _________, cellular moisture evaporates, causing the wood to shrink, warp, and crumble into dust.</p><p>To prevent catastrophic collapse, conservators spray the hull continuous with polyethylene glycol, a water-soluble synthetic wax. Over years of spraying, this compound slowly penetrates deep <strong>(4)</strong> _________ the porous wood fibers, replacing water inside the plant cell walls. Once the wax solidifies, the timber can safely dry without losing <strong>(5)</strong> _________ structural shape. This painstaking preservation process requires decades of patience, but it allows museum visitors to gaze <strong>(6)</strong> _________ original naval craftsmanship that would otherwise have vanished <strong>(7)</strong> _________ trace.</p>",
            [
                (3, "out", "Phrasal Verb Particle (B1)", "Timber dries 'out'.", ["out"]),
                (4, "into", "Directional Preposition (B1)", "Penetrates deep 'into' wood fibers.", ["into"]),
                (5, "its", "Possessive Determiner (A2-B1)", "Without losing 'its' structural shape.", ["its"]),
                (6, "upon", "Preposition after Verb (B2)", "Gaze 'upon' or at naval craftsmanship.", ["upon", "at"]),
                (7, "without", "Fixed Idiom (B1-B2)", "Vanished 'without' trace.", ["without"])
            ]
        ),
        (
            "The Renaissance of Urban Beekeeping",
            "<p>On flat rooftops above financial districts and residential towers across the globe, an unexpected agricultural movement is buzzing. Urban beekeeping has expanded rapidly <strong>(3)</strong> _________ recent years, with thousands of amateur apiarists tending hives amid skyscrapers.</p><p>Curiously, research indicates that metropolitan honeybees frequently produce healthier honey <strong>(4)</strong> _________ their rural counterparts. Cities offer a diverse floral diet in botanical gardens, balcony planters, and municipal parks, whereas agricultural countryside is often dominated <strong>(5)</strong> _________ chemical-intensive monocultures that flower for only two weeks a year. Furthermore, municipal park authorities report that city bees boost pollination rates for urban fruit orchards. Beekeeping thus bridges the divide <strong>(6)</strong> _________ urban dwellers and the natural systems <strong>(7)</strong> _________ sustain our food supply.</p>",
            [
                (3, "in", "Time Preposition (A2-B1)", "Expanded rapidly 'in' recent years.", ["in"]),
                (4, "than", "Comparative Particle (A2-B1)", "Healthier honey 'than' rural counterparts.", ["than"]),
                (5, "by", "Passive Agent (A2-B1)", "Dominated 'by' monocultures.", ["by"]),
                (6, "between", "Preposition of Division (B1)", "Bridges the divide 'between' dwellers and nature.", ["between"]),
                (7, "that", "Relative Pronoun (B1)", "Systems 'that' sustain food supply (or which).", ["that", "which"])
            ]
        ),
        (
            "The Wonder of Bioluminescent Caves",
            "<p>Deep beneath the lush hills of New Zealand's North Island lies the Waitomo cave complex, famous worldwide for its thousands of shimmering subterranean lights. As visitors glide silently into the limestone caverns aboard small rowboats, the vaulted ceiling overhead resembles a brilliant galaxy <strong>(3)</strong> _________ stars.</p><p>These living lights are produced <strong>(4)</strong> _________ the carnivorous larvae of an endemic fungus gnat. Each glowworm suspends dozens of silk threads coated with sticky mucus droplets from the cave ceiling, then illuminates its tail using a chemical bioluminescent reaction. Attracted <strong>(5)</strong> _________ the glowing light in total darkness, midges and moths fly upward and become entangled in the hanging silk snare. When the river level rises during heavy rainfall, cave guides monitor air humidity carefully, <strong>(6)</strong> _________ dry conditions cause the delicate snare threads to tangle together and ruin the glowworms' ability <strong>(7)</strong> _________ feed.</p>",
            [
                (3, "of", "Preposition of Composition (A2-B1)", "Galaxy 'of' stars.", ["of"]),
                (4, "by", "Passive Agent (A2-B1)", "Produced 'by' the larvae.", ["by"]),
                (5, "by", "Passive Agent (B1)", "Attracted 'by' or to the glowing light.", ["by", "to"]),
                (6, "as", "Causal Conjunction (B1)", "'as' dry conditions cause snares to tangle (or since, because).", ["as", "since", "because"]),
                (7, "to", "Infinitive Marker (A2-B1)", "Ability 'to' feed.", ["to"])
            ]
        ),
        (
            "The Engineering of Roman Concrete",
            "<p>More than two thousand years after they were built, Roman harbor piers, aqueducts, and the colossal unreinforced dome of the Pantheon remain structurally sound. Modern concrete structures, <strong>(3)</strong> _________ contrast, often begin to crack and deteriorate after just fifty or sixty years of exposure to environmental weathering.</p><p>Geologists studying Roman concrete have unraveled the secret <strong>(4)</strong> _________ its astonishing durability. Roman builders blended volcanic ash from Mount Vesuvius with slaked lime and seawater. When seawater percolated through the concrete matrix, it triggered a rare chemical reaction <strong>(5)</strong> _________ caused interlocking crystals of aluminum tobermorite to grow inside microscopic fractures. Instead of weakening the structure, exposure to saltwater actually strengthened it <strong>(6)</strong> _________ time. Modern materials scientists are now attempting to replicate this self-healing formula in <strong>(7)</strong> _________ to design sustainable sea walls that resist rising sea levels.</p>",
            [
                (3, "by", "Contrastive Idiom (B1-B2)", "'by' contrast (or in).", ["by", "in"]),
                (4, "to", "Dependent Preposition (B2)", "Secret 'to' its durability (or of).", ["to", "of"]),
                (5, "that", "Relative Pronoun (B1)", "Reaction 'that' caused crystals (or which).", ["that", "which"]),
                (6, "over", "Preposition of Time (B1-B2)", "Strengthened it 'over' time.", ["over"]),
                (7, "order", "Purpose Connector (B1-B2)", "'in' order to design sustainable walls.", ["order"])
            ]
        )
    ]
]

TASK_4_EXPANSIONS = [
    {
        "task": 4,
        "tag": "Task 4 • Multiple-Choice Gap-Fill",
        "title": title,
        "instruction": "Read the text below and choose the correct word (A, B, C, or D) for each gap.",
        "passage": passage,
        "questions": [
            {
                "id": f"r_q{num}",
                "num": num,
                "type": "select",
                "stem": f"{num}.",
                "options": [
                    {"val": "A", "label": f"A - {opts[0]}"},
                    {"val": "B", "label": f"B - {opts[1]}"},
                    {"val": "C", "label": f"C - {opts[2]}"},
                    {"val": "D", "label": f"D - {opts[3]}"}
                ],
                "key": key,
                "skill": skill,
                "trap": trap
            }
            for num, opts, key, skill, trap in q_specs
        ]
    }
    for title, passage, q_specs in [
        (
            "Commercial Satellite Telematics",
            "Fleet logistics operators are utilizing satellite tracking systems to <strong>(8)</strong> _________ operational efficiency. By monitoring engine diagnostics continuously, maintenance engineers can identify faulty parts before vehicles <strong>(9)</strong> _________ breakdown on remote highways. This preventative approach has <strong>(10)</strong> _________ reduced repair costs across national haulage networks. Drivers also receive real-time navigational guidance designed to <strong>(11)</strong> _________ urban traffic bottlenecks during morning rush hours. Analysts believe telematics will remain an indispensable <strong>(12)</strong> _________ of corporate supply chains.",
            [
                (8, ["maximize", "expand", "broaden", "enlarge"], "A", "Collocation (B2)", "Maximize efficiency."),
                (9, ["suffer", "tolerate", "undergo", "receive"], "A", "Collocation (B2)", "Suffer a breakdown."),
                (10, ["substantially", "firmly", "strictly", "closely"], "A", "Adverbial Modification (B2)", "Substantially reduced costs."),
                (11, ["circumvent", "abandon", "neglect", "dismiss"], "A", "Formal Lexis (B2)", "Circumvent bottlenecks."),
                (12, ["component", "fraction", "division", "ingredient"], "A", "Noun Collocation (B2)", "Indispensable component.")
            ]
        ),
        (
            "The Psychology of Ambient Sound",
            "Modern architectural planners are increasingly aware of how acoustic environments <strong>(8)</strong> _________ employee well-being. Chronic exposure to high decibel levels in open-plan offices can <strong>(9)</strong> _________ focus and elevate cortisol production. To counteract this, designers are installing natural water features that <strong>(10)</strong> _________ harsh printer and typing noises. Clinical trials demonstrate that soothing broadband soundscapes significantly <strong>(11)</strong> _________ cognitive fatigue. Integrating psychoacoustic principles into workspace layout represents a crucial <strong>(12)</strong> _________ toward healthier commercial offices.",
            [
                (8, ["influence", "compel", "enforce", "induce"], "A", "Verb Selection (B2)", "Influence well-being."),
                (9, ["disrupt", "fracture", "split", "demolish"], "A", "Lexical Collocation (B2)", "Disrupt focus."),
                (10, ["mask", "cloak", "shroud", "veil"], "A", "Acoustic Lexis (B2)", "Mask harsh noises."),
                (11, ["alleviate", "abate", "deflate", "lighten"], "A", "Formal Vocabulary (B2)", "Alleviate cognitive fatigue."),
                (12, ["step", "pace", "stride", "march"], "A", "Idiomatic Collocation (B1-B2)", "A crucial step toward.")
            ]
        ),
        (
            "Subterranean Fungal Networks",
            "Botanists have revealed that forest trees do not compete as isolated organisms, but actively <strong>(8)</strong> _________ via fungal threads. Mycorrhizal networks colonize root tips, <strong>(9)</strong> _________ underground conduits that link entire groves. Mature parent trees transfer carbon to younger saplings that grow in deep <strong>(10)</strong> _________, thereby boosting seedling survival rates. When trees face beetle infestations, they release chemical signals through the network that <strong>(11)</strong> _________ neighbors to activate their own defenses. These remarkable partnerships have transformed our <strong>(12)</strong> _________ of forest ecology.",
            [
                (8, ["collaborate", "combine", "associate", "concur"], "A", "Scientific Lexis (B2)", "Actively collaborate."),
                (9, ["forming", "erecting", "framing", "compiling"], "A", "Participial Phrase (B2)", "Forming conduits."),
                (10, ["shade", "shadow", "gloom", "darkness"], "A", "Environmental Noun (B1-B2)", "Grow in deep shade."),
                (11, ["prompt", "instigate", "provoke", "impel"], "A", "Causal Verb (B2)", "Prompt neighbors to activate."),
                (12, ["understanding", "realization", "apprehension", "judgment"], "A", "Collocation (B2)", "Transformed our understanding.")
            ]
        ),
        (
            "Preserving Antique Vellum Bindings",
            "Restoring centuries-old leather and vellum books requires a delicate balance of science and craftsmanship. Over time, fluctuating humidity causes parchment leaves to <strong>(8)</strong> _________ and buckle. Conservators place folios inside controlled chambers that <strong>(9)</strong> _________ humidify the sheets before pressing. Chemical tests are conducted to <strong>(10)</strong> _________ whether acidic iron gall inks are eating into the vellum matrix. Rather than applying synthetic adhesives, specialists use reversible wheat starch paste to <strong>(11)</strong> _________ torn gutters, ensuring that original bindings remain intact for future <strong>(12)</strong> _________.",
            [
                (8, ["warp", "bend", "curve", "twist"], "A", "Material Degradation Lexis (B2)", "Vellum warps and buckles."),
                (9, ["gradually", "hastily", "sharply", "promptly"], "A", "Adverb Selection (B2)", "Gradually humidify."),
                (10, ["determine", "decide", "settle", "judge"], "A", "Diagnostic Verb (B2)", "Determine whether inks eat."),
                (11, ["repair", "mend", "restore", "patch"], "A", "Conservation Collocation (B2)", "Repair torn gutters."),
                (12, ["generations", "cohorts", "descendants", "successors"], "A", "Noun Selection (B1-B2)", "Future generations.")
            ]
        ),
        (
            "Biomimetic Architectural Engineering",
            "Engineers are increasingly looking to biological structures to <strong>(8)</strong> _________ sustainable building solutions. The Eastgate Centre in Harare, Zimbabwe, famously mirrors the cooling architecture of termite mounds, which maintain <strong>(9)</strong> _________ internal temperatures despite scorching outdoor heat. Passive air ducts draw night air into the base of the structure, while thermal mass concrete <strong>(10)</strong> _________ heat during daytime hours. This innovative biomimetic design <strong>(11)</strong> _________ thirty-five percent less energy than conventional office towers, demonstrating that natural engineering holds the <strong>(12)</strong> _________ to low-emission urban architecture.",
            [
                (8, ["develop", "originate", "invent", "erect"], "A", "Collocation (B2)", "Develop sustainable solutions."),
                (9, ["constant", "stagnant", "fixed", "motionless"], "A", "Adjective Collocation (B2)", "Maintain constant temperatures."),
                (10, ["absorbs", "intakes", "ingests", "imbibes"], "A", "Thermal Lexis (B2)", "Concrete absorbs heat."),
                (11, ["consumes", "exhausts", "spends", "depletes"], "A", "Commercial/Energy Verb (B2)", "Consumes less energy."),
                (12, ["key", "clue", "pass", "ticket"], "A", "Idiomatic Collocation (B1-B2)", "Holds the key to.")
            ]
        ),
        (
            "Alpine Glaciology and Ice Core Archives",
            "Glacial ice sheets act as planetary time capsules, locking ancient atmospheric gases into tiny air bubbles that <strong>(8)</strong> _________ for hundreds of millennia. By extracting vertical ice core cylinders from polar domes, paleoclimatologists can reconstruct historic temperatures with unmatched <strong>(9)</strong> _________. Chemical isotopic analysis reveals how atmospheric carbon levels have <strong>(10)</strong> _________ across ancient ice age cycles. However, as global temperatures climb, retreating glacier tongues <strong>(11)</strong> _________ severe flooding hazards for downstream alpine communities, making glaciological monitoring more <strong>(12)</strong> _________ than ever before.",
            [
                (8, ["persist", "endure", "prolong", "sustain"], "A", "Natural Science Lexis (B2)", "Air bubbles that persist."),
                (9, ["precision", "fidelity", "strictness", "rigor"], "A", "Collocation (B2)", "Unmatched precision."),
                (10, ["fluctuated", "wavered", "swayed", "rocked"], "A", "Scientific Trends (B2)", "Carbon levels have fluctuated."),
                (11, ["pose", "place", "set", "post"], "A", "Risk Collocation (B2)", "Pose severe hazards."),
                (12, ["urgent", "insistent", "exigent", "hasty"], "A", "Contextual Register (B2)", "More urgent than ever.")
            ]
        ),
        (
            "The Revival of Natural Dyes",
            "The textile fashion sector is reconsidering historic botanical pigments in an effort to <strong>(8)</strong> _________ reliance on petroleum-derived synthetic colorants. Historically, vibrant purples and scarlets were <strong>(9)</strong> _________ from lichens, madder roots, and oak galls through complex fermentation rituals. While synthetic azo dyes are cheaper to mass-produce, their wastewater discharges <strong>(10)</strong> _________ severe chemical contamination in river ecosystems. Contemporary artisanal fashion labels are proving that plant-based dyes can achieve rich color <strong>(11)</strong> _________ without generating toxic effluents, marking a significant <strong>(12)</strong> _________ in eco-conscious apparel manufacturing.",
            [
                (8, ["diminish", "shorten", "shrink", "narrow"], "A", "Industrial Collocation (B2)", "Diminish reliance on."),
                (9, ["extracted", "withdrawn", "plucked", "pulled"], "A", "Chemical Extraction Lexis (B2)", "Extracted from lichens."),
                (10, ["cause", "induce", "breed", "originate"], "A", "Causal Verb (B1-B2)", "Discharges cause contamination."),
                (11, ["fastness", "durability", "firmness", "stiffness"], "A", "Textile Term (B2-C1)", "Color fastness."),
                (12, ["milestone", "landmark", "checkpoint", "border"], "A", "Collocation (B2)", "Significant milestone.")
            ]
        ),
        (
            "The Acoustics of Stradivarius Violins",
            "For over three centuries, musicians and luthiers have attempted to decipher what makes violins crafted by Antonio Stradivari <strong>(8)</strong> _________ such resonant acoustic timbre. Some acousticians attribute the instrument's tonal brilliance to the dense alpine spruce timber harvested during a prolonged European mini ice age, which produced unusually uniform growth <strong>(9)</strong> _________. Other researchers contend that mineral-rich chemical varnishes formulated with volcanic ash and alum <strong>(10)</strong> _________ the key acoustic factor. While modern replica violins match the physical dimensions of antique originals, Stradivarius instruments continue to <strong>(11)</strong> _________ astronomical valuations in the global fine arts <strong>(12)</strong> _________.",
            [
                (8, ["produce", "fabricate", "forge", "erect"], "A", "Acoustic Collocation (B2)", "Produce resonant timbre."),
                (9, ["rings", "circles", "loops", "hoops"], "A", "Botanical Lexis (B2)", "Growth rings in spruce."),
                (10, ["constitute", "comprise", "contain", "involve"], "A", "Formal Verb (B2)", "Constitute the key factor."),
                (11, ["command", "dictate", "impose", "compel"], "A", "Commercial Register (B2-C1)", "Command valuations."),
                (12, ["market", "bazaar", "outlet", "exchange"], "A", "Collocation (B1-B2)", "Fine arts market.")
            ]
        ),
        (
            "Wetland Peatland Restoration",
            "Peatland ecosystems covering upland basins are increasingly valued for their capability to <strong>(8)</strong> _________ massive quantities of atmospheric carbon. When left undisturbed, waterlogged sphagnum mosses decompose at a glacial rate, <strong>(9)</strong> _________ organic carbon deep underground for millennia. Decades of artificial draining for commercial forestry, however, <strong>(10)</strong> _________ peat layers to dry out and oxidize into carbon dioxide. Rewetting degraded blanket bogs has consequently become a national conservation <strong>(11)</strong> _________, serving as an economical nature-based strategy to meet carbon neutral <strong>(12)</strong> _________.",
            [
                (8, ["sequester", "confine", "isolate", "cage"], "A", "Environmental Scientific Lexis (B2-C1)", "Sequester carbon."),
                (9, ["storing", "stocking", "depoting", "shelving"], "A", "Participial Phrase (B1-B2)", "Storing organic carbon."),
                (10, ["caused", "provoked", "forced", "compelled"], "A", "Causal Verb (B1-B2)", "Caused peat to dry."),
                (11, ["priority", "precedence", "superiority", "supremacy"], "A", "Policy Collocation (B2)", "Conservation priority."),
                (12, ["targets", "goals", "aims", "marks"], "A", "Collocation (B2)", "Carbon neutral targets.")
            ]
        ),
        (
            "Autonomous Deep-Sea Gliders",
            "Oceanographic exploration has made an immense stride forward with the development of robotic buoyancy gliders that <strong>(8)</strong> _________ across deep ocean basins for months without human intervention. Instead of relying on noisy propulsion propellers, these sleek autonomous probes adjust internal oil bladders to descend and ascend, <strong>(9)</strong> _________ forward velocity from vertical lift. Onboard telemetry instruments continuously log salinity, dissolved oxygen, and acoustic currents, transmitting data packets via satellite each time the vehicle <strong>(10)</strong> _________ on the surface. These cost-effective gliders allow oceanographers to monitor vast oceanic fronts with unprecedented <strong>(11)</strong> _________, revolutionizing our ability to forecast marine <strong>(12)</strong> _________ changes.",
            [
                (8, ["navigate", "pilot", "steer", "channel"], "A", "Marine Navigation Lexis (B2)", "Navigate across basins."),
                (9, ["generating", "producing", "breeding", "framing"], "A", "Participial Phrase (B2)", "Generating forward velocity."),
                (10, ["surfaces", "emerges", "rises", "climbs"], "A", "Maritime Verb (B1-B2)", "Vehicle surfaces."),
                (11, ["frequency", "recurrence", "repetition", "habit"], "A", "Temporal Collocation (B2)", "Unprecedented frequency."),
                (12, ["ecosystem", "habitat", "biome", "sphere"], "A", "Collocation (B2)", "Marine ecosystem changes.")
            ]
        ),
        (
            "Urban Micro-Forests and Miyawaki Method",
            "Pioneered by Japanese botanist Akira Miyawaki, tiny dense urban woodlands are springing up in derelict schoolyards and motorway margins across European cities. By planting native climax tree saplings very <strong>(8)</strong> _________ together, the method stimulates intense biological competition for sunlight, accelerating vegetative growth up to ten times <strong>(9)</strong> _________ than conventional forestry schemes. These compact green sanctuaries quickly attract pollinating bees, songbirds, and beneficial beetles, creating self-sustaining biological <strong>(10)</strong> _________ within urban sprawl. Landscape architects emphasize that micro-forests also play a key role in <strong>(11)</strong> _________ heavy rainfall runoff, reducing the burden on municipal stormwater drainage <strong>(12)</strong> _________.",
            [
                (8, ["closely", "densely", "tightly", "strictly"], "A", "Collocation (B2)", "Planting saplings closely together."),
                (9, ["faster", "quicker", "swifter", "fleeter"], "A", "Comparative Particle (A2-B1)", "Ten times faster."),
                (10, ["oases", "havens", "refuges", "sanctuaries"], "A", "Metaphorical Noun (B2)", "Biological oases."),
                (11, ["absorbing", "intaking", "drinking", "imbibing"], "A", "Hydraulic Verb (B2)", "Absorbing rainfall runoff."),
                (12, ["infrastructure", "framework", "structure", "machinery"], "A", "Collocation (B2)", "Drainage infrastructure.")
            ]
        ),
        (
            "The Science of Sourdough Fermentation",
            "Unlike commercial bakeries that utilize isolated strains of instant baker's yeast, traditional sourdough relies on a wild symbiotic culture of wild yeasts and lactic acid bacteria. These microscopic organisms <strong>(8)</strong> _________ in a wet flour matrix, converting complex cereal starches into simple sugars and organic acids. The acetic and lactic acids produced during prolonged cool fermentation <strong>(9)</strong> _________ sourdough its characteristic tangy flavor while lowering dough pH. This acidic environment acts as a natural biological preservative, effectively <strong>(10)</strong> _________ mold germination and extending the loaf's shelf life. Furthermore, bacterial enzymatic activity breaks down gluten proteins, making sourdough significantly easier to <strong>(11)</strong> _________ for consumers with mild wheat <strong>(12)</strong> _________.",
            [
                (8, ["thrive", "prosper", "flourish", "bloom"], "A", "Biological Verb (B2)", "Organisms thrive in."),
                (9, ["give", "lend", "grant", "accord"], "A", "Collocation (B1-B2)", "Give sourdough its flavor."),
                (10, ["inhibiting", "halting", "stopping", "blocking"], "A", "Participial Phrase (B2)", "Inhibiting mold germination."),
                (11, ["digest", "ingest", "process", "consume"], "A", "Nutritional Lexis (B1-B2)", "Easier to digest."),
                (12, ["sensitivities", "allergies", "reactions", "ailments"], "A", "Medical Noun (B2)", "Wheat sensitivities.")
            ]
        ),
        (
            "The Preservation of Historical Textiles",
            "Conserving medieval ecclesiastical tapestries and silk vestments poses formidable biochemical challenges for museum restorers. Centuries of exposure to gallery light, atmospheric pollutants, and airborne dust cause fragile organic silk and wool fibers to <strong>(8)</strong> _________ and break. To halt further deterioration, conservators place garments on customized foam mounts that evenly <strong>(9)</strong> _________ physical strain across delicate seams. Microscopic vacuum nozzles are used to lift particulates without abrading woven yarns. Specialized LED luminaires that emit zero ultraviolet frequencies are installed to ensure that antique dyed threads do not <strong>(10)</strong> _________ into dull grey tones. Museum curators emphasize that preventive climate regulation remains far more <strong>(11)</strong> _________ than intrusive chemical consolidation <strong>(12)</strong> _________.",
            [
                (8, ["weaken", "falter", "soften", "dilute"], "A", "Material Verb (B2)", "Fibers weaken and break."),
                (9, ["distribute", "disperse", "scatter", "allocate"], "A", "Mechanical Lexis (B2)", "Distribute physical strain."),
                (10, ["fade", "wane", "bleach", "pale"], "A", "Color Lexis (B2)", "Dyed threads do not fade."),
                (11, ["effective", "potent", "efficient", "capable"], "A", "Evaluative Adjective (B2)", "Far more effective than."),
                (12, ["treatments", "remedies", "cures", "therapies"], "A", "Conservation Term (B2)", "Chemical consolidation treatments.")
            ]
        ),
        (
            "Geothermal Energy Extraction",
            "Harnessing geothermal energy represents one of the cleanest and most reliable baseload power technologies available to contemporary society. Unlike wind and photovoltaic solar installations that fluctuate <strong>(8)</strong> _________ weather conditions, deep geothermal reservoirs deliver continuous turbine generation three hundred and sixty-five days a year. Engineers drill production wells thousands of meters into subterranean volcanic formations, circulating pressurized cold water to <strong>(9)</strong> _________ thermal energy from fractured bedrock. When the superheated liquid returns to surface turbines, it flashes into steam, powering generators that supply the national electricity <strong>(10)</strong> _________. Geothermal development thus provides a steady <strong>(11)</strong> _________ for countries committed to decarbonizing their industrial energy <strong>(12)</strong> _________.",
            [
                (8, ["depending on", "counting on", "leaning on", "banking on"], "A", "Prepositional Phrase (B1-B2)", "Fluctuate depending on weather."),
                (9, ["extract", "draw", "harvest", "gather"], "A", "Technical Verb (B2)", "Extract thermal energy."),
                (10, ["grid", "network", "mesh", "lattice"], "A", "Electrical Infrastructure Noun (B2)", "Electricity grid."),
                (11, ["foundation", "groundwork", "basis", "cornerstone"], "A", "Metaphorical Collocation (B2)", "A steady foundation for."),
                (12, ["portfolio", "assortment", "collection", "bundle"], "A", "Commercial/Energy Collocation (B2)", "Industrial energy portfolio.")
            ]
        ),
        (
            "The Cognitive Benefits of Bilingualism",
            "For decades, educational theorists mistakenly believed that teaching children two languages simultaneously caused developmental delays and vocabulary confusion. Cognitive neuroscience has thoroughly <strong>(8)</strong> _________ this myth, demonstrating that bilingual individuals possess enhanced executive brain function. Managing two competing linguistic systems forces the prefrontal cortex to continuously <strong>(9)</strong> _________ between grammar rules, improving mental flexibility and working memory. Furthermore, neurological imaging studies demonstrate that lifelong bilingualism can <strong>(10)</strong> _________ the cognitive onset of dementia symptoms by up to five years. Far from being a cognitive burden, foreign language acquisition serves as a lifelong protective <strong>(11)</strong> _________ for mental <strong>(12)</strong> _________.",
            [
                (8, ["debunked", "dismissed", "denounced", "disowned"], "A", "Scholarly Lexis (B2-C1)", "Thoroughly debunked this myth."),
                (9, ["switch", "swap", "shift", "transfer"], "A", "Cognitive Verb (B2)", "Continuously switch between."),
                (10, ["delay", "postpone", "defer", "suspend"], "A", "Medical/Cognitive Lexis (B2)", "Delay the cognitive onset."),
                (11, ["buffer", "shield", "cushion", "screen"], "A", "Protective Noun (B2-C1)", "Lifelong protective buffer."),
                (12, ["vitality", "vigor", "stamina", "energy"], "A", "Health Register (B2)", "Mental vitality.")
            ]
        ),
        (
            "The History of the Printing Press",
            "Johannes Gutenberg's fifteenth-century development of movable metal type is widely acknowledged as one of the most transformative technological breakthroughs in human chronicle. Prior to Gutenberg's invention, books were copied by monastic scribes by hand, making volumes prohibitively expensive and <strong>(8)</strong> _________ accessible to the wealthy aristocratic elite. By combining durable lead alloy type sorts with oil-based ink and an adapted wooden grape press, Gutenberg enabled the rapid, uniform <strong>(9)</strong> _________ of texts. The resulting proliferation of printed pamphlets fueled the Protestant Reformation, catalyzed the Scientific Revolution, and democratized literacy across the European continent, forever <strong>(10)</strong> _________ the transmission of scholarly <strong>(11)</strong> _________ in Western <strong>(12)</strong> _________.",
            [
                (8, ["exclusively", "purely", "solely", "strictly"], "A", "Adverb Selection (B2)", "Exclusively accessible to."),
                (9, ["replication", "duplication", "reproduction", "cloning"], "A", "Print Lexis (B2)", "Uniform reproduction of texts."),
                (10, ["revolutionizing", "transforming", "modernizing", "shifting"], "A", "Participial Phrase (B2)", "Revolutionizing the transmission."),
                (11, ["knowledge", "wisdom", "intellect", "learning"], "A", "Noun Collocation (B2)", "Scholarly knowledge."),
                (12, ["civilization", "society", "culture", "community"], "A", "Broad Noun (B2)", "Western civilization.")
            ]
        ),
        (
            "Urban Wetland Biofiltration",
            "Civil engineering consultancies are ditching concrete stormwater culverts in favor of engineered biological wetlands to manage urban runoff. When heavy rainfall strikes paved parking lots, storm surges carry motor oils, dissolved heavy metals, and microplastic sediments into municipal waterways. In contrast, engineered biofiltration marshes utilize reed bed plantings and sand filtration layers that naturally <strong>(8)</strong> _________ and trap suspended particulate contaminants. Microbes dwelling on plant roots metabolize hydrocarbons, breaking down harmful industrial chemicals before filtered water <strong>(9)</strong> _________ into downstream rivers. Constructing ecological wetland swales also provides vital stopover habitats for migratory waterbirds, demonstrating how civil infrastructure can <strong>(10)</strong> _________ human engineering with ecological <strong>(11)</strong> _________ in urban <strong>(12)</strong> _________.",
            [
                (8, ["immobilize", "paralyze", "arrest", "freeze"], "A", "Technical Filtration Lexis (B2)", "Immobilize and trap contaminants."),
                (9, ["discharges", "releases", "emits", "expels"], "A", "Hydraulic Verb (B2)", "Water discharges into rivers."),
                (10, ["integrate", "combine", "amalgamate", "fuse"], "A", "Collocation (B2)", "Integrate engineering with."),
                (11, ["integrity", "purity", "wholeness", "soundness"], "A", "Ecological Noun (B2-C1)", "Ecological integrity."),
                (12, ["design", "architecture", "planning", "scheme"], "A", "Collocation (B2)", "In urban design.")
            ]
        ),
        (
            "The Psychology of Flow State",
            "Originally conceptualized by psychologist Mihaly Csikszentmihalyi, the 'flow state' refers to an optimal cognitive condition in which an individual becomes completely immersed in an activity with focused concentration. Experiencing flow requires an intricate equilibrium between the perceived difficulty of a task and the individual's personal <strong>(8)</strong> _________ to execute it. If the challenge surpasses capability, intense anxiety <strong>(9)</strong> _________; conversely, if the task is too simple, boredom quickly takes hold. When locked in authentic flow, individuals lose conscious awareness of physical time and self-doubt, leading to heightened productivity and intense creative <strong>(10)</strong> _________. Employers and educators are increasingly designing workplaces that foster uninterrupted focus to cultivate this valuable mental <strong>(11)</strong> _________ in everyday professional <strong>(12)</strong> _________.",
            [
                (8, ["competence", "capacity", "aptitude", "fitness"], "A", "Psychological Lexis (B2)", "Personal competence to execute."),
                (9, ["ensues", "follows", "results", "arises"], "A", "Formal Consequence Verb (B2)", "Anxiety ensues."),
                (10, ["fulfillment", "gratification", "satisfaction", "contentment"], "A", "Collocation (B2)", "Creative fulfillment."),
                (11, ["state", "phase", "condition", "mode"], "A", "Cognitive Noun (B1-B2)", "Valuable mental state."),
                (12, ["endeavors", "efforts", "enterprises", "ventures"], "A", "Formal Vocabulary (B2)", "Professional endeavors.")
            ]
        ),
        (
            "Ancient DNA Paleogenomics",
            "The emergence of high-throughput genetic sequencing technologies has unlocked an unprecedented window into prehistoric human migrations through the analysis of ancient DNA (aDNA). By extracting fragments of genomic material from fossilized tooth dentine and inner ear petrous bones preserved in deep cave vaults, paleogenomicists can reconstruct ancestral lineages that vanished millennia ago. However, working with ancient skeletal specimens requires extraordinary sterile <strong>(8)</strong> _________ to prevent modern laboratory airborne microbes from contaminating archaeological samples. Sophisticated computational algorithms must filter out post-mortem chemical degradation, allowing scientists to accurately <strong>(9)</strong> _________ ancient human migrations across continents. This revolutionary discipline has overturned longstanding archaeological orthodoxies, proving that human history was characterized by continuous intercontinental mobility and genetic <strong>(10)</strong> _________ across ancient human <strong>(11)</strong> _________ during prehistoric <strong>(12)</strong> _________.",
            [
                (8, ["precautions", "safeguards", "measures", "defenses"], "A", "Laboratory Lexis (B2)", "Sterile precautions."),
                (9, ["map", "chart", "plot", "trace"], "A", "Scientific Inquiry Verb (B2)", "Accurately map ancient migrations."),
                (10, ["exchange", "swap", "trade", "barter"], "A", "Anthropological Register (B2)", "Genetic exchange."),
                (11, ["populations", "communities", "settlements", "tribes"], "A", "Scientific Noun (B2)", "Ancient human populations."),
                (12, ["epochs", "periods", "eras", "times"], "A", "Chronological Noun (B2)", "Prehistoric epochs.")
            ]
        ),
        (
            "Marine Bioluminescence and Cancer Oncology",
            "Bioluminescent signaling mechanisms developed by deep-sea organisms for communication and predatory evasion are now spearheading breakthroughs in oncology laboratories. Biomedical researchers have isolated luciferin genes from marine coelenterates, <strong>(8)</strong> _________ them into engineered tumor models to monitor cellular growth in real time. Under high-sensitivity photon cameras, malignant cancer cells engineered with bioluminescent tags emit a faint green glow when metabolically active, allowing oncologists to <strong>(9)</strong> _________ the precise efficacy of experimental chemotherapy drugs without performing invasive surgical biopsies. This non-invasive tracking protocol dramatically reduces the timeline required to evaluate candidate oncology compounds, proving that natural biochemical adaptations evolved in deep abyssal trenches hold indispensable therapeutic <strong>(10)</strong> _________ for modern clinical <strong>(11)</strong> _________ in fighting malignant <strong>(12)</strong> _________.",
            [
                (8, ["inserting", "introducing", "injecting", "implanting"], "A", "Genetic Technology Lexis (B2)", "Inserting them into models."),
                (9, ["gauge", "meter", "scale", "rank"], "A", "Scientific Assessment Verb (B2)", "Gauge the precise efficacy."),
                (10, ["promise", "prospect", "potential", "hope"], "A", "Collocation (B2)", "Indispensable therapeutic promise."),
                (11, ["medicine", "practice", "treatment", "therapy"], "A", "Clinical Register (B2)", "Modern clinical medicine."),
                (12, ["diseases", "illnesses", "conditions", "disorders"], "A", "Medical Noun (B1-B2)", "Fighting malignant diseases.")
            ]
        )
    ]
]
