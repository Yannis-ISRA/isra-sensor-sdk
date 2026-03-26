---
id: miniapp-inventaire-epc
title: Mini-app 1 - EPC Inventory
---

# Mini-app 1 - EPC Inventory

Goal: detect tags in antenna field and display EPC values.

## 1) Why this mini-app matters

- Validate RF chain (reader + antenna + tag)
- Validate serial communication
- Get visible tags before sensor memory reading

## 2) Ready-to-run script

```python
import serial
import time

PORT = "COM3"            # Adjust
BAUDRATE = 57600          # Adjust
QUERY_CMD_HEX = "06 01 01 04 00 83 7C"  # RU5417 example


def hex_to_bytes(hex_str: str) -> bytes:
    return bytes.fromhex(hex_str.replace(" ", ""))


def bytes_to_hex(data: bytes) -> str:
    return " ".join(f"{b:02X}" for b in data)


def main():
    print("=== Mini-app EPC Inventory ===")
    print(f"Port={PORT}  Baudrate={BAUDRATE}")

    with serial.Serial(PORT, BAUDRATE, timeout=0.2) as ser:
        cmd = hex_to_bytes(QUERY_CMD_HEX)

        while True:
            ser.write(cmd)
            time.sleep(0.15)

            rx = ser.read(ser.in_waiting or 128)
            if rx:
                print("RX:", bytes_to_hex(rx))
            else:
                print("No frame received")

            time.sleep(0.5)


if __name__ == "__main__":
    main()
```

## 3) Expected behavior

- RX frames should change when tag moves in/out of field
- More stable answers when tag is well oriented

## 4) If no tag is detected

- Antenna disconnected or loose
- Reader power too low
- Tag out of field / bad orientation
- Wrong COM port / wrong baudrate

### 📷 Recommended illustration
Photo showing “good tag/antenna position” vs “bad position”.
