"""
IMU Sensor Fusion Simulator using Complementary Filter

Simulates 3-axis IMU motion and applies a complementary filter
on gyro + accel/mag data. This is the core script that wires together
motion generation, sensor simulation, fusion, and visualization.

Author: Alex (BSCS - Computation)
Date: 2025
"""

import matplotlib
matplotlib.use('TkAgg')  # Ensures interactive mode in PyCharm or similar

from config import D_TIME, DEFAULT_ALPHA
from motion.motion_profile import MotionProfile
from sensors.gyro_sensor import GyroSensor
from sensors.accelerometer_sensor import AccelerometerSensor
from sensors.magnetometer_sensor import MagnetometerSensor
from visualization.plot_manager import PlotManager


def main():
    # generates motion profile
    motion = MotionProfile()
    time_array = motion.get_time()
    true_pitch, true_roll, true_yaw = motion.generate()

    # sims gyro with 'noise'
    gyro = GyroSensor(noise_stddev=0.5)
    gyro_pitch_rate = gyro.simulate(true_pitch, time_array, D_TIME)
    gyro_roll_rate  = gyro.simulate(true_roll, time_array, D_TIME)
    gyro_yaw_rate   = gyro.simulate(true_yaw, time_array, D_TIME)

    accel = AccelerometerSensor(noise_stddev=2.0)
    mag = MagnetometerSensor(noise_stddev=2.0)

    # sims additional sensor input data
    accel_pitch = accel.add_noise(true_pitch)
    accel_roll = accel.add_noise(true_roll)
    mag_yaw = mag.add_noise(true_yaw)

    """# basic complementary filter
    filter = ComplementaryFilter(alpha=DEFAULT_ALPHA)
    fused_pitch = filter.apply(gyro_pitch_rate, accel_pitch, D_TIME)
    fused_roll  = filter.apply(gyro_roll_rate, accel_roll, D_TIME)
    fused_yaw   = filter.apply(gyro_yaw_rate, mag_yaw, D_TIME)"""

    # set up  plotting
    raw_data = {
        "true": {
            "pitch": true_pitch,
            "roll": true_roll,
            "yaw": true_yaw,
        },
        "gyro": {
            "pitch": gyro_pitch_rate,
            "roll": gyro_roll_rate,
            "yaw": gyro_yaw_rate,
        },
        "reference": {
            "pitch": accel_pitch,
            "roll": accel_roll,
            "yaw": mag_yaw,
        }
    }

    plot = PlotManager(time_array, raw_data, D_TIME, initial_alpha=DEFAULT_ALPHA)
    plot.show()
    # debug slider
    # plot._add_slider()

# debugg / launch confirmation
if __name__ == "__main__":
    print("[INFO] Launching IMU Sensor Fusion Simulator...")
    main()
