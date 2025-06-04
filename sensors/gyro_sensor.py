"""
Simulates a gyroscope sensor by calculating the angular velocity
(derivative of angle over time) and adding realistic noise.
"""

import numpy as np
from .base_sensor import BaseSensor
from config import D_TIME

class GyroSensor(BaseSensor):
    def __init__(self, noise_stddev):
        super().__init__(noise_stddev)

    """def simulate(self, angle_signal):
        # Derivative of angle gives us angular rate (deg/sec)
        angular_velocity = np.gradient(angle_signal, D_TIME)
        return self.add_noise(angular_velocity)
    """

    def simulate(self, true_signal, time_array, dt):
        """
        Simulates gyro rate by differentiating the true signal and adding noise.

        Parameters:
        - true_signal: np.ndarray — true orientation (deg)
        - time_array: np.ndarray — time values (s)
        - dt: float — time delta (s)

        Returns:
        - np.ndarray — noisy gyro rate signal (deg/s)
        """
        # Gyroscope measures angular velocity — we simulate this via derivative
        rate = np.gradient(true_signal, dt)
        return self.add_noise(rate)
