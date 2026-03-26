---
id: miniapp-export-integration
title: Mini-app 3 - Export & Industrial Integration
---

# Mini-app 3 - Export & Industrial Integration

Goal: convert sensor measurements into data usable by PLC, SCADA or IT systems.

## 1) Local JSON output (simple baseline)

```python
import json
from datetime import datetime

sample = {
    "timestamp": datetime.now().isoformat(timespec="seconds"),
    "sensor_id": "TAG_A",
    "epc": "30 00 11 22 33 44 55 66 77 88 99 AA",
    "temperature_c": 24.7,
    "humidity_pct": 46.2,
}

with open("measurements.json", "a", encoding="utf-8") as f:
    f.write(json.dumps(sample, ensure_ascii=False) + "\n")

print("Measurement exported")
```

## 2) CSV export (very common on site)

```python
import csv
from datetime import datetime

row = [
    datetime.now().isoformat(timespec="seconds"),
    "TAG_A",
    24.7,
    46.2,
]

with open("measurements.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(row)

print("CSV updated")
```

## 3) Recommended industrial bridges

- **Modbus RTU/TCP**: publish registers to PLC
- **MQTT**: send data to IIoT broker
- **OPC UA**: industrial interoperability
- **REST API**: connect business/web apps

## 4) Minimal MQTT example

```python
import json
import paho.mqtt.publish as publish

payload = {
    "sensor": "TAG_A",
    "temperature_c": 24.7,
    "humidity_pct": 46.2,
}

publish.single(
    topic="isra/line1/tag_a",
    payload=json.dumps(payload),
    hostname="192.168.1.10",
    port=1883,
)

print("MQTT published")
```

> Tip: start with CSV/JSON first, then add Modbus/MQTT once sensor reading is stable.

### 📷 Recommended illustration
Diagram: “reader -> mini-app -> MQTT broker -> dashboard”.
