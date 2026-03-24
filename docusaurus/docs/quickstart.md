---
id: quickstart
title: Quickstart
---

# Quickstart (FR)

Ce guide permet de démarrer rapidement avec le SDK ISRA.

## Présentation du projet

Le projet **ISRA Sensor SDK** fournit une documentation d’intégration claire pour l’usage industriel de capteurs RFID UHF (température/humidité), avec une approche simple à maintenir :

- documentation technique orientée intégration
- structure bilingue FR/EN
- déploiement automatique via GitHub Pages

## 1) Prérequis

- Python 3.10+
- Un lecteur UHF compatible
- Un capteur ISRA (EPC connu)

## 2) Installation

```bash
pip install pyserial
```

## 3) Premier test

```bash
python ../examples/read_to_json.py
```

## 4) Aller plus loin

- [Guide d’intégration](integration-guide)
- [Prompt IA adaptation lecteur](reader-adaptation-prompt)
