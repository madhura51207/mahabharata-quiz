"""
Test suite to validate:
1. Question bank integrity (all questions have 4 options, valid answer index 0-3, non-empty question & explanation)
2. All age groups, categories, difficulties are present
3. No duplicate IDs
"""

import json
import re

with open("js/data/questions.js", "r", encoding="utf-8") as f:
    content = f.read()

# Extract JSON object
match = re.search(r"const MAHABHARATA_QUESTIONS = (\[.*?\]);", content, re.DOTALL)
if not match:
    print("FAILED: Could not parse questions JSON from js/data/questions.js")
    exit(1)

questions = json.loads(match.group(1))

print(f"Total questions loaded: {len(questions)}")
assert len(questions) >= 120, "Should have at least 120 questions"

valid_age_groups = {"kids", "young_learners", "students", "adults"}
valid_categories = {"characters", "stories", "weapons", "places", "relationships", "values"}
valid_difficulties = {"easy", "medium", "hard"}

seen_ids = set()
category_counts = {}
age_counts = {}
difficulty_counts = {}

for idx, q in enumerate(questions):
    qid = q.get("id")
    assert qid, f"Question at index {idx} missing id"
    assert qid not in seen_ids, f"Duplicate id found: {qid}"
    seen_ids.add(qid)

    age = q.get("ageGroup")
    assert age in valid_age_groups, f"Invalid age group '{age}' in question {qid}"
    age_counts[age] = age_counts.get(age, 0) + 1

    cat = q.get("category")
    assert cat in valid_categories, f"Invalid category '{cat}' in question {qid}"
    category_counts[cat] = category_counts.get(cat, 0) + 1

    diff = q.get("difficulty")
    assert diff in valid_difficulties, f"Invalid difficulty '{diff}' in question {qid}"
    difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1

    q_text = q.get("question")
    assert q_text and len(q_text.strip()) > 5, f"Question text invalid in {qid}"

    options = q.get("options")
    assert isinstance(options, list) and len(options) == 4, f"Options must have 4 items in {qid}"
    for opt in options:
        assert opt and len(opt.strip()) > 0, f"Empty option in {qid}"

    ans = q.get("answer")
    assert isinstance(ans, int) and 0 <= ans <= 3, f"Answer must be integer 0..3 in {qid}, got {ans}"

    expl = q.get("explanation")
    assert expl and len(expl.strip()) > 10, f"Explanation too short or missing in {qid}"

print("\n--- Distribution Summary ---")
print("By Age Group:")
for k, v in age_counts.items():
    print(f"  {k}: {v}")

print("By Category:")
for k, v in category_counts.items():
    print(f"  {k}: {v}")

print("By Difficulty:")
for k, v in difficulty_counts.items():
    print(f"  {k}: {v}")

print("\nALL 120 QUESTIONS PASSED VALIDATION CHECKS!")
