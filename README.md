flashing
```bash
esptool.py erase_flash
esptool.py --baud 460800 write_flash 0 ESP32_GENERIC_S3-20241129-v1.24.1.bin
```

repl
```
picocom /dev/tty.usbserial-130 -b115200
```

run
```
mpremote run main.py
```


update code
```
mpremote connect /dev/tty.usbserial-130 fs cp main.py : # kinda bad
```

https://micropython.org/download/ESP32_GENERIC_S3/
