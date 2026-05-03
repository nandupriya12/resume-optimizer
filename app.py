import streamlit as st
from resume_parser import extract_text
from ats_score import ats_score
from skill_gap import skill_gap_analysis
from resume_tailor import tailor_resume

st.title("🚀 AI Resume Optimizer")

file = st.file_uploader("Upload Resume (PDF)")
job_desc = st.text_area("Paste Job Description")

if file and job_desc:
    resume_text = extract_text(file)

    if not resume_text:
        st.error("Could not read PDF properly")
        st.stop()

    with st.spinner("Analyzing resume..."):
        score, keywords = ats_score(resume_text, job_desc)
        matched, missing = skill_gap_analysis(resume_text, job_desc)

    # 🎯 ATS SCORE
    st.subheader(f"ATS Score: {score}%")
    st.progress(min(score / 100, 1.0))

    if score > 75:
        st.success("Strong match ✅")
    elif score > 50:
        st.warning("Average match ⚠️")
    else:
        st.error("Low match ❌ Improve your resume")

    # ✅ MATCHED KEYWORDS
    st.subheader("✅ Matched Keywords")
    if keywords:
        for k in keywords:
            if len(k) > 2:
                st.success(k)
    else:
        st.warning("No keywords matched")

    # ❌ MISSING SKILLS
    st.subheader("❌ Missing Skills")
    if missing:
        st.write(", ".join(missing))
    else:
        st.success("No missing skills")

    # 📊 SKILL GAP
    st.subheader("📊 Skill Gap Analysis")
    st.warning(f"You are missing {len(missing)} important skills")

    # ✨ SUGGESTIONS
    st.subheader("✨ Suggestions")

    if missing:
        st.write("Add these skills:")
        for skill in missing:
            st.write(f"- {skill}")

    st.write("- Use strong action verbs (developed, designed, led)")
    st.write("- Add measurable achievements")
    st.write("- Tailor resume based on job description")

    # 📄 TAILORED RESUME
    st.subheader("📄 Tailored Resume")

    if "improved_resume" not in st.session_state:
        st.session_state.improved_resume = ""

    if st.button("Generate Improved Resume"):
        st.session_state.improved_resume = tailor_resume(resume_text, job_desc, missing)

    if st.session_state.improved_resume:
        st.text_area("Improved Resume", st.session_state.improved_resume, height=300)