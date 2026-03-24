---
id: reader-adaptation-prompt
title: AI Reader Adaptation Prompt
---

# AI Prompt – UHF Reader Adaptation

Copy this prompt into ChatGPT/Claude to generate a Python driver compatible with ISRA.

> Act as an expert in hardware communication protocol development (RS232/TCP). I want to create a Python driver for a new UHF RFID reader.
>
> The driver must inherit from `BaseReader` and implement:
> `read_user_bank(self, epc, start_word, word_count)`.
>
> Protocol constraints:
> 1. The frame must include a length field.
> 2. The CRC must use [CRC NAME].
> 3. The reader default address is [ADDRESS].
>
> Task:
> Provide full Python code for `MyNewReader` using `self.transport.send()` and `self.transport.receive()`.
