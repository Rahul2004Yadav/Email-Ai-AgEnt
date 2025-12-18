from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle, os, base64
from email import message_from_bytes

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    if os.path.exists('token.pkl'):
        with open('token.pkl', 'rb') as f:
            creds = pickle.load(f)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.pkl', 'wb') as f:
            pickle.dump(creds, f)

    return build('gmail', 'v1', credentials=creds)

def fetch_emails(max_results=20):
    service = get_gmail_service()
    results = service.users().messages().list(
        userId='me', maxResults=max_results).execute()

    emails = []
    for msg in results.get('messages', []):
        data = service.users().messages().get(
            userId='me', id=msg['id'], format='raw').execute()

        raw = base64.urlsafe_b64decode(data['raw'])
        email_msg = message_from_bytes(raw)

        body = ""
        if email_msg.is_multipart():
            for part in email_msg.walk():
                if part.get_content_type() == "text/plain":
                    body += part.get_payload(decode=True).decode()
        else:
            body = email_msg.get_payload(decode=True).decode()

        emails.append({
            "subject": email_msg['subject'],
            "from": email_msg['from'],
            "body": body
        })

    return emails
