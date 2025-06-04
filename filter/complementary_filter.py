# complementary_filter.py

"""
Complementary filter for fusing gyro and absolute sensor data (like accel/mag).

This was the simplest way I found to get low-drift orientation from noisy signals.
It balances fast updates from the gyroscope with long-term stability from reference sensors.
Used for pitch, roll, and yaw estimation.
"""

import numpy as np

class ComplementaryFilter:
    def __init__(self, alpha):
        # how much to trust the gyro - 1.0 = only gyro, 0.0 = only reference like the accel or magmeter
        self.alpha = alpha

    def apply(self, gyro_rate, reference_signal, dt):
        fused_signal = np.zeros_like(reference_signal) # fuses gyro and reference signal into a single estimate. Returns a fused signal
        fused_signal[0] = reference_signal[0] # start with the absolute sensor value (e.g., accel or mag)

        for i in range(1, len(reference_signal)):
            gyro_estimate = fused_signal[i-1] + gyro_rate[i] * dt # Integrate gyro rate to estimate angle
            # complementary signal fusion: trust gyro short-term, reference long-term
            fused_signal[i] = self.alpha * gyro_estimate + (1 - self.alpha) * reference_signal[i]

        return fused_signal


# Example usage / debug check
if __name__ == "__main__":
    print("ComplementaryFilter module loaded — intended for use in sensor fusion simulations.")
    # TODO: Consider adding a simple demo or test case here
