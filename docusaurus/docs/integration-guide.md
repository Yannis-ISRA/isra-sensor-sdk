---
id: integration-guide
title: Guide d’intégration
---

# Guide d'intégration terrain (RS232, RS485, IP)

Ce guide est orienté intégrateurs terrain.

Objectif: comprendre rapidement comment intégrer des capteurs UHF ISRA dans un système industriel réel.

## 1) Architecture fonctionnelle simple

1. **Capteur ISRA**
2. **Lecteur UHF**
3. **Mini-app Python** (acquisition)
4. **Système client** (SCADA, PLC, cloud, base de données)

### 🧭 Schéma recommandé
`Capteur -> Lecteur UHF -> Mini-app -> Modbus/MQTT/OPC UA/REST -> Supervision`

### 📷 Illustration recommandée
Schéma bloc très simple avec flèches et protocoles (1 slide suffit).

## 2) Comparatif des connectiques

| Interface | Distance Max | Usage |
| :--- | :--- | :--- |
| RS-232 | 15 m | Liaison directe |
| RS-485 | 1200 m | Multi-lecteurs |
| Ethernet/IP | 100 m+ | Réseau IT/OT |

### Pourquoi on fait les cas pratiques en RS232

- Très répandu sur les lecteurs du marché
- Diagnostic rapide (port COM visible)
- Mise en service facile pour un premier POC

### Pourquoi l'adaptation RS485/IP reste simple

Dans la plupart des cas, le **protocole lecteur** (trame, CRC, parsing, format de réponse) ne change pas.

Ce qui change surtout:
- la **couche transport** (port série vs socket TCP/UDP),
- la gestion d'adressage/topologie (surtout en RS485).

Donc on réutilise le même coeur logiciel et on adapte l'I/O.

## 3) Choix du câble série (très important)

### Recommandation principale

- Utiliser un adaptateur USB-série à chipset **FTDI**.

### Retour terrain Windows 11

Certains adaptateurs low-cost (souvent clones/chipsets chinois) peuvent provoquer:
- port COM instable,
- erreurs d'ouverture,
- timeouts intermittents,
- comportement aléatoire sous charge.

### Checklist câble / driver

- Vérifier le chipset dans le gestionnaire de périphériques
- Installer le driver officiel
- Éviter les hubs USB non alimentés
- Utiliser un câble court et blindé
- Valider une référence unique pour vos projets

### 📷 Illustration recommandée
Capture gestionnaire de périphériques montrant un adaptateur FTDI reconnu.

## 4) Interfaçage avec les systèmes industriels

Une fois les mesures Temp/Hum récupérées, vous pouvez les publier vers:

- **Modbus RTU/TCP**: intégration automate / PLC
- **MQTT**: IIoT, brokers, cloud/on-prem
- **OPC UA**: interopérabilité supervision industrielle
- **REST API**: applications métier / dashboard web
- **CSV / SQL**: historisation qualité / traçabilité

### 🎬 Capture écran conseillée
Exemple de dashboard (température, humidité, alarme seuil) alimenté par la mini-app.

## 5) Parcours recommandé

1. [Démarrage rapide](quickstart)
2. [Mini-app 1: Inventaire EPC](miniapp-inventaire-epc)
3. [Mini-app 2: Lecture Temp/Hum](miniapp-lecture-temp-hum)
4. [Mini-app 3: Export & intégration](miniapp-export-integration)
5. [Diagnostic & dépannage](diagnostic-depannage)
6. [Checklist de mise en service](checklist-commissioning)
