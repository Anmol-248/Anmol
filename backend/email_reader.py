from datetime import datetime


def fetch_emails():
    """
    Fetch emails and return them in a structured format.

    Currently returns mocked data.
    Can be extended to integrate with:
    - Gmail API (OAuth 2.0)
    - Government mail servers
    - Enterprise IMAP/POP3 systems
    """
    emails = [
        {
            "id": "email_001",
            "from": "client@example.com",
            "subject": "Meeting request: Project sync",
            "body": (
                "Hi Anmol,\n"
                "Can we meet tomorrow at 3pm to discuss the project "
                "timeline and deliverables?\n"
                "Regards,\n"
                "Client."
            ),
            "timestamp": datetime.utcnow().isoformat()
        },
        {
            "id": "email_002",
            "from": "promo@store.com",
            "subject": "Big Sale this weekend!",
            "body": "Huge discounts on electronics. Don't miss out.",
            "timestamp": datetime.utcnow().isoformat()
        }
    ]

    return emails
