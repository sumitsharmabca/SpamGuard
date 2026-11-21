import streamlit as st
import joblib
import re

# ==========================================
# 1. LOAD TRAINED MODEL
# ==========================================

model = joblib.load("spam_classifier.pkl")


# ==========================================
# 2. TEXT CLEANING
# ==========================================

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# ==========================================
# 3. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="SpamGuard | SMS Detector",
    page_icon="🛡️",
    layout="wide"
)


# ==========================================
# 4. CUSTOM CSS DESIGN
# ==========================================

st.markdown("""
<style>

/* Streamlit top navigation bar */
header[data-testid="stHeader"] {
    background: #101827 !important;
    border-bottom: 1px solid #344a65;
    height: 55px;
}

/* App name on the top-left */
header[data-testid="stHeader"]::before {
    content: "SPAMGUARD | SMS DETECTOR";
    position: absolute;
    left: 20px;
    top: 15px;
    color: #7dc3ff;
    font-size: 17px;
    font-weight: 800;
    letter-spacing: 1px;
    pointer-events: none;
    z-index: 999;
}

/* Main background */
.stApp {
    background: linear-gradient(135deg, #101827, #172b46);
    color: white;
}

/* Page spacing */
.block-container {
    max-width: 1100px;
    padding-top: 0.5rem !important;
}

/* Hide white header background */
header[data-testid="stHeader"] {
    background: #101827 !important;
}

/* Continuous horizontal scrolling */
.ticker {
    width: 100%;
    overflow: hidden;
    background: #101827;
    border-bottom: 1px solid #344a65;
    padding: 12px 0;
    margin-bottom: 15px;
}

.ticker-track {
    display: flex;
    width: max-content;
    animation: tickerMove 22s linear infinite;
}

.ticker-content {
    white-space: nowrap;
    padding-right: 50px;
    color: #7dc3ff;
    font-size: 17px;
    font-weight: bold;
}

.ticker:hover .ticker-track {
    animation-play-state: paused;
}

@keyframes tickerMove {
    from {
        transform: translateX(0);
    }
    to {
        transform: translateX(-50%);
    }
}

/* Hero section */
.hero {
    background: linear-gradient(120deg, #173b68, #2563a6);
    padding: 35px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 25px;
    border: 1px solid #4778ad;
}

.hero h1 {
    color: white;
    font-size: 42px;
    margin-bottom: 8px;
}

.hero p {
    color: #dbeafe;
    font-size: 17px;
}

/* Result cards */
.result {
    background: #183e35;
    border: 1px solid #35a77b;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}

.spam {
    background: #48252d;
    border: 1px solid #e46b78;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}

/* Team section */
.team-section {
    margin-top: 35px;
    padding: 25px;
    background: #1e2d42;
    border: 1px solid #344a65;
    border-radius: 16px;
}

.team-card {
    background: linear-gradient(145deg, #243b58, #172b46);
    border: 1px solid #3c5d82;
    border-radius: 14px;
    padding: 22px 10px;
    text-align: center;
    min-height: 155px;
    transition: all 0.3s ease;
}

.team-card:hover {
    transform: translateY(-7px);
    border-color: #55aaff;
    box-shadow: 0 8px 25px #2878d055;
}

/* Animated developer name */
.name-glow {
    color: #7dc3ff;
    font-size: 20px;
    font-weight: bold;
    animation: nameGlow 2s ease-in-out infinite alternate;
}

@keyframes nameGlow {
    from {
        text-shadow: 0 0 5px #2878d0;
    }
    to {
        text-shadow: 0 0 15px #55aaff,
                     0 0 25px #2878d0;
    }
}

.team-role {
    color: #c2d5e9;
    font-size: 14px;
}

/* Message input */
.stTextArea textarea {
    background-color: #f4f7fb !important;
    color: #15243a !important;
    border-radius: 10px !important;
    font-size: 16px !important;
}

/* Buttons */
.stButton button {
    background: #2878d0;
    color: white;
    border: none;
    border-radius: 10px;
    min-height: 45px;
    font-weight: bold;
    width: 100%;
}

.stButton button:hover {
    background: #185da9;
    color: white;
}

/* Footer */
.footer {
    text-align: center;
    color: #a8b8cb;
    padding: 25px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 5. SCROLLING PROJECT BANNER
# ==========================================

st.markdown("""
<div class="ticker">
    <div class="ticker-text">
        SPAMGUARD | DEVELOPED BY SUMIT SHARMA |
        BCA 2025-29 | SMS SPAM CLASSIFICATION PROJECT
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 6. HERO HEADER
# ==========================================

# Continuous Scrolling Banner
st.markdown("""
<div class="ticker">
    <div class="ticker-track">
        <div class="ticker-content">
            SPAMGUARD | DEVELOPED BY SUMIT SHARMA |
            BCA 2025-29 | SMS SPAM CLASSIFICATION PROJECT
        </div>
        <div class="ticker-content">
            SPAMGUARD | DEVELOPED BY SUMIT SHARMA |
            BCA 2025-29 | SMS SPAM CLASSIFICATION PROJECT
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 7. TECHNOLOGY INFORMATION
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🤖 ML Powered")

with col2:
    st.markdown("### 📊 TF-IDF")

with col3:
    st.markdown("### 🎯 Linear SVM")

st.markdown("---")


# ==========================================
# 8. MESSAGE INPUT
# ==========================================

st.markdown("## 📩 Analyze Your Message")

st.write(
    "Enter an SMS message below to identify "
    "whether it is Spam or Ham."
)

message = st.text_area(
    "Enter your SMS message:",
    placeholder="Example: Congratulations! You have won a prize...",
    height=150,
    key="message_input"
)


# ==========================================
# 9. SAMPLE MESSAGES
# ==========================================

st.markdown("**Try a sample message:**")

sample_col1, sample_col2 = st.columns(2)

with sample_col1:
    if st.button("Normal Message"):
        st.session_state.message_input = (
            "Hey, how are you? Are you coming to college today?"
        )
        st.rerun()

with sample_col2:
    if st.button("Spam Message"):
        st.session_state.message_input = (
            "Congratulations! You have won a free prize. Claim now!"
        )
        st.rerun()


# ==========================================
# 10. SPAM DETECTION
# ==========================================

if st.button("Analyze Message"):

    message = st.session_state.message_input

    if not message.strip():

        st.warning("Please enter a message first.")

    elif not clean_text(message):

        st.warning("Please enter a message containing letters.")

    else:

        cleaned_message = clean_text(message)

        prediction = model.predict([cleaned_message])[0]

        st.markdown("---")
        st.markdown("## 📋 Analysis Result")

        if prediction == 1:

            st.markdown("""
            <div class="spam">
                <h2>SPAM MESSAGE</h2>
                <p>This message has been classified as spam.</p>
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="result">
                <h2>HAM MESSAGE</h2>
                <p>This message has been classified as a normal message.</p>
            </div>
            """, unsafe_allow_html=True)

        st.caption(
            "Prediction generated by the trained Linear SVM model."
        )


# ==========================================
# 11. PROJECT TEAM
# ==========================================

st.markdown("---")

st.markdown("""
<div class="team-section">
    <h2 style="text-align:center; color:white;">
        MEET OUR PROJECT TEAM
    </h2>
    <p style="text-align:center; color:#a8c5e3;">
        The developers behind SpamGuard
    </p>
</div>
""", unsafe_allow_html=True)

team1, team2, team3, team4 = st.columns(4)

with team1:
    st.markdown("""
    <div class="team-card">
        <div class="name-glow">Sumit Sharma</div>
        <p class="team-role">Lead Developer</p>
        <p class="team-role">BCA | 2025-29</p>
    </div>
    """, unsafe_allow_html=True)

with team2:
    st.markdown("""
    <div class="team-card">
        <h3 style="color:#7dc3ff;">Member 2</h3>
        <p class="team-role">Project Partner</p>
    </div>
    """, unsafe_allow_html=True)

with team3:
    st.markdown("""
    <div class="team-card">
        <h3 style="color:#7dc3ff;">Member 3</h3>
        <p class="team-role">Project Partner</p>
    </div>
    """, unsafe_allow_html=True)

with team4:
    st.markdown("""
    <div class="team-card">
        <h3 style="color:#7dc3ff;">Member 4</h3>
        <p class="team-role">Project Partner</p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# 12. FOOTER
# ==========================================

st.markdown("""
<div class="footer">
    <hr>
    <b>SpamGuard | SMS Spam Classification Project</b><br>
    BCA | 2025-29<br>
    Powered by Python, Scikit-learn and Streamlit
</div>
""", unsafe_allow_html=True)