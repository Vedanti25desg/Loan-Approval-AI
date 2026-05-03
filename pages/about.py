
import streamlit as st

st.set_page_config(
    page_title="LoanSense AI – About",
    page_icon="₹",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── INJECT CSS SEPARATELY ─────────────────────────────────────────────────────
st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>""", unsafe_allow_html=True)

st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.stApp {
    background: radial-gradient(circle at 20% 20%, #0F6B5C 0%, #063D33 40%, #021F1A 100%);
}
body { color: #D1FAE5; }
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

with col2:
    if st.button(" Home", use_container_width=True):
        st.switch_page("app.py")

with col3:
    st.markdown("""
    <div style="display:flex;align-items:center;justify-content:center;height:38px;
      border:1px solid rgba(52,209,122,0.6);border-radius:12px;
      color:#1fd47a;font-size:14px;font-weight:600;">
      About
    </div>""", unsafe_allow_html=True)

with col4:
    if st.button(" Log In", use_container_width=True):
        st.switch_page("pages/login.py")

st.divider()

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:50px 20px 30px;">
  <div style="display:inline-flex;align-items:center;gap:9px;background:rgba(21,168,92,0.18);
    border:1px solid rgba(52,209,122,0.35);padding:7px 20px;border-radius:100px;
    font-size:12.5px;font-weight:500;color:#34d17a;margin-bottom:28px;">
     About LoanSense AI
  </div>
  <h1 style="font-family:'Sora',sans-serif;font-size:clamp(2rem,5vw,3.4rem);font-weight:800;
    line-height:1.1;color:#f0faf5;margin-bottom:18px;">
    Built to Make
    <span style="background:linear-gradient(90deg,#15a85c,#1fd47a,#7fffba);
      -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
      Loan Decisions</span><br/>Smarter &amp; Faster
  </h1>
  <p style="font-size:1.05rem;color:#8ecfaa;max-width:560px;margin:0 auto;line-height:1.8;">
    LoanSense AI is an intelligent loan approval prediction system that uses machine learning
    to help individuals understand their loan eligibility before they even apply — saving time,
    reducing stress, and improving financial literacy.
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── ABOUT CARDS ───────────────────────────────────────────────────────────────
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
    <div style="background:rgba(8,36,25,0.6);border:1px solid rgba(52,209,122,0.18);
      border-radius:18px;padding:28px 24px;margin-bottom:20px;">
      <h3 style="font-family:'Sora',sans-serif;font-size:.95rem;font-weight:700;
        color:#1fd47a;margin-bottom:10px;"> Our Mission</h3>
      <p style="font-size:13.5px;color:#8ecfaa;line-height:1.75;">
        To democratise access to financial intelligence. We believe everyone deserves clear,
        instant, unbiased information about their loan eligibility — without waiting days
        for bank responses.
      </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:rgba(8,36,25,0.6);border:1px solid rgba(52,209,122,0.18);
      border-radius:18px;padding:28px 24px;">
      <h3 style="font-family:'Sora',sans-serif;font-size:.95rem;font-weight:700;
        color:#1fd47a;margin-bottom:10px;"> Privacy First</h3>
      <p style="font-size:13.5px;color:#8ecfaa;line-height:1.75;">
        We never sell or share your data. All predictions run within your session.
        Your financial information stays yours — always.
      </p>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
    <div style="background:rgba(8,36,25,0.6);border:1px solid rgba(52,209,122,0.18);
      border-radius:18px;padding:28px 24px;margin-bottom:20px;">
      <h3 style="font-family:'Sora',sans-serif;font-size:.95rem;font-weight:700;
        color:#1fd47a;margin-bottom:10px;"> The Technology</h3>
      <p style="font-size:13.5px;color:#8ecfaa;line-height:1.75;">
        Our core model is trained on thousands of real loan application outcomes. It analyses
        income, credit history, employment status, and more to deliver predictions with
        &gt;98% accuracy.
      </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:rgba(8,36,25,0.6);border:1px solid rgba(52,209,122,0.18);
      border-radius:18px;padding:28px 24px;">
      <h3 style="font-family:'Sora',sans-serif;font-size:.95rem;font-weight:700;
        color:#1fd47a;margin-bottom:10px;"> Completely Free</h3>
      <p style="font-size:13.5px;color:#8ecfaa;line-height:1.75;">
        Every tool on LoanSense AI is 100% free. No hidden fees, no premium tiers.
        We believe financial literacy should be accessible to all.
      </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── TECH STACK ────────────────────────────────────────────────────────────────
st.markdown("<h2 style='text-align:center;font-family:Sora,sans-serif;color:#f0faf5;margin-bottom:18px;'>Built With</h2>", unsafe_allow_html=True)

st.markdown("""
<div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-bottom:40px;">
  <span style="background:rgba(21,168,92,0.15);border:1px solid rgba(52,209,122,0.25);color:#34d17a;
    padding:8px 20px;border-radius:100px;font-size:13px;font-weight:500;">Python</span>
  <span style="background:rgba(21,168,92,0.15);border:1px solid rgba(52,209,122,0.25);color:#34d17a;
    padding:8px 20px;border-radius:100px;font-size:13px;font-weight:500;">Streamlit</span>
  <span style="background:rgba(21,168,92,0.15);border:1px solid rgba(52,209,122,0.25);color:#34d17a;
    padding:8px 20px;border-radius:100px;font-size:13px;font-weight:500;">Scikit-learn</span>
  <span style="background:rgba(21,168,92,0.15);border:1px solid rgba(52,209,122,0.25);color:#34d17a;
    padding:8px 20px;border-radius:100px;font-size:13px;font-weight:500;">Pandas</span>
  <span style="background:rgba(21,168,92,0.15);border:1px solid rgba(52,209,122,0.25);color:#34d17a;
    padding:8px 20px;border-radius:100px;font-size:13px;font-weight:500;">NumPy</span>
  <span style="background:rgba(21,168,92,0.15);border:1px solid rgba(52,209,122,0.25);color:#34d17a;
    padding:8px 20px;border-radius:100px;font-size:13px;font-weight:500;">SQLite</span>
  <span style="background:rgba(21,168,92,0.15);border:1px solid rgba(52,209,122,0.25);color:#34d17a;
    padding:8px 20px;border-radius:100px;font-size:13px;font-weight:500;">Joblib</span>
  <span style="background:rgba(21,168,92,0.15);border:1px solid rgba(52,209,122,0.25);color:#34d17a;
    padding:8px 20px;border-radius:100px;font-size:13px;font-weight:500;">Machine Learning</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-size:12.5px;color:#4e8a66;'>© 2025 LoanSense AI — Built for smarter financial decisions</p>", unsafe_allow_html=True)