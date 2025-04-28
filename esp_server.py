# esp32_server.py

from microdot import Microdot, Response
from machine import Pin
from neopixel import NeoPixel
import network, time
import secrets   # contains SSID, PASSWORD

# — Wi-Fi setup —
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
while not wlan.isconnected():
    time.sleep_ms(100)
print("Wi-Fi up:", wlan.ifconfig())

# — NeoPixel on GPIO48, single pixel —
pin    = Pin(48, Pin.OUT)
pixels = NeoPixel(pin, 1)
pixels[0] = (0,0,0)
pixels.write()

# — REST app —
app = Microdot()
Response.default_content_type = 'application/json'

@app.post('/display/color')
def set_color(req):
    c = req.json.get('c')
    # expect c = [R,G,B]
    if isinstance(c, list) and len(c) == 3:
        try:
            pixels[0] = tuple(int(x) for x in c)
            pixels.write()
            return {'status':'OK'}
        except:
            pass
    return {'status':'ERR','error':'invalid color'}, 400

app.run(host='0.0.0.0', port=80)
