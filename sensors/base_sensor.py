"""
Base class for all sensor types.
Handles basic noise generation and provides a common interface for simulated sensors.
"""

import numpy as np

class BaseSensor:
    def __init__(self, noise_stddev):
        self.noise_stddev = noise_stddev

    def add_noise(self, clean_signal):
        # adds random noise to make it more realistic when sim'ing artificial inputs
        if self.noise_stddev <= 0:
            return clean_signal
        noise = np.random.normal(0, self.noise_stddev, size=clean_signal.shape)
        return clean_signal + noise

    def simulate(self, true_signal):
        # child classes should override this?
        raise NotImplementedError("simulate() is required for each child class")
