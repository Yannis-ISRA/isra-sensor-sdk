# ISRA Sensor SDK

SDK Python et documentation d’intégration pour capteurs RFID ISRA (température/humidité) via lecteurs UHF RS-232, RS-485 et Ethernet.

Python SDK and integration documentation for ISRA RFID sensors (temperature/humidity) over UHF readers via RS-232, RS-485, and Ethernet.

---

## 🇫🇷 Français

### Démarrage rapide

1. Installer Python 3.10+.
2. Installer la dépendance série :

```bash
pip install pyserial
```

3. Lancer l’exemple :

```bash
python examples/read_to_json.py
```

### Documentation

- [Portail Documentation](docs/index.md)
- [Quickstart FR](docs/fr/quickstart.md)
- [Guide d’intégration FR](docs/fr/guide_integration.md)
- [Prompt IA d’adaptation lecteur](docs/fr/reader_adaptation_prompt.md)

---

## 🇬🇧 English

### Quick Start

1. Install Python 3.10+.
2. Install serial dependency:

```bash
pip install pyserial
```

3. Run the example:

```bash
python examples/read_to_json.py
```

### Documentation

- [Documentation Portal](docs/index.md)
- [Quickstart EN](docs/en/quickstart.md)
- [Integration Guide EN](docs/en/integration_guide.md)
- [AI Prompt for Reader Adaptation](docs/en/reader_adaptation_prompt.md)

---

## Repository Structure

```text
.
├─ sdk/
│  ├─ isra_sdk_core.py
│  ├─ isra_readers.py
│  └─ __init__.py
├─ examples/
│  └─ read_to_json.py
└─ docs/
   ├─ index.md
   ├─ fr/
   │  ├─ quickstart.md
   │  ├─ guide_integration.md
   │  └─ reader_adaptation_prompt.md
   └─ en/
      ├─ quickstart.md
      ├─ integration_guide.md
      └─ reader_adaptation_prompt.md
```
