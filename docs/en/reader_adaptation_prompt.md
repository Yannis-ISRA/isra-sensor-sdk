# 🚀 UHF Reader Driver Creation Assistant

**Version:** ISRA SDK v1.0  
**Purpose:** Copy this prompt into ChatGPT or Claude to transform any reader technical documentation into a Python driver compatible with the ISRA ecosystem.

---

## 📝 PROMPT TO COPY

> "Act as an expert in hardware communication protocol development (RS232/TCP). I want to create a Python driver for a new UHF RFID reader.
>
> The driver must inherit from `BaseReader` and implement:
> `read_user_bank(self, epc, start_word, word_count)`.
>
> Protocol constraints:
> 1. The frame must include a length field at the beginning.
> 2. The CRC must use [CRC NAME].
> 3. The reader default address is [ADDRESS].
>
> **Here is the reader technical documentation:**
> [PASTE TECHNICAL DOC TEXT OR PDF CONTENT HERE]
>
> **Task:**
> Provide full Python code for a class named `MyNewReader` that uses `self.transport.send()` and `self.transport.receive()` to read USER bank (Bank 3) and retrieve ISRA sensor data."

---

## 🛠 Integrator Tips

- Identify the exact **CRC variant** in the documentation (often CRC-16/MCRF4XX or CRC-16/CCITT).
- Check whether the reader expects **hexadecimal** payloads or **binary** payloads.
- Once generated, place your code in `sdk/isra_readers.py`.
