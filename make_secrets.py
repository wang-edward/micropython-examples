import os

ssid = os.environ.get("WIFI_SSID")
pwd  = os.environ.get("WIFI_PASSWORD")
if not ssid or not pwd:
    raise RuntimeError("Please set WIFI_SSID and WIFI_PASSWORD")

with open("secrets.py", "w") as f:
    f.write(f'SSID     = {ssid!r}\n')
    f.write(f'PASSWORD = {pwd!r}\n')
print("secrets.py generated")
