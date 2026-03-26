---
id: miniapp-lecture-temp-hum
title: Mini-app 2 - Lecture Température / Humidité
---

# Mini-app 2 - Lecture Température / Humidité

But: lire les données capteur depuis la mémoire USER du tag et convertir en valeurs physiques.

## 1) Prérequis

- Mini-app inventaire EPC validée
- EPC d'un tag connu
- Paramètres lecteur validés (port/vitesse)

## 2) Principe simplifié

1. Inventorier un tag
2. Lire un bloc de mots mémoire USER
3. Appliquer la conversion capteur
4. Afficher Temp °C et Hum %

## 3) Script de base (structure)

> Le format exact des trames dépend de votre lecteur. Gardez la structure, adaptez `build_read_cmd` et `parse_read_response`.

```python
import serial

PORT = "COM3"
BAUDRATE = 57600
EPC_HEX = "30 00 11 22 33 44 55 66 77 88 99 AA"


def build_read_cmd(epc_hex: str) -> bytes:
    # TODO: adapter à votre protocole lecteur
    # lecture USER bank, start=0x00, count=0x07
    raise NotImplementedError


def parse_read_response(data: bytes) -> bytes:
    # TODO: extraire la zone DATA utile (14 octets pour 7 mots)
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
        print(f"Humidite:   {hum_p:.2f} %")


if __name__ == "__main__":
    main()
```

## 4) Validation terrain

- Approcher la main du tag: la température doit évoluer
- Changer l'environnement (air plus humide/sec): l'humidité doit bouger progressivement

### 🎬 Capture écran conseillée
Capture terminal avec 3 lectures successives montrant l'évolution des valeurs.
