from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)

def summarize_emails(emails):
    if not emails:
        return "No emails to summarize."

    combined = ""
    for i, mail in enumerate(emails, 1):
        combined += f"""
Email {i}
Subject: {mail['subject']}
From: {mail['from']}
Content: {mail['body'][:1500]}
"""

    prompt = f"""
You are an intelligent email assistant.

Summarize the following emails.
Focus on:
- Important information
- Action items
- Deadlines

Provide a clear bullet-point summary.

Emails:
{combined}
"""

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content
