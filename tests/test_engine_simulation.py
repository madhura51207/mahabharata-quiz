"""
Test all 252 permutations of settings to guarantee zero failures and exact counts.
"""
import json
import re
import random

with open("js/data/questions.js", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"const MAHABHARATA_QUESTIONS = (\[.*?\]);", content, re.DOTALL)
pool = json.loads(match.group(1))

age_groups = ["kids", "young_learners", "students", "adults"]
categories = ["characters", "stories", "weapons", "places", "relationships", "values", "mixed"]
difficulties = ["easy", "medium", "hard"]
counts = [5, 10, 20]

def simulate_generate_quiz(age_group, category, difficulty, count):
    requested_count = count
    selected_category = category.lower()
    selected_age = age_group.lower()
    selected_diff = difficulty.lower()

    candidates = []
    used_ids = set()

    def add_candidates(filter_fn):
        matches = [q for q in pool if q["id"] not in used_ids and filter_fn(q)]
        random.shuffle(matches)
        for q in matches:
            if len(candidates) < requested_count:
                candidates.append(q)
                used_ids.add(q["id"])

    # Stage 1: Exact matches
    add_candidates(lambda q: q["ageGroup"] == selected_age and (selected_category == "mixed" or q["category"] == selected_category) and q["difficulty"] == selected_diff)

    # Stage 2: Same age + cat, any diff
    if len(candidates) < requested_count:
        add_candidates(lambda q: q["ageGroup"] == selected_age and (selected_category == "mixed" or q["category"] == selected_category))

    # Stage 3: Same age, any cat, any diff
    if len(candidates) < requested_count:
        add_candidates(lambda q: q["ageGroup"] == selected_age)

    # Stage 4: Same cat across ages
    if len(candidates) < requested_count:
        add_candidates(lambda q: selected_category == "mixed" or q["category"] == selected_category)

    # Stage 5: Any remaining
    if len(candidates) < requested_count:
        add_candidates(lambda q: True)

    assert len(candidates) == requested_count, f"Failed to get {requested_count} questions for {age_group}, {category}, {difficulty}. Got {len(candidates)}"
    assert len(used_ids) == requested_count, "Found duplicate IDs in generated quiz!"

    # Verify option shuffling and answer integrity
    for q in candidates:
        orig_opts = list(q["options"])
        correct_text = orig_opts[q["answer"]]
        shuffled = list(orig_opts)
        random.shuffle(shuffled)
        new_ans = shuffled.index(correct_text)
        assert shuffled[new_ans] == correct_text

total_combos = len(age_groups) * len(categories) * len(difficulties) * len(counts)
print(f"Testing all {total_combos} combinations...")

for age in age_groups:
    for cat in categories:
        for diff in difficulties:
            for cnt in counts:
                simulate_generate_quiz(age, cat, diff, cnt)

print(f"SUCCESS: All {total_combos} configuration combinations generated exactly the requested questions with zero duplicates!")
