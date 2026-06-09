import streamlit as st
from rag_core import ask
 
st.set_page_config(
    page_title="Sunshine Clinic – Patient Assistant",
    page_icon="🏥",
    layout="centered"
)
 
st.markdown("""
<style>
    .clinic-header {
        background: linear-gradient(135deg, #1a73e8, #0d47a1);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .clinic-header h1 { margin: 0; font-size: 1.6rem; }
    .clinic-header p  { margin: 0.3rem 0 0; opacity: 0.85; font-size: 0.9rem; }
 
    .info-badge {
        display: inline-block;
        background: #e8f0fe;
        color: #1a73e8;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        margin: 2px;
    }
    .quick-btn {
        background: #f1f3f4;
        border: 1px solid #dadce0;
        border-radius: 20px;
        padding: 6px 14px;
        cursor: pointer;
        font-size: 0.85rem;
        margin: 3px;
    }
    [data-testid="stChatMessage"] {
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)
 
st.markdown("""
<div class="clinic-header">
    <h1>🏥 Sunshine Clinic</h1>
    <p>AI Patient Assistant • Available 24/7 • Hindi & English</p>
</div>
""", unsafe_allow_html=True)
 
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<span class="info-badge">📍 FC Road, Pune</span>', unsafe_allow_html=True)
with col2:
    st.markdown('<span class="info-badge">📞 020-25001234</span>', unsafe_allow_html=True)
with col3:
    st.markdown('<span class="info-badge">⏰ Mon–Sat 9AM–8PM</span>', unsafe_allow_html=True)
 
st.markdown("---")
st.markdown("**Quick questions** — click to ask instantly:")
 
quick_questions = [
    "What are the clinic timings?",
    "Which doctors are available?",
    "What is the consultation fee?",
    "How to book an appointment?",
    "Is the clinic open on Sunday?",
    "क्लिनिक का समय क्या है?"
]
 
cols = st.columns(3)
for i, q in enumerate(quick_questions):
    with cols[i % 3]:
        if st.button(q, key=f"quick_{i}", use_container_width=True):
            if "messages" not in st.session_state:
                st.session_state.messages = []
            st.session_state.messages.append({"role": "user", "content": q})
            with st.spinner("Checking clinic records..."):
                answer = ask(q)
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.rerun()
 
st.markdown("---")
 
if "messages" not in st.session_state:
    st.session_state.messages = []
 
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.write("👋 Hello! I'm the Sunshine Clinic assistant. I can answer questions about our doctors, timings, fees, and appointments — in Hindi or English. How can I help you today?")
 
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
 
if user_input := st.chat_input("Type your question here... (Hindi या English में पूछें)"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
 
    with st.chat_message("assistant"):
        with st.spinner("Checking clinic records..."):
            response = ask(user_input)
        st.write(response)
 
    st.session_state.messages.append({"role": "assistant", "content": response})
 
st.markdown("---")
st.markdown("""
<div style="text-align:center; color: #888; font-size: 0.8rem; padding: 1rem;">
    🤖 This AI assistant answers from verified clinic records only.<br>
    For emergencies call <strong>9876500000</strong> • 
    <a href="tel:02025001234">📞 Book: 020-25001234</a>
</div>
""", unsafe_allow_html=True)