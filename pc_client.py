# pc_client.py
import requests
from typing import List, Any, Dict

class HilBox:
    def __init__(self, host: str, timeout: float = 5.0):
        self.base = host.rstrip('/')
        self.sess = requests.Session()
        self.timeout = timeout

    def _post(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base}{path}"
        r = self.sess.post(url, json=payload, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def set_color(self, color: List[int]) -> Dict[str, Any]:
        """
        Set the NeoPixel to an [R, G, B] value.
        """
        if any(not (0 <= c <= 255) for c in color) or len(color) != 3:
            raise ValueError("color must be a list of three 0–255 ints")
        return self._post('/display/color', {'c': color})

    # convenience shortcuts
    def led_on(self) -> Dict[str, Any]:
        return self.set_color([0,255,0])

    def led_off(self) -> Dict[str, Any]:
        return self.set_color([0,0,0])

if __name__ == '__main__':
    box = HilBox('http://192.168.1.25')
    # directly:
    resp = box.set_color([128,0,128])
    print('set_color →', resp)

    # or via helper:
    print('led_on  →', box.led_on())
    print('led_off →', box.led_off())
