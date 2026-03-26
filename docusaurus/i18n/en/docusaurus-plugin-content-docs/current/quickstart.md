---
id: quickstart
title: Quickstart (10 min)
slug: /
---

# Quickstart (EN)

This guide is written for field integrators (electrotechnical / electromechanical profile).

Goal: run a first working script to detect a UHF tag, then prepare temperature/humidity reading.

## 1) What you will do

- Connect a UHF reader in **RS232**
- Check Windows serial port
- Run a simple Python mini-app
- Prepare next step (Temp/Hum reading)

## 2) Why we start with RS232

RS232 is available on most readers and is the easiest way to start.

- **RS232**: point-to-point, fast commissioning
- **RS485**: stronger in noisy environments, multi-device bus
- **IP (TCP/UDP)**: practical for IT/OT network integration

Good news: software logic stays very similar (frames/CRC/parsing). Only transport layer changes.

## 3) Recommended hardware

- Python 3.10+
- A compatible UHF reader
- UHF antenna + proper coax cable
- ISRA sensor tag
- **FTDI USB-serial adapter recommended**

> ⚠️ Field feedback: some low-cost adapters (often clone/chinese chipsets) can be unstable on Windows 11. FTDI is usually more reliable.

### 📷 Recommended illustration
“Minimum kit” photo: reader + antenna + FTDI USB-serial + tag.

## 4) Software setup

```bash
pip install pyserial
```

## 5) EPC inventory test script (copy/paste)

```python
import serial
import time

PORT = "COM3"        # Adjust
BAUDRATE = 57600      # Adjust to your reader
QUERY_CMD_HEX = "06 01 01 04 00 83 7C"  # RU5417-style example

def hex_to_bytes(s):
    return bytes.fromhex(s.replace(" ", ""))

def main():
    with serial.Serial(PORT, BAUDRATE, timeout=0.2) as ser:
        print(f"Connected on {PORT} @ {BAUDRATE}")

        cmd = hex_to_bytes(QUERY_CMD_HEX)
        ser.write(cmd)
        time.sleep(0.15)

        data = ser.read(ser.in_waiting or 128)
        if data:
            print("RX:", " ".join(f"{b:02X}" for b in data))
        else:
            print("No response. Check wiring, COM port, baudrate, antenna, tag presence.")

if __name__ == "__main__":
    main()
```

### 🎬 Recommended screenshot
Terminal screenshot with a valid RX frame.

## 6) Before going further

Validate these 4 points:

- COM port is visible in Windows
- No other app is locking serial port
- Antenna is connected before RF transmission
- Tag is inside reading field

## 7) Next steps

- [Integration guide](integration-guide)
- [Mini-app 1: EPC inventory](miniapp-inventaire-epc)
- [Mini-app 2: Temp/Hum reading](miniapp-lecture-temp-hum)
- [Mini-app 3: Export & industrial integration](miniapp-export-integration)
- [Troubleshooting](diagnostic-depannage)
