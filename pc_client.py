# pc_client.py

import requests

class Box:
    def __init__(self, host: str):
        self.host = host.rstrip('/')

    def post(self, path: str, data: dict):
        url = f"{self.host}{path}"
        resp = requests.post(url, json=data, timeout=5)
        resp.raise_for_status()
        return resp.json()

if __name__ == '__main__':
    box = Box('http://192.168.1.25')   # replace with your ESP32’s IP
    # example: set to bright purple
    color = [255, 0, 255]
    result = box.post('/display/color', {'c': color})
    print('Response:', result)
