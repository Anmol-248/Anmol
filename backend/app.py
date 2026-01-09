from flask import Flask, jsonify, request
import logging

from email_reader import fetch_emails
from call_handler import analyze_calls
from nlp import summarize_text
from notifier import send_sms_alert


# --------------------------------------------------
# Logging configuration
# --------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def create_app():
    """
    Application factory to create and configure the Flask app.
    """
    app = Flask(__name__)

    # -----------------------------
    # Health Check
    # -----------------------------
    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "AIVA backend running"}), 200

    # -----------------------------
    # Email Analysis (STABILIZED)
    # -----------------------------
    @app.route("/check_emails", methods=["GET"])
    def check_emails():
        logging.info("Email analysis requested")

        try:
            emails = fetch_emails()

            # Always return a list
            emails = emails if isinstance(emails, list) else []

            for e in emails:
                e["summary"] = summarize_text(e.get("body", ""))

            return jsonify({
                "count": len(emails),
                "emails": emails
            }), 200

        except Exception as err:
            logging.error(f"Email analysis failed: {err}")

            # Phase-1 rule: NEVER crash, ALWAYS respond
            return jsonify({
                "count": 0,
                "emails": [],
                "error": "Email analysis failed"
            }), 200

    # -----------------------------
    # Call Analysis (STABILIZED)
    # -----------------------------
    @app.route("/check_calls", methods=["GET"])
    def check_calls():
        logging.info("Call analysis requested")

        try:
            calls = analyze_calls()

            calls = calls if isinstance(calls, list) else []

            return jsonify({
                "count": len(calls),
                "calls": calls
            }), 200

        except Exception as err:
            logging.error(f"Call analysis failed: {err}")

            return jsonify({
                "count": 0,
                "calls": [],
                "error": "Call analysis failed"
            }), 200

    # -----------------------------
    # Send Alert (STABILIZED)
    # -----------------------------
    @app.route("/send_alert", methods=["POST"])
    def send_alert():
        logging.info("Send alert requested")

        data = request.get_json(silent=True) or {}

        recipient = data.get("to")
        message = data.get("message", "Test alert from AIVA")

        if not recipient:
            logging.warning("Alert request missing recipient")
            return jsonify({
                "error": "Recipient phone number is required"
            }), 400

        try:
            result = send_sms_alert(recipient, message)

            return jsonify({
                "result": result
            }), 200

        except Exception as err:
            logging.error(f"Alert sending failed: {err}")

            return jsonify({
                "error": "Failed to send alert"
            }), 200

    return app


# --------------------------------------------------
# App Entry Point
# --------------------------------------------------
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
