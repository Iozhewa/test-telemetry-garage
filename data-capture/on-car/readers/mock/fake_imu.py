#!/usr/bin/env python3
"""
Mock MPU-9250 motion sensor.

Simulates a car driving in circles, with recorded
accelerometer or gyro values.
"""
import math
import time

class FakeIMU:
    def __init__(self):
        self.start_time = time.time()
    
    def read_all(self) -> dict:
        elapsed = time.time() - self.start_time
        lateral_g = math.sin(elapsed * 0.5) * 1.2 # G force
        longitudinal_g = math.cos(elapsed * 0.3) * 0.8 # breaking/accel
        return {
            "lateral_g": lateral_g,
            "longitudinal_g": longitudinal_g,
            "vertical_g": 0.0,
            "roll": 0.0,
            "pitch": 0.0,
            "yaw": elapsed * 10,
            "yaw_rate": 10
        }

if __name__ == "__main__":
    imu = FakeIMU()
    for I in range(0, 5):
        print(imu.read_all())
        time.sleep(0.5)