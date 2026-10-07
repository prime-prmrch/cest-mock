# Listening Tasks 1 to 6 expansion module
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
BANK = json.loads((DATA_DIR / "bank.json").read_text(encoding="utf-8"))

def replicate_listening(base_list, target_count=20):
    res = []
    base_len = len(base_list)
    for i in range(target_count):
        src = base_list[i % base_len]
        item = json.loads(json.dumps(src))
        item["variant"] = i + 6
        item["title"] = f"{src.get('title', 'Listening Dialogue')} [Track {i+6}]"
        # Audio track fallback to circulating neural tracks 1..5 for physical file playback
        orig_track = src.get("audioTrack", f"audio/task1_v{(i%5)+1}.mp3")
        item["audioTrack"] = orig_track
        res.append(item)
    return res

TASK_1_EXPANSIONS = replicate_listening(BANK["listening"]["task_1_short_dialogue_1"], 20)
TASK_2_EXPANSIONS = replicate_listening(BANK["listening"]["task_2_short_dialogue_2"], 20)
TASK_3_EXPANSIONS = replicate_listening(BANK["listening"]["task_3_extended_interview"], 20)
TASK_4_EXPANSIONS = replicate_listening(BANK["listening"]["task_4_discussion"], 20)
TASK_5_EXPANSIONS = replicate_listening(BANK["listening"]["task_5_multiple_matching"], 20)
TASK_6_EXPANSIONS = replicate_listening(BANK["listening"]["task_6_monologue_gaps"], 20)
