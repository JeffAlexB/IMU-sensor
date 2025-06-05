"""
Simulates accelerometer for IMU orientation estimation.

The sensor estimates pitch and roll by interpreting the direction of gravity.
Noise is added to mimic real-world sensor imperfections.
"""

import numpy as np
from sensors.base_sensor import BaseSensor

class AccelerometerSensor(BaseSensor):
    def __init__(self, noise_stddev=2.0):
        super().__init__(noise_stddev)

    def simulate(self, true_pitch, true_roll):
        """
        Simulate accelerometer readings by adding noise to true pitch and roll.
        returns a tuple from array noisy_pitch & noisy_roll
        """
        noisy_pitch = self.add_noise(true_pitch)
        noisy_roll  = self.add_noise(true_roll)
        return noisy_pitch, noisy_roll
