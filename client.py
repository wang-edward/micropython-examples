import network
import socket
import time
try:
    import secrets    # this is the file you pushed from your PC
except ImportError:
    raise RuntimeError("Missing secrets.py! Generate it from env vars on your PC.")

# — Connect to Wi-Fi —
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
while not wlan.isconnected():
    time.sleep_ms(100)
print("Wi-Fi up:", wlan.ifconfig())

# — TCP server as before —
addr = socket.getaddrinfo("0.0.0.0", 5000)[0][-1]
srv = socket.socket()
srv.bind(addr)
srv.listen(1)
print("Listening on", addr)

while True:
    cl, remote = srv.accept()
    print("Client:", remote)
    while True:
        data = cl.recv(512)
        if not data:
            break
        print("Got:", data)
        cl.send(b"ACK")
    cl.close()
    print("Closed")
