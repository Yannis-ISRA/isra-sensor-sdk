# Quickstart (EN)

This guide helps you start quickly with the ISRA SDK.

## 1) Prerequisites

- Python 3.10+
- A compatible UHF reader
- An ISRA sensor (known EPC)

## 2) Installation

```bash
pip install pyserial
```

## 3) First test

```bash
python examples/read_to_json.py
```

The script prints JSON measurements in a loop.

## 4) Adapt to your setup

In `examples/read_to_json.py`:

- Update the serial port (`COM3` / `/dev/ttyUSB0`)
- Replace `target_epc` with your real sensor EPC

## 5) Next steps

- [Integration Guide EN](integration_guide.md)
- [AI reader adaptation prompt](reader_adaptation_prompt.md)
