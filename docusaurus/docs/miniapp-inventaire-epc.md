---
id: miniapp-inventaire-epc
title: Mini-app 1 - Inventaire EPC
---

# Mini-app 1 - Inventaire EPC

But: détecter les tags présents dans le champ antenne et afficher leurs EPC.

## 1) À quoi sert cette mini-app

- Vérifier que la chaîne RF fonctionne (lecteur + antenne + tag)
- Confirmer la communication série
- Obtenir la liste des tags détectés avant lecture capteur

## 2) Script prêt à l'emploi

```python
import serial
import time

PORT = "COM3"            # A adapter
BAUDRATE = 57600          # A adapter
QUERY_CMD_HEX = "06 01 01 04 00 83 7C"  # Exemple RU5417


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
                print("Aucune trame reçue")

            time.sleep(0.5)


if __name__ == "__main__":
    main()
```

## 3) Ce que vous devez voir

- Des trames RX qui varient quand vous approchez/éloignez un tag
- Plus de réponses quand le tag est proche et bien orienté

## 4) Causes fréquentes si aucun tag n'est vu

- Antenne non branchée ou mal serrée
- Puissance lecteur trop faible
- Tag hors champ ou mal orienté
- Mauvais port COM / mauvaise vitesse série

### 📷 Illustration recommandée
Photo comparant un “bon positionnement tag/antenne” et un “mauvais positionnement”.
