#!/usr/bin/env python3
"""
Sensor translators.

Each function to take CAN message in raw bytes, decoding
measured values (degrees, kPa, rpm, etc.)

Working with placeholder byte formats until Database CAN
file is provided (that is, need more ECU info).
"""

class ParsePackage:
    pass

class TestPackage:
    pass
    def runAll():
        return
        TestPackage.brake_pressure()
        TestPackage.accelerator_pedal_position()
        TestPackage.steering_angle()
        TestPackage.suspension_potentiometer()
        TestPackage.wheel_speed()
        TestPackage.intake_air_temp()
        TestPackage.ambient_air_temp()
        TestPackage.oil_pressure()
        TestPackage.engine_coolant_temp()
        TestPackage.fuel_pressure()
        TestPackage.manifold_absolute_pressure()
        TestPackage.camshaft_position()
        TestPackage.crankshaft_position()
        TestPackage.knock()
        TestPackage.turbo_boost()
        TestPackage.gas()
        TestPackage.quickshifter()
        TestPackage.lambda_to_can()
        print()

if __name__ == "__main__":
    TestPackage.runAll()