
# components.html(html_content, height=820, scrolling=False)
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="LoanSense AI",
    page_icon="₹",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# st.markdown("""
# <link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
# <style>
# #MainMenu, footer, header { visibility: hidden; }
# .block-container { padding: 0 !important; max-width: 100% !important; }
# </style>
# """, unsafe_allow_html=True)
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>

<style>
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* 🎨 PREMIUM DARK GREEN BACKGROUND */
.stApp {
    background: radial-gradient(circle at 20% 20%, #0F6B5C 0%, #063D33 40%, #021F1A 100%);
}

/* 🧾 GLOBAL TEXT */
body {
    color: #D1FAE5;
}

/* 🎯 BUTTON STYLE (MATCH ABOUT PAGE) */
.stButton>button {
    background: transparent;
    color: #D1FAE5;
    border: 1px solid rgba(52, 211, 153, 0.4);
    border-radius: 12px;
    font-weight: 500;
    transition: 0.3s;
}

.stButton>button:hover {
    background: rgba(52, 211, 153, 0.1);
    border-color: #34D399;
    color: #34D399;
}

/* ✨ CARD STYLE (GLASS EFFECT) */
.glass-card {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(52, 211, 153, 0.15);
    backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 24px;
}

/* 🟢 HEADINGS GRADIENT */
.gradient-text {
    background: linear-gradient(90deg, #22C55E, #34D399, #86EFAC);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* 🌿 MUTED TEXT */
.muted {
    color: #A7F3D0;
}
</style>
""", unsafe_allow_html=True)
# ── TOP NAVBAR ────────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

with col1:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:12px;padding:8px 0;">
      <div style="width:42px;height:42px;border-radius:11px;background:linear-gradient(135deg,#15a85c,#1fd47a);
        display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:800;color:#082419;">₹</div>
      <div>
        <div style="font-family:'Sora',sans-serif;font-weight:700;font-size:17px;color:#f0faf5;">
          Loan<span style="color:#34d17a;">Sense</span> AI</div>
        <div style="font-size:9px;letter-spacing:.16em;color:#8ecfaa;text-transform:uppercase;">Intelligent Loan System</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    if st.button("About", use_container_width=True):
        st.switch_page("pages/about.py")

with col4:
    if st.button(" Log In", use_container_width=True):
        st.switch_page("pages/login.py")

st.divider()

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:60px 20px 30px;">
  <div style="display:inline-flex;align-items:center;gap:9px;background:rgba(21,168,92,0.18);
    border:1px solid rgba(52,209,122,0.35);padding:7px 20px;border-radius:100px;
    font-size:12.5px;font-weight:500;color:#34d17a;margin-bottom:28px;">
    <span style="width:7px;height:7px;border-radius:50%;background:#1fd47a;display:inline-block;"></span>
    Powered by Machine Learning &amp; AI
  </div>
  <h1 style="font-family:'Sora',sans-serif;font-size:clamp(2rem,5vw,3.8rem);font-weight:800;
    line-height:1.1;color:#f0faf5;margin-bottom:18px;">
    <span style="background:linear-gradient(90deg,#15a85c,#1fd47a,#7fffba);
      -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
      Smart Loan Approval</span><br/>&amp; Prediction System
  </h1>
  <p style="font-size:1.05rem;color:#8ecfaa;max-width:500px;margin:0 auto;line-height:1.8;">
    Predict loan approval instantly using AI-powered insights and make smarter
    financial decisions &mdash; in seconds, not days.
  </p>
</div>
""", unsafe_allow_html=True)

# ── CTA BUTTONS ───────────────────────────────────────────────────────────────
# _, b1, b2, _ = st.columns([2, 1.5, 1.5, 2])
# with b1:
#     if st.button("🎯 Check My Eligibility", use_container_width=True, type="primary"):
#         st.switch_page("pages/form.py")
# with b2:
#     if st.button("🔒 Sign In / Register", use_container_width=True):
#         st.switch_page("pages/login.py")

st.markdown("<br>", unsafe_allow_html=True)

# ── STATS ─────────────────────────────────────────────────────────────────────
for col, num, label in zip(
    st.columns(3),
    ["98.2%", "< 5s", "Free"],
    ["Model Accuracy", "Prediction Time", "Always & Forever"]
):
    with col:
        st.markdown(f"""
        <div style="text-align:center;background:rgba(8,36,25,0.6);border:1px solid rgba(52,209,122,0.18);
          border-radius:14px;padding:22px 10px;">
          <div style="font-family:'Sora',sans-serif;font-size:1.8rem;font-weight:800;color:#1fd47a;">{num}</div>
          <div style="font-size:12px;color:#8ecfaa;margin-top:5px;">{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── FEATURE CARDS ─────────────────────────────────────────────────────────────
st.markdown("<h2 style='text-align:center;font-family:Sora,sans-serif;color:#f0faf5;margin-bottom:8px;'>Why Choose LoanSense AI?</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#8ecfaa;font-size:14px;margin-bottom:24px;'>Everything you need to make smarter loan decisions</p>", unsafe_allow_html=True)

cards = [
    ("🛡️", "Secure & Private",   "Your data is never stored or shared. All predictions happen within your session."),
    ("⚡", "Instant Results",     "Get your loan approval prediction in under 5 seconds with detailed reasoning."),
   
    ("🧠", "AI-Powered Insights", "Our ML model analyses 10+ financial parameters for highly accurate predictions."),
]
for col, (icon, title, desc) in zip(st.columns(3), cards):
    with col:
        st.markdown(f"""
        <div style="background:rgba(8,36,25,0.6);border:1px solid rgba(52,209,122,0.18);
          border-radius:18px;padding:26px 22px;">
          <div style="font-size:28px;margin-bottom:14px;">{icon}</div>
          <h3 style="font-family:'Sora',sans-serif;font-size:.95rem;font-weight:700;color:#f0faf5;margin-bottom:9px;">{title}</h3>
          <p style="font-size:13px;color:#8ecfaa;line-height:1.7;">{desc}</p>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── HOW IT WORKS ─────────────────────────────────────────────────────────────
st.markdown("<h2 style='text-align:center;font-family:Sora,sans-serif;color:#f0faf5;margin-bottom:8px;'>How It Works</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#8ecfaa;font-size:14px;margin-bottom:24px;'>Three simple steps to your loan prediction</p>", unsafe_allow_html=True)

steps = [
    ("1", "Enter Your Details", "Fill in your income, credit score, employment status and loan requirements."),
    ("2", "AI Analysis",        "Our trained ML model analyses your profile against thousands of loan patterns."),
    ("3", "Get Your Result",    "Receive your approval prediction with a confidence score and improvement tips."),
]
for col, (num, title, desc) in zip(st.columns(3), steps):
    with col:
        st.markdown(f"""
        <div style="text-align:center;background:rgba(8,36,25,0.6);border:1px solid rgba(52,209,122,0.12);
          border-radius:18px;padding:32px 20px;">
          <div style="width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,#15a85c,#1fd47a);
            display:flex;align-items:center;justify-content:center;font-family:'Sora',sans-serif;
            font-weight:800;font-size:16px;color:#082419;margin:0 auto 16px;">{num}</div>
          <h4 style="font-family:'Sora',sans-serif;font-size:.95rem;font-weight:700;color:#f0faf5;margin-bottom:10px;">{title}</h4>
          <p style="font-size:13px;color:#8ecfaa;line-height:1.65;">{desc}</p>
        </div>""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-size:12.5px;color:#4e8a66;'>© 2025 LoanSense AI — Built for smarter financial decisions</p>", unsafe_allow_html=True)