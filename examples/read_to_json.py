#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ISRA Industrial Example: Reading an ISRA sensor and outputting JSON.
Simple, robust and ready to be integrated into third-party software.
"""

import sys
import os
import time

# Allow importing the SDK from the local directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sdk')))

from isra_readers import SerialTransport, RU5417Reader
from isra_sdk_core import IsraSensor

def main():
    # 1. Transport configuration (update with your hardware port)
    # Could be /dev/ttyUSB0 on Linux or COM3 on Windows
    try:
        transport = SerialTransport(port="COM3", baudrate=57600)
        reader = RU5417Reader(transport)
    except Exception as e:
        print(f"ERROR: Could not connect to reader. Check wiring. ({e})")
        return

    # 2. Target sensor ID (EPC)
    # Replace with your actual ISRA sensor EPC
    target_epc = "E280 1105 5000 0042 1234 5678"

    print(f"--- Monitoring ISRA Sensor {target_epc} ---")
    print("Press Ctrl+C to stop.")

    try:
        sensor = IsraSensor(reader, target_epc)
        
        while True:
            # Get data in standard JSON format
            json_data = sensor.to_json()
            print(json_data)
            
            # Wait 2 seconds between readings
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        transport.close()
        print("Reader disconnected.")

if __name__ == "__main__":
    main()
