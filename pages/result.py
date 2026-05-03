import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="LoanSense AI – Result",
    page_icon="₹",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

nav = st.query_params.get("nav", "")
if nav == "home":
    st.query_params.clear()
    st.switch_page("app.py")
elif nav == "form":
    st.query_params.clear()
    st.switch_page("pages/form.py")

# Get prediction results from session state
prediction = st.session_state.get("prediction", None)
confidence = st.session_state.get("confidence", 0)
error = st.session_state.get("pred_error", "")
form_data = st.session_state.get("form_data", {})

if prediction is None:
    # No prediction found, redirect to form
    st.switch_page("pages/form.py")

approved = str(prediction).strip() in ["Y", "1", "Approved", "Yes", "approved"]

if error:
    result_html = f"""
    <div class="result-card error-card">
      <div class="result-icon">&#10060;</div>
      <h2 class="result-title">Prediction Error</h2>
      <p class="result-sub" style="color:#ff9999;">{error}</p>
      <p class="result-sub">Please check your model file and try again.</p>
    </div>
    """
elif approved:
    result_html = f"""
    <div class="result-card approved-card">
      <div class="result-icon approved-glow">&#9989;</div>
      <div class="result-badge approved-badge">APPROVED</div>
      <h2 class="result-title">Congratulations!</h2>
      <p class="result-sub">Based on your profile, you are likely to be <strong style="color:#1fd47a;">approved</strong> for this loan.</p>
      <div class="confidence-row">
        <span class="conf-label">Confidence Score</span>
        <span class="conf-score approved-score">{confidence}%</span>
      </div>
      <div class="conf-bar"><div class="conf-fill approved-fill" style="width:{confidence}%"></div></div>
    </div>
    """
else:
    result_html = f"""
    <div class="result-card rejected-card">
      <div class="result-icon rejected-glow">&#10060;</div>
      <div class="result-badge rejected-badge">DECLINED</div>
      <h2 class="result-title">Not Approved</h2>
      <p class="result-sub">Based on your current profile, loan approval is <strong style="color:#ff6b6b;">unlikely</strong>. See tips below to improve your chances.</p>
      <div class="confidence-row">
        <span class="conf-label">Confidence Score</span>
        <span class="conf-score rejected-score">{confidence}%</span>
      </div>
      <div class="conf-bar"><div class="conf-fill rejected-fill" style="width:{confidence}%"></div></div>
    </div>
    """

# Tips HTML
if approved:
    tips_html = """
    <div class="tips-section">
      <h3 class="tips-title">&#128218; Next Steps</h3>
      <div class="tips-grid">
        <div class="tip-card"><div class="tip-icon">&#127974;</div><h4>Compare Banks</h4><p>Compare interest rates from SBI, HDFC, ICICI and others to get the best deal.</p></div>
        <div class="tip-card"><div class="tip-icon">&#128203;</div><h4>Gather Documents</h4><p>Prepare income proof, ID, address proof and bank statements for quick processing.</p></div>
        <div class="tip-card"><div class="tip-icon">&#128176;</div><h4>Check EMI</h4><p>Calculate your monthly EMI to ensure it fits comfortably within your budget.</p></div>
      </div>
    </div>
    """
else:
    credit_tip = "Repay outstanding loans and avoid defaults to build a strong credit history." if form_data.get("credit_history", 1) == 0 else "Maintain timely repayments to keep your credit score high."
    tips_html = f"""
    <div class="tips-section">
      <h3 class="tips-title">&#128161; How to Improve Your Chances</h3>
      <div class="tips-grid">
        <div class="tip-card"><div class="tip-icon">&#128200;</div><h4>Boost Income</h4><p>Consider adding a co-applicant with stable income to strengthen your application.</p></div>
        <div class="tip-card"><div class="tip-icon">&#127775;</div><h4>Credit Score</h4><p>{credit_tip}</p></div>
        <div class="tip-card"><div class="tip-icon">&#128184;</div><h4>Reduce Loan Amount</h4><p>Applying for a smaller loan amount relative to your income improves approval odds.</p></div>
      </div>
    </div>
    """

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'DM Sans', sans-serif; background: #082419; color: #f0faf5; min-height: 100vh; }}
  .bg-mesh {{ position: fixed; inset: 0; z-index: 0; pointer-events: none;
    background: radial-gradient(ellipse 70% 50% at 50% 0%, rgba(21,168,92,0.35) 0%, transparent 65%),
                linear-gradient(160deg, #0a2e1e 0%, #082419 55%, #061a12 100%); }}
  .navbar {{ position: sticky; top: 0; z-index: 999; display: flex; align-items: center; justify-content: space-between;
    padding: 0 60px; height: 68px; background: rgba(10,46,30,0.85); backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(52,209,122,0.14); }}
  .nav-logo {{ display: flex; align-items: center; gap: 12px; cursor: pointer; }}
  .logo-icon {{ width: 38px; height: 38px; border-radius: 10px; background: linear-gradient(135deg,#15a85c,#1fd47a);
    display:flex; align-items:center; justify-content:center; font-size:18px; font-weight:800; color:#082419; }}
  .logo-name {{ font-family:'Sora',sans-serif; font-weight:700; font-size:16px; color:#f0faf5; }}
  .logo-name span {{ color:#34d17a; }}
  .nav-btns {{ display:flex; gap:10px; }}
  .btn-nav {{ font-family:'Sora',sans-serif; font-size:13px; font-weight:600; color:#8ecfaa; background:transparent;
    border:1px solid rgba(52,209,122,0.25); padding:8px 18px; border-radius:8px; cursor:pointer; transition:all .2s; }}
  .btn-nav:hover {{ color:#f0faf5; border-color:#34d17a; background:rgba(52,209,122,0.08); }}
  .btn-primary-nav {{ color:#082419; background:linear-gradient(135deg,#15a85c,#1fd47a); border:none;
    box-shadow:0 4px 16px rgba(31,212,122,.35); }}
  .btn-primary-nav:hover {{ transform:translateY(-1px); box-shadow:0 6px 22px rgba(31,212,122,.5); color:#082419; }}

  .content {{ position:relative; z-index:1; max-width:700px; margin:0 auto; padding:50px 30px 80px; }}

  .result-card {{ border-radius:22px; padding:44px; text-align:center; margin-bottom:28px;
    animation: pop .5s cubic-bezier(.175,.885,.32,1.275) both; }}
  .approved-card {{ background:rgba(21,168,92,0.12); border:1.5px solid rgba(52,209,122,0.35); }}
  .rejected-card {{ background:rgba(255,107,107,0.08); border:1.5px solid rgba(255,107,107,0.25); }}
  .error-card {{ background:rgba(255,150,50,0.08); border:1.5px solid rgba(255,150,50,0.25); }}

  .result-icon {{ font-size:3.5rem; margin-bottom:16px; display:block; }}
  .approved-glow {{ filter:drop-shadow(0 0 20px rgba(31,212,122,.6)); }}
  .rejected-glow {{ filter:drop-shadow(0 0 20px rgba(255,107,107,.5)); }}

  .result-badge {{ display:inline-block; font-family:'Sora',sans-serif; font-size:11px; font-weight:800;
    letter-spacing:.15em; padding:5px 18px; border-radius:100px; margin-bottom:14px; }}
  .approved-badge {{ background:rgba(31,212,122,0.2); color:#1fd47a; border:1px solid rgba(31,212,122,.4); }}
  .rejected-badge {{ background:rgba(255,107,107,0.15); color:#ff6b6b; border:1px solid rgba(255,107,107,.35); }}

  .result-title {{ font-family:'Sora',sans-serif; font-size:1.9rem; font-weight:800; margin-bottom:12px; }}
  .result-sub {{ font-size:14.5px; color:#8ecfaa; line-height:1.7; max-width:440px; margin:0 auto 22px; }}

  .confidence-row {{ display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; }}
  .conf-label {{ font-size:13px; color:#8ecfaa; }}
  .conf-score {{ font-family:'Sora',sans-serif; font-size:1.4rem; font-weight:800; }}
  .approved-score {{ color:#1fd47a; }}
  .rejected-score {{ color:#ff6b6b; }}
  .conf-bar {{ height:8px; background:rgba(255,255,255,0.08); border-radius:100px; overflow:hidden; }}
  .conf-fill {{ height:100%; border-radius:100px; transition:width 1s ease; }}
  .approved-fill {{ background:linear-gradient(90deg,#15a85c,#1fd47a); }}
  .rejected-fill {{ background:linear-gradient(90deg,#c0392b,#ff6b6b); }}

  .tips-section {{ animation: fadeUp .5s .25s ease both; }}
  .tips-title {{ font-family:'Sora',sans-serif; font-size:1.1rem; font-weight:800; margin-bottom:18px; }}
  .tips-grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:16px; }}
  .tip-card {{ background:rgba(13,92,58,0.2); border:1px solid rgba(52,209,122,0.12); border-radius:14px; padding:22px 18px; }}
  .tip-icon {{ font-size:1.6rem; margin-bottom:10px; }}
  .tip-card h4 {{ font-family:'Sora',sans-serif; font-size:.88rem; font-weight:700; color:#f0faf5; margin-bottom:7px; }}
  .tip-card p {{ font-size:12.5px; color:#8ecfaa; line-height:1.6; }}

  @keyframes pop {{ from {{ opacity:0; transform:scale(.92); }} to {{ opacity:1; transform:scale(1); }} }}
  @keyframes fadeUp {{ from {{ opacity:0; transform:translateY(16px); }} to {{ opacity:1; transform:translateY(0); }} }}

  @media(max-width:600px) {{
    .tips-grid {{ grid-template-columns:1fr; }}
    .navbar {{ padding:0 16px; }}
    .result-card {{ padding:28px 22px; }}
  }}
</style>
</head>
<body>
<div class="bg-mesh"></div>
<nav class="navbar">
  <div class="nav-logo" onclick="navigate('home')">
    <div class="logo-icon">&#8377;</div>
    <span class="logo-name">Loan<span>Sense</span> AI</span>
  </div>
  <div class="nav-btns">
    <button class="btn-nav" onclick="navigate('home')">&#8592; Home</button>
    <button class="btn-nav btn-primary-nav" onclick="navigate('form')">&#128260; Try Again</button>
  </div>
</nav>

<div class="content">
  {result_html}
  {tips_html}
</div>

<script>
function navigate(page) {{
  const url = new URL(window.parent.location.href);
  url.searchParams.set('nav', page);
  window.parent.location.href = url.toString();
}}
</script>
</body>
</html>
"""

components.html(html_content, height=1000, scrolling=True)