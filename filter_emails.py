def filter_emails(emails, instruction):
    keywords = instruction.lower().split()
    filtered = []

    for mail in emails:
        text = (mail["subject"] + mail["body"]).lower()
        if any(k in text for k in keywords):
            filtered.append(mail)

    return filtered
