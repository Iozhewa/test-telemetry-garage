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

def parse_brake_pressure(data:bytes) -> float:
    """
    Brake Pressure Parser (for BPS)
    Expects _ bytes. Returns bar.
    https://www.bestech.com.au/blogs/how-pressure-sensors-are-used-in-hydraulic-brake-test-setup/

    Verify against ECU datasheet
    """
    raw = data[0]
    toBar = lambda psi: psi / 14.504
    standard = toBar(raw)
    return standard
def test_brake_pressure():
    testBytes = bytes([14, 28])
    result = parse_brake_pressure(testBytes)
    print(f"Brake Pressure: {round(result, 2)} bar")
    assert round(result) == 1.0, f"Result was {round(result, 2)} and not ~1"

def parse_accelerator_pedal_position(data:bytes) -> float:
    """
    Accelerator Pedal Position Parser (for APPS)
    Expects _ bytes. Returns pedal travel (0-100%).
    https://filmelectronics.in/accelerator-pedal-position-sensor-importance/

    Verify against ECU datasheet
    """
    raw = data[0]
    toTravel = lambda volts: 100*(volts/5)
    standard = toTravel(raw)
    return standard
def test_accelerator_pedal_position():
    testBytes = bytes([1, 3])
    result = parse_accelerator_pedal_position(testBytes)
    print(f"Accelerator Pedal Position: {round(result, 2)}%")
    assert round(result) == 20.0, f"Result was {round(result, 2)} and not ~20"
