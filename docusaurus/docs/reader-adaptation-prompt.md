---
id: reader-adaptation-prompt
title: Prompt IA adaptation lecteur
---

# Prompt IA – Adapter un nouveau lecteur UHF

Cette page vous aide à adapter rapidement votre code si vous changez de modèle de lecteur.

## 1) Principe

Le plus important est de **séparer**:

- la couche transport (RS232 / RS485 / TCP),
- la couche protocole (trames, CRC, parsing réponse),
- la couche métier (température / humidité / export).

Si cette séparation est propre, changer de lecteur devient simple.

## 2) Prompt recommandé (copier-coller)

```text
Act as a senior industrial communication engineer.

I need a Python driver for a UHF RFID reader used with ISRA temperature/humidity tags.

Constraints:
- Keep business logic independent from transport layer.
- Transport can be RS232, RS485 (serial), or TCP socket.
- Protocol frames have: [LEN][ADDR][CMD][DATA][CRC].
- CRC algorithm: [CRC_NAME].
- Default reader address: [ADDR_HEX].
- Provide robust timeout and retry handling.

Expected output:
1) A `Transport` abstraction (`send_bytes`, `receive_bytes`).
2) A concrete `SerialTransport` and optional `TcpTransport`.
3) A `ReaderProtocol` class with methods:
   - `build_inventory_cmd()`
   - `build_read_user_cmd(epc, start_word, word_count)`
   - `parse_inventory_response(data)`
   - `parse_read_response(data)`
4) A runnable example script that:
   - inventories tags,
   - reads user bank,
   - prints temp/hum values.
5) Clear comments for field technicians.
```

## 3) Ce qu'il faut vérifier dans le code généré

- Longueur de trame correcte
- Endianness CRC correcte
- Timeouts réalistes (atelier)
- Erreurs lisibles (pas uniquement des codes bruts)
- Logs RX/TX activables

## 4) Bonnes pratiques terrain

- Tester d'abord en RS232 avec adaptateur FTDI
- Valider l'inventaire EPC avant la lecture mémoire
- Garder une commande de diagnostic simple dans le script

### 📷 Illustration recommandée
Capture d'un terminal avec TX/RX coloré + exemple d'erreur claire (“timeout lecture capteur B”).
