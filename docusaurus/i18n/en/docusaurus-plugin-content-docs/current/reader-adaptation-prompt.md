---
id: reader-adaptation-prompt
title: AI Reader Adaptation Prompt
---

# AI Prompt – Adapt a new UHF Reader

Use this page when you need to adapt your software to another reader model.

## 1) Core principle

Keep these layers separated:

- transport layer (RS232 / RS485 / TCP)
- protocol layer (frames, CRC, response parsing)
- business layer (temperature, humidity, export)

If this separation is clean, changing reader becomes much easier.

## 2) Recommended prompt (copy/paste)

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

## 3) What to verify in generated code

- Correct frame length
- Correct CRC endianness
- Realistic field timeouts
- Human-readable error messages
- Optional RX/TX debug logs

## 4) Field best practices

- Start validation in RS232 using FTDI adapter
- Validate EPC inventory before memory reading
- Keep one simple diagnostic command in your script

### 📷 Recommended illustration
Terminal screenshot with TX/RX traces + one explicit timeout message.
