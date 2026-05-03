def ats_score(resume_text, job_desc):
    resume_words = set(resume_text.lower().split())
    jd_words = set(job_desc.lower().split())

    matched = resume_words.intersection(jd_words)

    if len(jd_words) == 0:
        return 0, []

    score = (len(matched) / len(jd_words)) * 100

    return round(score, 2), list(matched)