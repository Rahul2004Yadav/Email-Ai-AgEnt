

import os
from dotenv import load_dotenv
import streamlit as st
from dotenv import dotenv_values
# Force load .env file
load_dotenv()

try:
    # Try local .env (dev)
    config = dotenv_values(".env")
    GROQ_API_KEY = config["GROQ_API_KEY"]
except Exception:
    # Streamlit deploy
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

if not GROQ_API_KEY:
    raise RuntimeError("❌ GROQ_API_KEY not found. Add to .env or Streamlit secrets.")
GROQ_MODEL = "llama-3.1-8b-instant"

# Debug check (TEMPORARY)
if GROQ_API_KEY is None:
    raise RuntimeError("❌ GROQ_API_KEY not found. Check your .env file.")

# =========================
# Gmail Configuration
# =========================

GMAIL_SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]

MAX_EMAILS_TO_FETCH = 5  # keep small to save tokens

DEBUG = True
