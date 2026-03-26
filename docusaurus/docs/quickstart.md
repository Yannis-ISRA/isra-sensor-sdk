---
id: quickstart
title: Démarrage rapide (10 min)
---

# Démarrage rapide (FR)

Ce guide est pensé pour les intégrateurs terrain (électrotechnique / électromécanique).

Objectif: avoir un premier script qui détecte un tag UHF puis prépare la lecture Temp/Hum.

## 1) Ce que vous allez faire

- Brancher un lecteur UHF en **RS232**
- Vérifier le port série Windows
- Lancer une mini-app Python de test
- Préparer la suite (lecture Temp/Hum)

## 2) Pourquoi on commence en RS232

On trouve du RS232 sur la majorité des lecteurs, c'est le plus simple pour démarrer.

- **RS232**: point à point, mise en service rapide, idéal banc de test
- **RS485**: plus robuste en environnement bruité, bus multi-équipements
- **IP (TCP/UDP)**: pratique en réseau IT/OT, supervision distante

Bonne nouvelle: la logique logicielle reste très proche (trames/CRC/parsing identiques). On change surtout la couche transport.

## 3) Matériel recommandé

- PC Windows 11
- Lecteur UHF compatible
- Antenne UHF + câble coaxial adapté
- Tag capteur ISRA
- **Adaptateur USB-série FTDI recommandé**

> ⚠️ Retour terrain: certains adaptateurs low-cost (souvent chipsets clones/CH340) peuvent poser des problèmes sur Windows 11 (port instable, erreurs d'ouverture). FTDI est généralement plus stable.

### 📷 Illustration recommandée
Photo “kit minimum” sur table: lecteur + antenne + câble USB-série FTDI + tag.

## 4) Préparation logicielle

```bash
pip install pyserial
```

## 5) Script de test inventaire EPC (copier-coller)

```python
import serial
import time

PORT = "COM3"        # A adapter
BAUDRATE = 57600      # A adapter selon lecteur
QUERY_CMD_HEX = "06 01 01 04 00 83 7C"  # Exemple type RU5417

def hex_to_bytes(s):
    return bytes.fromhex(s.replace(" ", ""))

def main():
    with serial.Serial(PORT, BAUDRATE, timeout=0.2) as ser:
        print(f"Connecté sur {PORT} @ {BAUDRATE}")

        cmd = hex_to_bytes(QUERY_CMD_HEX)
        ser.write(cmd)
        time.sleep(0.15)

        data = ser.read(ser.in_waiting or 128)
        if data:
            print("RX:", " ".join(f"{b:02X}" for b in data))
        else:
            print("Aucune réponse. Vérifier câblage, port, vitesse, antenne, présence tag.")

if __name__ == "__main__":
    main()
```

### 🎬 Capture écran conseillée
Capture terminal avec une trame RX valide (pour rassurer l'intégrateur sur le “premier succès”).

## 6) Avant de continuer

Validez ces 4 points:

- Port COM visible dans Windows
- Aucun conflit applicatif sur le port
- Antenne connectée avant émission
- Tag présent dans le champ

## 7) Suite du parcours

- [Guide d’intégration](integration-guide)
- [Mini-app 1: Inventaire EPC](miniapp-inventaire-epc)
- [Mini-app 2: Lecture Temp/Hum](miniapp-lecture-temp-hum)
- [Mini-app 3: Export et intégration industrielle](miniapp-export-integration)
- [Diagnostic & dépannage](diagnostic-depannage)




