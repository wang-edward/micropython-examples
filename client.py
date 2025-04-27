from machine import Pin
from neopixel import NeoPixel
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

# pin
pin = Pin(48, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
pixels = NeoPixel(pin, 1)   # create NeoPixel driver on GPIO0 for 8 pixels
pixels[0] = [0, 0, 0]
pixels.write()

while True:
    cl, remote = srv.accept()
    print("Client:", remote)
    while True:
        data = cl.recv(512)
        if not data:
            break
        print("Got:", data)
        cmd = data.strip().upper()
        if cmd == b"LED ON":
            pixels[0] = [0, 255, 0]
            pixels.write()
            cl.send(b"OK")
        elif cmd == b"LED OFF":
            pixels[0] = [0, 0, 0]
            pixels.write()
            cl.send(b"OK")
        else:
            cl.send(b"ERR")


    cl.close()
    print("Closed")
