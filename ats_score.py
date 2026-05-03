import re

def clean_words(text):
    text = text.lower()
    words = re.findall(r'\b[a-z]+\b', text)  # removes punctuation
    stopwords = {
        "and", "or", "the", "is", "a", "an", "to", "of", "in", "for", "on", "with"
    }
    return set([word for word in words if word not in stopwords])


def ats_score(resume_text, job_desc):
    resume_words = clean_words(resume_text)
    jd_words = clean_words(job_desc)

    matched = resume_words.intersection(jd_words)

    if len(jd_words) == 0:
        return 0, []

    score = (len(matched) / len(jd_words)) * 100

    return round(score, 2), list(matched)