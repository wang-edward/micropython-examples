# esp32_rest.py
from microdot import Microdot, Response
from machine import Pin
from neopixel import NeoPixel
import network, time, secrets

# — Wi-Fi setup (as before) —
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
while not wlan.isconnected():
    time.sleep_ms(100)
print("Wi-Fi up:", wlan.ifconfig())

# — NeoPixel setup —
pin = Pin(48, Pin.OUT)
pixels = NeoPixel(pin, 1)
pixels[0] = (0,0,0)
pixels.write()

# — REST app —
app = Microdot()
Response.default_content_type = 'application/json'

@app.post('/led')
def led(req):
    cmd = req.json.get('cmd','').strip().upper()
    if cmd == 'LED ON':
        pixels[0] = (0,255,0)
        pixels.write()
        return {'status':'OK'}
    elif cmd == 'LED OFF':
        pixels[0] = (0,0,0)
        pixels.write()
        return {'status':'OK'}
    else:
        return {'status':'ERR','error':'unknown command'}, 400

app.run(host='0.0.0.0', port=80)
