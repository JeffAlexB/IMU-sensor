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

    """ # ticket stub
    def simulate(self, angle_signal):
        Derivative of angle gives angular rate (deg/sec)
        angular_velocity a gradient of angle_signal & D_TIME
    """

    def simulate(self, true_signal, time_array, dt):
        """
        Simulates gyro rate by differentiating the true signal and adding noise.
        - true_signal an array for true orientation (deg)
        - time_array an array time values (s)
        - dt a float value of the time delta (s)
        returns a noisy gyro rate signal (deg/s)
        """
        # Gyroscope measures angular velocity
        rate = np.gradient(true_signal, dt)
        return self.add_noise(rate)
