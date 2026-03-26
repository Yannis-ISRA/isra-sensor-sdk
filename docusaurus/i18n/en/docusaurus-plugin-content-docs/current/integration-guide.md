---
id: integration-guide
title: Integration Guide
---

# Field Integration Guide (RS232, RS485, IP)

This guide is made for field integrators.

Goal: quickly understand how to connect ISRA UHF sensors into real industrial systems.

## 1) Simple functional architecture

1. **ISRA Sensor**
2. **UHF Reader**
3. **Python mini-app** (data acquisition)
4. **Customer system** (SCADA, PLC, cloud, database)

### 🧭 Recommended diagram
`Sensor -> UHF Reader -> Mini-app -> Modbus/MQTT/OPC UA/REST -> Supervision`

### 📷 Recommended illustration
One simple block diagram with arrows and protocol labels.

## 2) Connection types comparison

| Interface | Max Distance | Usage |
| :--- | :--- | :--- |
| RS-232 | 15 m | Direct link |
| RS-485 | 1200 m | Multi-reader bus |
| Ethernet/IP | 100 m+ | IT/OT network |

### Why practical examples use RS232

- Available on most readers
- Easy commissioning (COM port visible)
- Fast and reliable for first PoC

### Why RS485/IP adaptation is still easy

In most cases, **reader protocol** (frame format, CRC, response parsing) stays the same.

Main changes are:
- **transport layer** (serial port vs TCP/UDP socket)
- addressing/topology management (especially with RS485)

So you can reuse the same protocol/business code and only adapt I/O.

## 3) Serial cable choice (very important)

### Main recommendation

- Use an **FTDI-based** USB-serial adapter.

### Windows 11 field feedback

Some low-cost adapters (often clone/chinese chipsets) can cause:
- unstable COM ports,
- open errors,
- intermittent timeouts,
- random behavior under load.

### Cable / driver checklist

- Check chipset in Device Manager
- Install official driver
- Avoid non-powered USB hubs
- Use short shielded cable
- Validate one known-good reference for projects

### 📷 Recommended illustration
Device Manager screenshot showing a properly recognized FTDI adapter.

## 4) Industrial system interfacing

Once Temp/Hum values are available, publish them to:

- **Modbus RTU/TCP**: PLC integration
- **MQTT**: IIoT broker/cloud/on-prem
- **OPC UA**: industrial interoperability
- **REST API**: business apps / web dashboards
- **CSV / SQL**: quality traceability and reporting

### 🎬 Recommended screenshot
Dashboard example with temperature, humidity and threshold alarm.

## 5) Recommended learning path

1. [Quickstart](quickstart)
2. [Mini-app 1: EPC inventory](miniapp-inventaire-epc)
3. [Mini-app 2: Temp/Hum reading](miniapp-lecture-temp-hum)
4. [Mini-app 3: Export & integration](miniapp-export-integration)
5. [Troubleshooting](diagnostic-depannage)
6. [Commissioning checklist](checklist-commissioning)
