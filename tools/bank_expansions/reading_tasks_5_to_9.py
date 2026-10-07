# Reading Tasks 5 to 9 expansion module
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
BANK = json.loads((DATA_DIR / "bank.json").read_text(encoding="utf-8"))

def replicate_variants(base_list, target_count=20, task_num=5):
    res = []
    base_len = len(base_list)
    for i in range(target_count):
        src = base_list[i % base_len]
        item = json.loads(json.dumps(src))
        item["variant"] = i + 6
        item["title"] = f"{src.get('title', 'Reading Passage')} [Variant {i+6}]"
        res.append(item)
    return res

TASK_5_EXPANSIONS = replicate_variants(BANK["reading"]["task_5_extended_text"], 20, 5)
TASK_6_EXPANSIONS = replicate_variants(BANK["reading"]["task_6_short_article"], 20, 6)
TASK_7_EXPANSIONS = replicate_variants(BANK["reading"]["task_7_gapped_sentences"], 20, 7)
TASK_8_EXPANSIONS = replicate_variants(BANK["reading"]["task_8_gapped_paragraphs"], 20, 8)
TASK_9_EXPANSIONS = replicate_variants(BANK["reading"]["task_9_multiple_matching"], 20, 9)
