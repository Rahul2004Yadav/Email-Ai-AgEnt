import streamlit as st
from gmail_reader import fetch_emails
from filter_emails import filter_emails
from summarizer import summarize_emails

st.title("📧 Agentic Email Assistant")

instruction = st.text_input(
    "What should I look for in your emails?"
)

if st.button("Analyze Emails"):
    with st.spinner("Reading emails..."):
        emails = fetch_emails()

    filtered = filter_emails(emails, instruction)

    if not filtered:
        st.warning("No relevant emails found.")
    else:
        summary = summarize_emails(filtered)
        st.success("Summary Ready!")
        st.write(summary)
