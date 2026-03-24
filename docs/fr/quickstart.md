# Quickstart (FR)

Ce guide permet de démarrer rapidement avec le SDK ISRA.

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
python examples/read_to_json.py
```

Le script affiche des mesures JSON en boucle.

## 4) Adapter à votre installation

Dans `examples/read_to_json.py` :

- Modifiez le port série (`COM3` / `/dev/ttyUSB0`)
- Remplacez `target_epc` par l’EPC réel de votre capteur

## 5) Aller plus loin

- [Guide d’intégration FR](guide_integration.md)
- [Prompt IA adaptation lecteur](reader_adaptation_prompt.md)
