---
id: diagnostic-depannage
title: Troubleshooting
---

# Troubleshooting (field)

This page lists the most common issues seen during commissioning.

## 1) No COM port detected

**Probable causes**
- Missing or wrong USB-serial driver
- Faulty adapter
- Poor USB cable quality

**Recommended actions**
- Check Device Manager
- Reinstall chipset driver
- Test with validated **FTDI** adapter

## 2) COM port exists but cannot be opened

**Probable causes**
- Port already used by another app
- Wrong serial settings
- Unstable low-cost adapter

**Recommended actions**
- Close all other serial tools
- Check baudrate/parity/stopbits
- Replace adapter (FTDI)

## 3) Empty or random RX frames

**Probable causes**
- Wrong RX/TX/GND wiring
- Wrong baudrate
- EMC disturbances

**Recommended actions**
- Verify actual vendor pinout
- Test with short cable first
- Use shielded cable and proper grounding

## 4) No tag detected

**Probable causes**
- Antenna disconnected
- Reader power too low
- Tag out of field / bad orientation

**Recommended actions**
- Check RF connectors
- Reposition antenna/tag
- Validate EPC inventory first

## 5) Wrong Temp/Hum values

**Probable causes**
- Wrong response parsing
- Wrong memory word conversion
- Incomplete read (timeout)

**Recommended actions**
- Log raw RX frames
- Check word order (endianness)
- Add retry + explicit timeout handling

## 6) Quick table “Symptom -> Action”

| Symptom | Action 1 | Action 2 |
| :--- | :--- | :--- |
| COM missing | Reinstall driver | Test another cable/adapter |
| COM busy | Close serial tools | Restart PC if needed |
| No tag | Check antenna | Reposition tag |
| Unstable values | Enable RX/TX logs | Verify conversion |

### 📷 Recommended illustration
Annotated photo of correct serial wiring + Device Manager screenshot.
