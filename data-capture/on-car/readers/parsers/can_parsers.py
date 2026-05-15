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

def parse_steering_angle(data:bytes) -> float:
    """
    Steering Angle Parser (for SAS)
    Expects _ bytes. Returns turn (1 tr = 360 deg).
    https://www.delphiautoparts.com/resource-center/article/making-sense-of-sensors-steering-angle-sensor

    Verify against ECU datasheet
    """
    raw = data[0]
    toTurn = lambda degrees: degrees/360
    standard = toTurn(raw)
    return standard
def test_steering_angle():
    testBytes = bytes([45, 90])
    result = parse_steering_angle(testBytes)
    print(f"Steering Angle: {round(result, 2)} turn")
    assert result == 0.125, f"Result was {round(result, 3)} and not ~0.125"

def parse_suspension_potentiometer(data:bytes) -> float:
    """
    Suspension Potentiometer Parser (for SP)
    Expects _ bytes. Returns cm.
    https://www.datamc.org/data-acquisition/adding-sensors/suspension-potentiometers/

    Verify against ECU datasheet
    """
    raw = data[0]
    toCm = lambda mm: mm / 10
    standard = toCm(raw)
    return standard
def test_suspension_potentiometer():
    testBytes = bytes([10, 20])
    result = parse_suspension_potentiometer(testBytes)
    print(f"Suspension Potentiometer: {round(result, 2)} cm")
    assert result == 1.0, f"Result was {round(result, 2)} and not ~0.1"

def parse_wheel_speed(data:bytes) -> float:
    """
    Wheel Speed Parser (for WS)
    Expects _ bytes. Returns m/s.
    https://premierautotrade.com.au/news/wheel-speed-sensors%E2%80%93more-than-just-abs.php

    Verify against ECU datasheet
    """
    raw = data[0]
    toMS = lambda kmh: kmh / 3.6
    standard = toMS(raw)
    return standard
def test_wheel_speed():
    testBytes = bytes([1, 10])
    result = parse_wheel_speed(testBytes)
    print(f"Wheel Speed: {round(result, 2)} m/s")
    assert round(result, 3) == round(0.277778, 3), f"Result was {round(result, 3)} and not ~{round(0.277778, 3)}"
