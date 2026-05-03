import re

SKILL_KEYWORDS = [
    "communication", "english", "teaching", "lesson planning",
    "grammar", "vocabulary", "student management", "tefl",
    "presentation", "training", "mentoring"
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    return text

def extract_skills(text):
    text = clean_text(text)
    found_skills = []

    for skill in SKILL_KEYWORDS:
        if skill in text:
            found_skills.append(skill)

    return set(found_skills)

def skill_gap_analysis(resume_text, jd_text):
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    missing_skills = jd_skills - resume_skills
    matched_skills = jd_skills & resume_skills

    return list(matched_skills), list(missing_skills)