from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    events = requests.get("http://127.0.0.1:5050/events").json()

    devices = {}
    alerts = []

    for e in events:
        ip = e.get("ip", "")
        event = e.get("event", "")

        if ip:
            devices[ip] = e

        if event in ["ARP_SPOOF", "PORT_SCAN"]:
            alerts.append(e)

    html = """
    <html>
    <head>
    <title>SOC Dashboard</title>
    <meta http-equiv="refresh" content="3">
    <style>
    body { background:#0b1220; color:white; font-family:Arial; }
    .box { background:#1e293b; margin:15px; padding:15px; border-radius:10px; }
    .device { color:#22c55e; }
    .alert { color:#f87171; }
    </style>
    </head>
    <body>

    <h2>SOC DASHBOARD</h2>

    <div class="box">
    <h3>Active Devices</h3>
    """

    for ip in devices:
        html += f'<div class="device">{ip}</div>'

    html += """
    </div>

    <div class="box">
    <h3>Alerts</h3>
    """

    for a in alerts:
        html += f'<div class="alert">{a}</div>'

    html += """
    </div>

    </body>
    </html>
    """

    return html

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)