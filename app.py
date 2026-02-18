from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Simple in-memory store to prevent duplicate processing
processed_events = set()

logging.basicConfig(level=logging.INFO)

@app.route("/webhook", methods=["POST"])
def handle_webhook():
    data = request.json

    if not data or "event_id" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    event_id = data["event_id"]

    # Idempotency check
    if event_id in processed_events:
        logging.info(f"Duplicate event received: {event_id}")
        return jsonify({"status": "duplicate"}), 200

    processed_events.add(event_id)

    logging.info(f"Processing event: {event_id}")
    logging.info(f"Payload: {data}")

    return jsonify({"status": "processed"}), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)
