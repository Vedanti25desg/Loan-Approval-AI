import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from auth import login_user, register_user

st.set_page_config(
    page_title="LoanSense AI – Sign In",
    page_icon="₹",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── ALL styles in one block, unsafe_allow_html=True, at the very top ──────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
<style>
#MainMenu, footer, header { visibility: hidden; }
.stApp { background: #063D33 !important; }
.block-container {
    padding: 2rem 1rem !important;
    max-width: 500px !important;
    margin: 0 auto !important;
}
.stTextInput > div > div > input {
    background: rgba(8,36,25,0.9) !important;
    border: 1.5px solid rgba(52,209,122,0.25) !important;
    border-radius: 10px !important;
    color: #f0faf5 !important;
    font-size: 14px !important;
    padding: 12px 14px !important;
}
.stTextInput > div > div > input:focus {
    border-color: #34d17a !important;
    box-shadow: 0 0 0 3px rgba(52,209,122,0.12) !important;
}
.stTextInput > div > div > input::placeholder { color: #4e8a66 !important; }
.stTextInput label { color: #8ecfaa !important; font-size: 13px !important; font-weight: 500 !important; }
.stFormSubmitButton > button {
    width: 100% !important;
    border-radius: 11px !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    padding: 12px 20px !important;
    background: linear-gradient(135deg, #15a85c, #1fd47a) !important;
    color: #082419 !important;
    border: none !important;
}
.stFormSubmitButton > button:hover {
    box-shadow: 0 8px 28px rgba(31,212,122,0.45) !important;
    transform: translateY(-1px) !important;
}
.stButton > button {
    background: transparent !important;
    color: #8ecfaa !important;
    border: 1px solid rgba(52,209,122,0.3) !important;
    border-radius: 9px !important;
    font-size: 13px !important;
    padding: 8px 16px !important;
}
.stButton > button:hover {
    color: #f0faf5 !important;
    border-color: #34d17a !important;
    background: rgba(52,209,122,0.08) !important;
}
.stTabs [data-baseweb="tab-list"] {
    background: rgba(8,36,25,0.6) !important;
    border-radius: 10px !important;
    padding: 4px !important;
    border: 1px solid rgba(52,209,122,0.15) !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 8px !important;
    color: #8ecfaa !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    padding: 8px 20px !important;
    background: transparent !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #15a85c, #1fd47a) !important;
    color: #082419 !important;
}
hr { border-color: rgba(52,209,122,0.12) !important; }
</style>
""", unsafe_allow_html=True)

# ── If already logged in, go straight to form ─────────────────────────────────
if st.session_state.get("logged_in"):
    st.switch_page("pages/form.py")

# ── Back button ───────────────────────────────────────────────────────────────
if st.button("← Back to Home"):
    st.switch_page("app.py")

# ── Logo + Title ──────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding: 20px 0 10px;">
  <div style="width:54px;height:54px;border-radius:14px;
    background:linear-gradient(135deg,#15a85c,#1fd47a);
    display:inline-flex;align-items:center;justify-content:center;
    font-size:26px;font-weight:800;color:#082419;
    box-shadow:0 0 28px rgba(31,212,122,.4);margin-bottom:14px;">₹</div>
  <h2 style="font-family:'Sora',sans-serif;font-size:1.55rem;
    font-weight:800;color:#f0faf5;margin-bottom:6px;">
    Welcome to LoanSense AI
  </h2>
  <p style="font-size:13.5px;color:#8ecfaa;">
    Sign in or create your account below
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2 = st.tabs(["🔐   Sign In", "📝   Register"])

# ── SIGN IN TAB ───────────────────────────────────────────────────────────────
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    with st.form("login_form", clear_on_submit=False):
        email    = st.text_input("Email Address", placeholder="you@example.com")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Sign In →", use_container_width=True)

    if submitted:
        if not email.strip() or not password.strip():
            st.error("⚠️ Please enter both email and password.")
        else:
            result = login_user(email.strip(), password)
            if result["success"]:
                st.session_state["logged_in"]  = True
                st.session_state["user_name"]  = result["name"]
                st.session_state["user_email"] = email.strip()
                st.success(f"✅ Welcome back, **{result['name']}**!")
                st.switch_page("pages/form.py")
            else:
                st.error(f"❌ {result['error']}")

    st.markdown("""
    <p style="text-align:center;font-size:13px;color:#8ecfaa;margin-top:16px;">
      No account yet? Click the <strong style="color:#34d17a;">Register</strong> tab above.
    </p>
    """, unsafe_allow_html=True)

# ── REGISTER TAB ──────────────────────────────────────────────────────────────
with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    with st.form("register_form", clear_on_submit=True):
        name      = st.text_input("Full Name", placeholder="Your full name")
        reg_email = st.text_input("Email Address", placeholder="you@example.com")
        reg_pass  = st.text_input("Password", type="password", placeholder="At least 6 characters")
        st.markdown("<br>", unsafe_allow_html=True)
        reg_submit = st.form_submit_button("Create Account →", use_container_width=True)

    if reg_submit:
        if not name.strip() or not reg_email.strip() or not reg_pass.strip():
            st.error("⚠️ Please fill in all three fields.")
        elif len(reg_pass) < 6:
            st.error("⚠️ Password must be at least 6 characters.")
        else:
            result = register_user(name.strip(), reg_email.strip(), reg_pass)
            if result["success"]:
                st.success("✅ Account created! Now click the **Sign In** tab and log in.")
            else:
                st.error(f"❌ {result['error']}")

    st.markdown("""
    <p style="text-align:center;font-size:13px;color:#8ecfaa;margin-top:16px;">
      Already registered? Click the <strong style="color:#34d17a;">Sign In</strong> tab above.
    </p>
    """, unsafe_allow_html=True)