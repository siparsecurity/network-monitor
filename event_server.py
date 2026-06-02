from flask import Flask, jsonify
from collections import deque

app = Flask(__name__)

events = deque(maxlen=200)
devices = {}

# called by IDS
@app.route("/push", methods=["POST"])
def push_event():
    from flask import request

    data = request.json

    events.append(data)

    ip = data.get("ip")
    mac = data.get("mac")

    if ip:
        devices[ip] = mac

    return {"status": "ok"}

# dashboard uses this
@app.route("/events")
def get_events():
    return jsonify(list(events))

@app.route("/devices")
def get_devices():
    return jsonify(devices)

if __name__ == "__main__":
    print("[+] Event Server running on http://127.0.0.1:5050")
    app.run(port=5050)
@app.route("/")
def home():
    return "SOC Event Server Running"