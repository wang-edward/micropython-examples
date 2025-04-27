import socket
import time
import pytest

ESP32_IP   = "192.168.1.25"
ESP32_PORT = 5000
TIMEOUT    = 2  # seconds

def send_command(cmd: bytes) -> bytes:
    """Open a fresh connection, send cmd (with newline), return the reply."""
    with socket.create_connection((ESP32_IP, ESP32_PORT), timeout=TIMEOUT) as s:
        s.sendall(cmd + b"\n")
        return s.recv(100).strip()


def test_led_on_off_sequence():
    """Toggle onboard LED (requires your ESP32 code to handle these)."""
    # turn LED on
    resp_on = send_command(b"LED ON")
    assert resp_on == b"OK"
    time.sleep(1)  # give it a moment to actually toggle

    # turn LED off
    resp_off = send_command(b"LED OFF")
    assert resp_off == b"OK"
