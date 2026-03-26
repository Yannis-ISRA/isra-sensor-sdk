---
id: miniapp-lecture-temp-hum
title: Mini-app 2 - Temperature / Humidity Reading
---

# Mini-app 2 - Temperature / Humidity Reading

Goal: read sensor data from tag USER memory and convert it to physical values.

## 1) Prerequisites

- EPC inventory mini-app is working
- One known EPC tag
- Reader serial settings validated

## 2) Simplified workflow

1. Inventory one tag
2. Read USER memory words
3. Apply sensor conversion
4. Display Temp °C and Hum %

## 3) Base script (template)

> Exact frame format depends on your reader. Keep this structure, adapt `build_read_cmd` and `parse_read_response`.

```python
import serial

PORT = "COM3"
BAUDRATE = 57600
EPC_HEX = "30 00 11 22 33 44 55 66 77 88 99 AA"


def build_read_cmd(epc_hex: str) -> bytes:
    # TODO: adapt to your reader protocol
    # USER bank, start=0x00, count=0x07
    raise NotImplementedError


def parse_read_response(data: bytes) -> bytes:
    # TODO: extract useful DATA payload (14 bytes for 7 words)
    raise NotImplementedError


def parse_calib(word: int) -> float:
    value = word & 0x1FFF
    div_exp = (word >> 14) & 0x03
    return value / (2 ** div_exp)


def convert_temp_hum(raw_data: bytes):
    words = []
    for i in range(0, len(raw_data), 2):
        words.append((raw_data[i] << 8) | raw_data[i + 1])

    acq_sens = words[0]
    acq_temp = words[1]
    acq_sens_30 = words[2]
    acq_sens_70 = words[3]
    acq_temp_60 = words[4]
    acq_temp_30 = words[6]

    t_raw = parse_calib(acq_temp)
    h_raw = parse_calib(acq_sens)
    t_30 = parse_calib(acq_temp_30)
    t_60 = parse_calib(acq_temp_60)
    h_30 = parse_calib(acq_sens_30)
    h_70 = parse_calib(acq_sens_70)

    temp_c = 30 + 30 * (t_raw - t_30) / (t_60 - t_30) if (t_60 - t_30) else 0.0
    hum_p = 30 + 40 * (h_raw - h_30) / (h_70 - h_30) if (h_70 - h_30) else 0.0
    return temp_c, hum_p


def main():
    with serial.Serial(PORT, BAUDRATE, timeout=0.3) as ser:
        cmd = build_read_cmd(EPC_HEX)
        ser.write(cmd)
        rx = ser.read(ser.in_waiting or 256)

        payload = parse_read_response(rx)
        temp_c, hum_p = convert_temp_hum(payload)
        print(f"Temperature: {temp_c:.2f} °C")
        print(f"Humidity:    {hum_p:.2f} %")


if __name__ == "__main__":
    main()
```

## 4) Field validation

- Put your hand near the tag: temperature should move
- Change ambient conditions: humidity should evolve gradually

### 🎬 Recommended screenshot
Terminal capture with 3 successive measurements showing evolution.
