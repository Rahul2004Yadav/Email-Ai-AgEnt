

import os
from dotenv import load_dotenv

# Force load .env file
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
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
