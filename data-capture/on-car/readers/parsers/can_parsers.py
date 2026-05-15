#!/usr/bin/env python3
"""
Sensor translators.

Each function to take CAN message in raw bytes, decoding
measured values (degrees, kPa, rpm, etc.)

Working with placeholder byte formats until Database CAN
file is provided (that is, need more ECU info).
"""

def parse_sensor(data:bytes) -> float:
    """
    Sensor Name (Abbrev.)
    Expects 2 bytes. Returns unit in SI.

    Placeholder formula to verify against ECU datasheet
    """
    raw = data[0]
    conversion = lambda x: x
    standardized = conversion(raw)
    return standardized
def test_sensor():
    testBytes = bytes([75, 0])
    result = parse_sensor(testBytes)
    print(f"Sensor data: {result} units")
    assert result == 75  # Or other expected value
