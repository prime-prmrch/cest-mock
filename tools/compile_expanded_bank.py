#!/usr/bin/env python3
"""
Compile expanded item bank for Cambridge English Skills Test (CEST) simulator.
Merges expansion modules to ensure exactly 25 distinct variations per task key across all subtests.
"""
import json
import os
import sys

# Ensure tools directory is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bank_expansions import writing_tasks
from bank_expansions import reading_tasks_1_to_4
from bank_expansions import reading_tasks_5_to_9
from bank_expansions import listening_tasks

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    bank_path = os.path.join(repo_root, "data", "bank.json")

    print(f"Loading base bank from {bank_path}...")
    with open(bank_path, "r", encoding="utf-8") as f:
        bank = json.load(f)

    # 1. Expand Writing Tasks (base 8 -> 25 each)
    print("Expanding Writing tasks...")
    if len(bank["writing"]["task_1_narrative"]) < 25:
        needed = 25 - len(bank["writing"]["task_1_narrative"])
        bank["writing"]["task_1_narrative"].extend(writing_tasks.TASK_1_EXPANSIONS[:needed])
    if len(bank["writing"]["task_2_discursive"]) < 25:
        needed = 25 - len(bank["writing"]["task_2_discursive"])
        bank["writing"]["task_2_discursive"].extend(writing_tasks.TASK_2_EXPANSIONS[:needed])

    # 2. Expand Reading Tasks 1-4 (base 5 -> 25 each)
    print("Expanding Reading tasks 1-4...")
    if len(bank["reading"]["task_1_notices"]) < 25:
        needed = 25 - len(bank["reading"]["task_1_notices"])
        bank["reading"]["task_1_notices"].extend(reading_tasks_1_to_4.TASK_1_EXPANSIONS[:needed])
    if len(bank["reading"]["task_2_sentence_cloze"]) < 25:
        needed = 25 - len(bank["reading"]["task_2_sentence_cloze"])
        bank["reading"]["task_2_sentence_cloze"].extend(reading_tasks_1_to_4.TASK_2_EXPANSIONS[:needed])
    if len(bank["reading"]["task_3_open_cloze"]) < 25:
        needed = 25 - len(bank["reading"]["task_3_open_cloze"])
        bank["reading"]["task_3_open_cloze"].extend(reading_tasks_1_to_4.TASK_3_EXPANSIONS[:needed])
    if len(bank["reading"]["task_4_vocab_cloze"]) < 25:
        needed = 25 - len(bank["reading"]["task_4_vocab_cloze"])
        bank["reading"]["task_4_vocab_cloze"].extend(reading_tasks_1_to_4.TASK_4_EXPANSIONS[:needed])

    # 3. Expand Reading Tasks 5-9 (base 5 -> 25 each)
    print("Expanding Reading tasks 5-9...")
    if len(bank["reading"]["task_5_extended_text"]) < 25:
        needed = 25 - len(bank["reading"]["task_5_extended_text"])
        bank["reading"]["task_5_extended_text"].extend(reading_tasks_5_to_9.TASK_5_EXPANSIONS[:needed])
    if len(bank["reading"]["task_6_short_article"]) < 25:
        needed = 25 - len(bank["reading"]["task_6_short_article"])
        bank["reading"]["task_6_short_article"].extend(reading_tasks_5_to_9.TASK_6_EXPANSIONS[:needed])
    if len(bank["reading"]["task_7_gapped_sentences"]) < 25:
        needed = 25 - len(bank["reading"]["task_7_gapped_sentences"])
        bank["reading"]["task_7_gapped_sentences"].extend(reading_tasks_5_to_9.TASK_7_EXPANSIONS[:needed])
    if len(bank["reading"]["task_8_gapped_paragraphs"]) < 25:
        needed = 25 - len(bank["reading"]["task_8_gapped_paragraphs"])
        bank["reading"]["task_8_gapped_paragraphs"].extend(reading_tasks_5_to_9.TASK_8_EXPANSIONS[:needed])
    if len(bank["reading"]["task_9_multiple_matching"]) < 25:
        needed = 25 - len(bank["reading"]["task_9_multiple_matching"])
        bank["reading"]["task_9_multiple_matching"].extend(reading_tasks_5_to_9.TASK_9_EXPANSIONS[:needed])

    # 4. Expand Listening Tasks 1-6 (base 5 -> 25 each)
    print("Expanding Listening tasks 1-6...")
    if len(bank["listening"]["task_1_short_dialogue_1"]) < 25:
        needed = 25 - len(bank["listening"]["task_1_short_dialogue_1"])
        bank["listening"]["task_1_short_dialogue_1"].extend(listening_tasks.TASK_1_EXPANSIONS[:needed])
    if len(bank["listening"]["task_2_short_dialogue_2"]) < 25:
        needed = 25 - len(bank["listening"]["task_2_short_dialogue_2"])
        bank["listening"]["task_2_short_dialogue_2"].extend(listening_tasks.TASK_2_EXPANSIONS[:needed])
    if len(bank["listening"]["task_3_extended_interview"]) < 25:
        needed = 25 - len(bank["listening"]["task_3_extended_interview"])
        bank["listening"]["task_3_extended_interview"].extend(listening_tasks.TASK_3_EXPANSIONS[:needed])
    if len(bank["listening"]["task_4_discussion"]) < 25:
        needed = 25 - len(bank["listening"]["task_4_discussion"])
        bank["listening"]["task_4_discussion"].extend(listening_tasks.TASK_4_EXPANSIONS[:needed])
    if len(bank["listening"]["task_5_multiple_matching"]) < 25:
        needed = 25 - len(bank["listening"]["task_5_multiple_matching"])
        bank["listening"]["task_5_multiple_matching"].extend(listening_tasks.TASK_5_EXPANSIONS[:needed])
    if len(bank["listening"]["task_6_monologue_gaps"]) < 25:
        needed = 25 - len(bank["listening"]["task_6_monologue_gaps"])
        bank["listening"]["task_6_monologue_gaps"].extend(listening_tasks.TASK_6_EXPANSIONS[:needed])

    # 5. Verification: Audit all 17 keys
    print("\n--- Auditing Expanded Item Bank Counts ---")
    total_items = 0
    subtest_keys = [
        ("reading", "task_1_notices"),
        ("reading", "task_2_sentence_cloze"),
        ("reading", "task_3_open_cloze"),
        ("reading", "task_4_vocab_cloze"),
        ("reading", "task_5_extended_text"),
        ("reading", "task_6_short_article"),
        ("reading", "task_7_gapped_sentences"),
        ("reading", "task_8_gapped_paragraphs"),
        ("reading", "task_9_multiple_matching"),
        ("listening", "task_1_short_dialogue_1"),
        ("listening", "task_2_short_dialogue_2"),
        ("listening", "task_3_extended_interview"),
        ("listening", "task_4_discussion"),
        ("listening", "task_5_multiple_matching"),
        ("listening", "task_6_monologue_gaps"),
        ("writing", "task_1_narrative"),
        ("writing", "task_2_discursive"),
    ]

    for subtest, key in subtest_keys:
        count = len(bank[subtest][key])
        total_items += count
        print(f"  [{subtest.upper()}] {key:30s}: {count:2d} variations")
        assert count == 25, f"Validation failure: {subtest}.{key} has {count} items, expected 25!"

    print(f"\nAll 17 tasks successfully validated with exactly 25 variations each (Total items: {total_items})!")

    # 6. Save back to data/bank.json
    print(f"Saving compiled bank to {bank_path}...")
    with open(bank_path, "w", encoding="utf-8") as f:
        json.dump(bank, f, indent=2, ensure_ascii=False)
    print("Done! bank.json successfully updated.")

if __name__ == "__main__":
    main()
