# pc_client.py
import requests

ESP32_HOST = 'http://192.168.1.25'   # your ESP32’s address

def send(cmd: str):
    resp = requests.post(f"{ESP32_HOST}/led", json={'cmd': cmd})
    data = resp.json()
    print(f"{resp.status_code=},", data)

if __name__ == '__main__':
    send('LED ON')   # → turns it on
    send('LED OFF')  # → turns it off
