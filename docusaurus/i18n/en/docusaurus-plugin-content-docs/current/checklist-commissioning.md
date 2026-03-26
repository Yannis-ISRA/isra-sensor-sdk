---
id: checklist-commissioning
title: Commissioning Checklist
---

# Commissioning Checklist

Use this checklist during customer site installation.

## 1) Hardware preparation

- [ ] UHF reader powered and stable
- [ ] Antenna correctly connected
- [ ] **FTDI** USB-serial adapter validated
- [ ] ISRA test tag(s) available

## 2) PC preparation

- [ ] Serial driver installed
- [ ] COM port detected
- [ ] Python installed
- [ ] Dependencies installed (`pyserial` minimum)

## 3) Communication validation

- [ ] EPC inventory mini-app works
- [ ] Coherent RX frames observed
- [ ] No recurring timeout

## 4) Sensor validation

- [ ] Temp/Hum reading works
- [ ] Values plausible and stable
- [ ] Repeatability confirmed (several readings)

## 5) Customer integration validation

- [ ] Output format validated (JSON/CSV)
- [ ] Target protocol validated (Modbus/MQTT/OPC UA/REST)
- [ ] Data visible in supervision
- [ ] Timestamp validation done

## 6) End-of-commissioning deliverables

- [ ] Final script delivered
- [ ] Parameters documented (port, baudrate, address, timeout)
- [ ] Restart procedure provided
- [ ] Troubleshooting procedure provided

### 📷 Recommended illustration
Photo of final installation + supervision screenshot with real-time Temp/Hum.
