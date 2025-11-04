import streamlit as st
from PIL import Image
import base64
import smtplib
from email.mime.text import MIMEText
import streamlit as st
def send_email(name, sender_email, message):
    gmail_user = "akhillade431@gmail.com"
    gmail_password = "obth uwfi ahfn ptoe"  # from Google App Password
    receiver_email = "akhillade431@gmail.com"  # same as your Gmail

    subject = f"New Contact from {name}"
    body = f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(gmail_user, gmail_password)
            server.send_message(msg)
        return True
    except Exception as e:
        print("❌ Email sending error:", e)
        return False


# -------------------------------
# 🎯 BASIC INFO
# -------------------------------
NAME = "Akhil Lade"
ROLE = "Machine Learning Engineer | AI Enthusiast"
EMAIL = "akhillade431@gmail.com"
PHONE = "+91 9392032795"
LINKEDIN = "https://linkedin.com/in/akhillade"
GITHUB = "https://github.com/akhillade"
RESUME_LINK = "Akhil lade.pdf"
TWITTER = "https://x.com/LadeAkhi5222?t=-mQ6xE2xWb9Xs4LnDFALKg&s=09"


ABOUT_ME = """
Hi! I'm **Akhil Lade**, a passionate Machine Learning Engineer with a strong interest in **AI, Data Science, and full-stack development**.
I enjoy building intelligent systems, clean web apps, and solving real-world problems using data-driven approaches.
In my free time, I explore emerging technologies, contribute to open-source, and believe in **continuous learning** and **practical innovation**.
"""
st.subheader("💼 Professional Summary")
st.write("""
Machine Learning Engineer with hands-on experience in developing deep learning models,
building web applications with Flask and Streamlit.
Strong foundation in Python, Data Structures, and AI research applications.
""")


CAREER_OBJECTIVE = """
To work in a challenging and dynamic environment where I can utilize my technical and analytical skills
to contribute effectively towards the growth of the organization while constantly learning and improving.
"""

TECH_STRENGTHS = [
    "Strong problem-solving and debugging skills",
    "Good understanding of OOP concepts and algorithms",
    "Experience with Machine Learning model training and optimization",
    "Ability to work in a team and communicate effectively",
    "Eager to learn and adapt to new technologies quickly"
]

LANGUAGES = ["English", "Telugu", "Hindi"]
HOBBIES = ["Exploring AI tools", "Coding projects", "Learning new tech", "Listening to music"]

ACHIEVEMENTS = [
    "🏆 Developed an Animal Footprint Classifier using CNN, SVM & Random Forest.",
    "📊 Built an end-to-end Machine Learning pipeline for predictive analytics.",
    "💡 Created multiple interactive Streamlit apps for data visualization.",
    "🎓 Earned certifications in Machine Learning and Deep Learning (Coursera).",
    "🤝 Participated in hackathons and won awards for innovation and teamwork."
]

PROJECTS = [

    {
        "title": "🐾 Tiger vs Lion Footprint Classifier",
        "description": "Developed a CNN-based image classifier achieving **95% accuracy** in distinguishing tiger vs lion footprints. Added Random Forest and SVM models for hybrid comparison.",
        "tech": "Python, TensorFlow, Streamlit, Scikit-learn",
        "link": "https://github.com/akill10/Tiger-vs-Lion-Foot-print-classifier.git"
    },
    {
        "title": "📈 Bitcoin Price Prediction",
        "description": "Built an LSTM-based predictive model to forecast Bitcoin price movement with **real-time sentiment integration** using Twitter data.",
        "tech": "Python, Pandas, Sklearn, LSTM",
        "link": "https://github.com/akill10/Bitcoin-price-prediction-using-ML.git"
    }
]



SKILLS = {
    "Python": 90,
    "Machine Learning": 85,
    "C++ / Java": 80,
    "Data Analysis": 75,
    "Web Development": 70,
    "Deep Learning": 65,
}

EDUCATION = [
    {"degree": "B.Tech in Computer Science and Engineering", "institution": "Chaitanya Deemed to be University", "year": "2022–2026"},
    {"degree": "Intermediate (MPC)", "institution": "Sri Vikas Junior College", "year": "2020–2022"},
    {"degree": "10th (SSC)", "institution": "TS Residential School, Velair", "year": "2019–2020"},
]

CERTIFICATIONS = [
    "✅ Java Foundations (IBM SkillsBuild)",
    "✅ Deep Learning Specialization (Coursera)",
    "✅ Python Foundations (IBM SkillsBuild)",
    "✅ Python for Everybody (University of Michigan)"
]

EXPERIENCE = [
    {
        "role": "Talent Acquisition Trainee Intern",
        "company": "Dijit program(Remote)",
        "year": "Sept 2025 – Feb 2026",
        "details": "Worked as an intern in Dijit program."
    }
]

# -------------------------------
# 🎨 PAGE SETUP
# -------------------------------
st.set_page_config(page_title=f"{NAME} | Portfolio", page_icon="💼", layout="wide")
# 🌙 --- DARK MODE TOGGLE (with Smooth Transition) ---
st.sidebar.title("")
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)

# Define smooth transition and dark/light themes
base_css = """
<style>
html, body, .stApp {
    transition: background-color 0.6s ease, color 0.6s ease;
}
div[data-testid="stSidebar"] {
    transition: background-color 0.6s ease, color 0.6s ease;
}
</style>
"""

dark_css = """
<style>
body, .stApp {
    background-color: #0e1117;
    color: white;
}
div[data-testid="stSidebar"] {
    background-color: #1b1f24;
    color: white;
}
</style>
"""

light_css = """
<style>
body, .stApp {
    background-color: #f8f9fa;
    color: #000;
}
div[data-testid="stSidebar"] {
    background-color: #ffffff;
    color: #000;
}
</style>
"""

# Apply base transition CSS
st.markdown(base_css, unsafe_allow_html=True)

# Apply chosen theme
if dark_mode:
    st.markdown(dark_css, unsafe_allow_html=True)
else:
    st.markdown(light_css, unsafe_allow_html=True)
    # Apply chosen theme to <body> for CSS variable updates
theme_class = "dark" if dark_mode else "light"
st.markdown(f"<body data-theme='{theme_class}'>", unsafe_allow_html=True)



# -------------------------------
# 💅 STYLES (Enhanced UI)
# -------------------------------
st.markdown("""
<style>
/* 🌗 Dark/Light Mode */
:root {
  --bg-color: #ffffff;
  --text-color: #1b3b6f;
}
[data-theme="dark"] {
  --bg-color: #0d1117;
  --text-color: #e6edf3;
}
html, body {
  background-color: var(--bg-color);
  color: var(--text-color);
}

section.main h1::after, 
section.main h2::after {
    content: "";
    display: block;
    width: 80px;
    height: 4px;
    margin-top: 6px;
    border-radius: 2px;
    background: linear-gradient(90deg, #2196f3, #21cbf3);
}


}
section {
    background: white;
    padding: 25px;
    margin: 20px 0;
    border-radius: 16px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
    transition: transform 0.3s ease;
}
section:hover {
    transform: scale(1.01);
}
.skill-bar {
    height: 12px;
    background-color: #e3f2fd;
    border-radius: 10px;
    margin-bottom: 10px;
    overflow: hidden;
}
.skill-fill {
    height: 12px;
    background: linear-gradient(90deg, #2196f3, #21cbf3);
    border-radius: 10px;
    animation: fillAnim 2s ease-in-out forwards;
}
@keyframes fillAnim {
    from { width: 0; }
    to { width: var(--percent); }
}
.circular-img {
    width: 180px;
    height: 180px;
    border-radius: 50%;
    object-fit: cover;
    display: block;
    margin-left: auto;
    margin-right: auto;
    border: 4px solid #2196f3;
    box-shadow: 0 0 20px rgba(33,150,243,0.4);
}
.sidebar .stMarkdown {
    text-align: center;
}
.project-card {
    background: #f8f9fa;
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 10px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
}
.project-card:hover {
    background: #eef7ff;
    box-shadow: 0px 4px 12px rgba(33,150,243,0.2);
}
a {
    color: #1565c0 !important;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
.footer {
    text-align: center;
    margin-top: 40px;
    padding: 15px;
    border-radius: 12px;
    background: linear-gradient(90deg, #f6d365, #fda085);
    color: white;
    font-size: 15px;
    font-weight: 500;
}
</style>
<style>
/* Increase sidebar width */
section[data-testid="stSidebar"] {
    width: 285px !important;      /* default ~300px — increase slightly */
}
</style>

""", unsafe_allow_html=True)

# -------------------------------
# 🏠 SIDEBAR PROFILE
# -------------------------------
with st.sidebar:
    with open("profile.jpg", "rb") as img_file:
        img_bytes = img_file.read()
        img_base64 = base64.b64encode(img_bytes).decode()
        
    st.markdown(f"<img src='data:image/png;base64,{img_base64}' class='circular-img'>", unsafe_allow_html=True)
    st.title(NAME)
    st.markdown(f"<p style='text-align:center; font-size:16px; color:gray;'>{ROLE}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='white-space:nowrap; display:flex; align-items:center;'>📧&nbsp;<a href='mailto:{EMAIL}' style='text-decoration:none; color:inherit;'>{EMAIL}</a></p>", unsafe_allow_html=True)
    st.markdown(f"🔗 [LinkedIn]({LINKEDIN})")
    st.markdown(f"🐙 [GitHub]({GITHUB})")
    st.markdown(f"📱 {PHONE}")
    if RESUME_LINK:
        with open(RESUME_LINK, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button("📄 Download Resume", data=PDFbyte, file_name="Akhil_Lade_Resume.pdf")

# -------------------------------
# 🧍 ABOUT ME
# -------------------------------
st.markdown("<section>", unsafe_allow_html=True)
st.title(" About Me")
st.write(ABOUT_ME)
st.markdown("</section>", unsafe_allow_html=True)

# -------------------------------
# 🎯 CAREER OBJECTIVE
# -------------------------------
st.markdown("<section>", unsafe_allow_html=True)
st.header("Career Objective")
st.write(CAREER_OBJECTIVE)
st.markdown("</section>", unsafe_allow_html=True)

# -------------------------------
# 💪 TECHNICAL STRENGTHS
# -------------------------------
st.markdown("<section>", unsafe_allow_html=True)
st.header("Technical Strengths")
for s in TECH_STRENGTHS:
    st.markdown(f"- {s}")
st.markdown("</section>", unsafe_allow_html=True)

# -------------------------------
# 🧠 SKILLS
# -------------------------------
st.markdown("<section>", unsafe_allow_html=True)
st.header("Skills Overview")
for skill, percent in SKILLS.items():
    st.markdown(f"**{skill}**")
    st.markdown(f"<div class='skill-bar'><div class='skill-fill' style='--percent:{percent}%; width:{percent}%;'></div></div>", unsafe_allow_html=True)
st.markdown("</section>", unsafe_allow_html=True)

# -------------------------------
# 💼 EXPERIENCE
# -------------------------------
st.markdown("<section>", unsafe_allow_html=True)
st.header("Experience")
for exp in EXPERIENCE:
    st.markdown(f"**{exp['role']}** — *{exp['company']}* ({exp['year']})")
    st.write(exp["details"])
st.markdown("</section>", unsafe_allow_html=True)

# -------------------------------
# 🎓 EDUCATION
# -------------------------------
st.markdown("<section>", unsafe_allow_html=True)
st.header("🎓 Education")
for edu in EDUCATION:
    st.markdown(f"**{edu['degree']}** — {edu['institution']} ({edu['year']})")
st.markdown("</section>", unsafe_allow_html=True)

# -------------------------------
# 🏆 ACHIEVEMENTS
# -------------------------------
st.markdown("<section>", unsafe_allow_html=True)
st.header("🏆 Achievements")
for ach in ACHIEVEMENTS:
    st.markdown(f"- {ach}")
st.markdown("</section>", unsafe_allow_html=True)

# -------------------------------
# 💻 PROJECTS
# -------------------------------
st.markdown("<section>", unsafe_allow_html=True)
st.header("💻 Projects")
for proj in PROJECTS:
    st.markdown(f"<div class='project-card'><h4>{proj['title']}</h4><p>{proj['description']}</p><b>Tech Used:</b> {proj['tech']}<br><a href='{proj['link']}' target='_blank'>🔗 View Project</a></div>", unsafe_allow_html=True)
st.markdown("</section>", unsafe_allow_html=True)

# -------------------------------
# 📜 CERTIFICATIONS
# -------------------------------
st.markdown("<section>", unsafe_allow_html=True)
st.header("📜 Certifications")
for cert in CERTIFICATIONS:
    st.markdown(f"- {cert}")
st.markdown("</section>", unsafe_allow_html=True)

# -------------------------------
# 🌐 EXTRA INFO
# -------------------------------
st.markdown("<section>", unsafe_allow_html=True)
st.header(" Languages & Hobbies")
col1, col2 = st.columns(2)
with col1:
    st.markdown("###  Languages Known")
    for lang in LANGUAGES:
        st.markdown(f"- {lang}")
with col2:
    st.markdown("###  Hobbies & Interests")
    for hobby in HOBBIES:
        st.markdown(f"- {hobby}")
st.markdown("<section>", unsafe_allow_html=True)
st.header("📩 Contact Me")

with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send Message")

    if submitted:
        if name and email and message:
            success = send_email(name, email, message)
            if success:
                st.success("✅ Message sent successfully! I'll get back to you soon.")
            #else:
             #   st.error("❌ Something went wrong. Please try again later.")
        else:
            st.warning("⚠️ Please fill out all fields before sending.")

st.markdown("</section>", unsafe_allow_html=True)



# -------------------------------
# 🌟 FOOTER
# -------------------------------

# -------------------------------
st.markdown(f"""
<div style="text-align:center; margin-bottom:15px;">
    <a href="{LINKEDIN}" target="_blank" style="margin-right:25px; text-decoration:none;">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="35" style="vertical-align:middle;">
    </a>
    <a href="{GITHUB}" target="_blank" style="margin-right:25px; text-decoration:none;">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="35" style="vertical-align:middle;">
    </a>
    <a href="{TWITTER}" target="_blank" style="text-decoration:none;">
        <img src="https://cdn-icons-png.flaticon.com/512/733/733579.png" width="35" style="vertical-align:middle;">
    </a>
</div>

<div class="footer" style="text-align:center; font-size:15px; color:#555;">
    Developed with ❤️ by {NAME} | © 2025 All Rights Reserved
    <div style="font-size:13px; color:#777; margin-top:4px;">
        “Transforming AI ideas into real-world impact.”
    </div>
</div>
""", unsafe_allow_html=True)



