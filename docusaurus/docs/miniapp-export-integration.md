---
id: miniapp-export-integration
title: Mini-app 3 - Export & intégration industrielle
---

# Mini-app 3 - Export & intégration industrielle

But: transformer vos mesures en données exploitables par un automate, une supervision ou un SI.

## 1) Sortie JSON locale (base simple)

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

print("Mesure exportée")
```

## 2) Export CSV (très demandé en atelier)

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

print("CSV mis à jour")
```

## 3) Passerelles industrielles recommandées

- **Modbus RTU/TCP**: publication de registres vers PLC
- **MQTT**: envoi vers broker IIoT
- **OPC UA**: interopérabilité supervision
- **REST API**: intégration SI / application web

## 4) Exemple MQTT minimal

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

print("MQTT publié")
```

> Astuce: démarrez d'abord avec CSV/JSON, puis ajoutez Modbus/MQTT quand la lecture capteur est stable.

### 📷 Illustration recommandée
Schéma “lecteur -> mini-app -> MQTT broker -> dashboard”.
