from datetime import datetime


def analyze_calls():
    """
    Analyze call logs and return structured call information.

    Currently returns mock data.
    Can be extended to integrate with:
    - Twilio APIs
    - Android call logs
    - Telecom provider data
    """
    calls = [
        {
            "id": "call_001",
            "from": "+919876543210",
            "type": "missed",
            "duration_sec": 0,
            "timestamp": datetime.utcnow().isoformat(),
            "note": "Unknown number - suspected spam"
        },
        {
            "id": "call_002",
            "from": "+911234567890",
            "type": "incoming",
            "duration_sec": 120,
            "timestamp": datetime.utcnow().isoformat(),
            "note": "Client - project discussion"
        }
    ]

    return calls
