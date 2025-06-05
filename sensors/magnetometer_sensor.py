"""
Simulates magnetometer sensor to estimate yaw aka heading.

Uses the yaw angle and adds Gaussian noise to mimic magnetic disturbances.
"""

from sensors.base_sensor import BaseSensor

class MagnetometerSensor(BaseSensor):
    def __init__(self, noise_stddev):
        super().__init__(noise_stddev)

    def simulate(self, true_yaw):
        """
        uses true yaw angle in degrees and adds Gaussian noise to mimic magnetic disturbances.
        returns noisy yaw readings
        """
        return self.add_noise(true_yaw)


"""# verify its running
if __name__ == "__main__":
    print("MagnetometerSensor module loaded")
    time = np.linespace(0, 10, 1000)
    true_yaw = 30 * np.sin(2 * np.pi * 0.1 * time)
    sensor = MagnetometerSensor(noise_stddev=2.0)
    noisy_yaw = sensor.simulate(true_yaw)
"""