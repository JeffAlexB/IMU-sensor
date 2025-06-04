"""
Simulates a gyroscope sensor by calculating the angular velocity
(derivative of angle over time) and adding realistic noise.
"""

import numpy as np
from base_sensor import BaseSensor
from config import D_TIME

class GyroSensor(BaseSensor):
    def __init__(self, noise_stddev):
        super().__init__(noise_stddev)

    def simulate(self, angle_signal):
        # Derivative of angle gives us angular rate (deg/sec)
        angular_velocity = np.gradient(angle_signal, D_TIME)
        return self.add_noise(angular_velocity)
