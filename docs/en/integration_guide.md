# ISRA Sensor Integration Guide for Industry

Welcome to the **ISRA Sensor RFID** ecosystem.
This guide is designed for automation engineers, technicians, and system integrators who need battery-free wireless sensing in industrial environments.

---

## System Architecture

The ISRA system is built around 3 simple blocks:

1. **ISRA Sensor**: Installed on your asset (motor, cable, container). It measures temperature/humidity with **no battery**.
2. **UHF Reader**: Sends energy to power the sensor and receives back the sensor data.
3. **ISRA SDK**: Runs on PC/Server/PLC gateway and converts raw radio values into engineering values (°C, %).

---

## Choosing a Communication Interface

| Interface | Max Distance | Main Benefit | Recommended Use |
| :--- | :--- | :--- | :--- |
| **RS-232** | 15 m | Simple / Standard | Direct connection to one PC. |
| **RS-485** | 1200 m | Multi-reader bus | Factory floors and long distances. |
| **Ethernet/IP** | 100 m+ | Standard networking | Existing IT/OT network integration. |

---

## RS-485 Wiring Tips

In industrial environments, electrical noise is common:

- Use a **shielded twisted pair** cable.
- Verify A/B polarity on the ISRA reader.
- For long buses (>100 m), add a **120 Ω termination resistor** on the last device.

---

## Data Exploitation

### CSV / Excel Logging
Store measurements into `.csv` files for traceability and reporting.

### PLC / Automation
Use JSON file exchange or a gateway (Modbus/MQTT) for PLC or SCADA integration.

### Web Supervision
Push live data into dashboards for real-time monitoring on desktop, tablet, or mobile.
