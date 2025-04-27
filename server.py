import socket

ESP32_IP   = '192.168.1.42'  # replace with your ESP32’s IP
ESP32_PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ESP32_IP, ESP32_PORT))
    payload = b'My HIL test vector\n'
    s.sendall(payload)
    # Optional: read the ESP32’s response
    resp = s.recv(512)
    print('ESP32 replied:', resp)
