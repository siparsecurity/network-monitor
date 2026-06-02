from scapy.all import ARP, Ether, srp, conf
import netifaces
import ipaddress
import time
import requests
from collections import defaultdict

# -----------------------------
# EVENT SENDER
# -----------------------------
def send_event(event, ip, mac="", details="", risk=0):
    try:
        requests.post(
            "http://127.0.0.1:5050/push",
            json={
                "event": event,
                "ip": ip,
                "mac": mac,
                "details": details,
                "risk": risk
            },
            timeout=1
        )
    except:
        pass


# -----------------------------
# AUTO NETWORK DETECTION
# -----------------------------
iface = str(conf.iface)

ip_info = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]
ip_addr = ip_info["addr"]
netmask = ip_info["netmask"]

network = ipaddress.IPv4Network(f"{ip_addr}/{netmask}", strict=False)
target = str(network)

print(f"[+] IDS Running on {target}")
send_event("IDS_START", ip_addr, "", target, 0)


# -----------------------------
# SCAN FUNCTION
# -----------------------------
def scan():
    arp = ARP(pdst=target)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    pkt = ether / arp

    ans = srp(pkt, timeout=2, verbose=False)[0]

    devices = {}
    for _, r in ans:
        devices[r.psrc] = r.hwsrc

    return devices


# -----------------------------
# STATE
# -----------------------------
trusted = scan()
mac_history = defaultdict(set)

print("\n[+] Initial Devices:")
for ip, mac in trusted.items():
    print(ip, "->", mac)
    send_event("INITIAL_DEVICE", ip, mac)


print("\n[+] IDS Running...\n")


# -----------------------------
# MAIN LOOP
# -----------------------------
while True:
    time.sleep(5)
    current = scan()

    # NEW DEVICE
    for ip, mac in current.items():
        if ip not in trusted:
            print(f"[NEW DEVICE] {ip}")
            send_event("NEW_DEVICE", ip, mac, "new device detected", 5)

        trusted[ip] = mac

    # ARP SPOOF DETECTION
    for ip, mac in current.items():
        mac_history[ip].add(mac)

        if len(mac_history[ip]) > 1:
            print(f"[ALERT] ARP SPOOF: {ip}")
            send_event("ARP_SPOOF", ip, mac, str(mac_history[ip]), 20)