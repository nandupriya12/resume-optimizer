def tailor_resume(resume_text, job_desc, missing_skills):
    improved = resume_text

    if missing_skills:
        improved += "\n\n--- Improved Section ---\n"
        improved += "Add these skills:\n"

        for skill in missing_skills:
            improved += f"- {skill}\n"

    return improved