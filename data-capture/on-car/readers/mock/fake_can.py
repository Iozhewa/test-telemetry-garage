#!/usr/bin/env python3
"""
Mock CAN sender.

Simulate's an ECU sending engine sensor data, sending
a fake "engine RPM" message and fake "coolant temp" message
every 100ms.
"""
import time
import random

class FakeCANBus:
    def __init__(self):
        self.running = True

    def read_message(self, timeout=0.1):
        time.sleep(timeout)
        return {
            "arbitration_id": 0x100,  # mock CAN ID for engine RPM
            "data": bytes([0x1F, 0x40]).hex(),  # 8000 in 2 bytes
            "timestamp": time.time(),
            "dlc": 2
        }

if __name__ == "__main__":
    bus = FakeCANBus()
    for _ in range(0, 5):
        message = bus.read_message()
        print(message)