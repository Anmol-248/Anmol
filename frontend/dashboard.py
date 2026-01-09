import streamlit as st
import requests

# -----------------------------------
# Configuration
# -----------------------------------
BACKEND_URL = "http://127.0.0.1:5000"

st.set_page_config(
    page_title="AIVA – AI Virtual Assistant",
    layout="wide"
)

# -----------------------------------
# Header
# -----------------------------------
st.title("🤖 AIVA – AI Virtual Assistant")
st.caption("Unified dashboard for email and call intelligence")

st.success("🟢 Backend Connected")

st.markdown("---")

# -----------------------------------
# Layout Columns
# -----------------------------------
col1, col2 = st.columns(2)

# ===================================
# EMAIL ANALYSIS
# ===================================
with col1:
    st.subheader("📧 Email Analysis")

    if st.button("Run Email Analysis"):
        with st.spinner("Analyzing emails..."):
            try:
                res = requests.get(f"{BACKEND_URL}/check_emails", timeout=10)
                data = res.json()

                st.metric("Total Emails", data.get("count", 0))

                if data.get("emails"):
                    for email in data["emails"]:
                        with st.container():
                            st.markdown(f"**From:** {email.get('from', 'N/A')}")
                            st.markdown(f"**Subject:** {email.get('subject', 'N/A')}")
                            st.markdown(f"**Summary:** {email.get('summary', '')}")
                            st.markdown("---")
                else:
                    st.info("No emails found.")

                if data.get("error"):
                    st.warning(data.get("error"))

            except Exception as e:
                st.error(f"Failed to fetch emails: {e}")

# ===================================
# CALL ANALYSIS
# ===================================
with col2:
    st.subheader("📞 Call Analysis")

    if st.button("Run Call Analysis"):
        with st.spinner("Analyzing calls..."):
            try:
                res = requests.get(f"{BACKEND_URL}/check_calls", timeout=10)
                data = res.json()

                st.metric("Total Calls", data.get("count", 0))

                if data.get("calls"):
                    for call in data["calls"]:
                        st.json(call)
                else:
                    st.info("No calls found.")

                if data.get("error"):
                    st.warning(data.get("error"))

            except Exception as e:
                st.error(f"Failed to fetch calls: {e}")

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")
st.caption("AIVA © Local AI Virtual Assistant Dashboard")

