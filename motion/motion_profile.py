# motion_profile.py

"""
Generates the true pitch, roll, and yaw motion profiles for the IMU simulation.
Also includes a decaying disturbance for pitch to simulate turbulence.
"""

import numpy as np
from config import (
    SIM_TIME_SECONDS,
    DT,
    PITCH_AMPLITUDE_DEG, ROLL_AMPLITUDE_DEG, YAW_AMPLITUDE_DEG,
    PITCH_FREQ_HZ, ROLL_FREQ_HZ, YAW_FREQ_HZ,
    DISTURBANCE_AMPLITUDE, DISTURBANCE_FREQ_HZ, DISTURBANCE_DECAY
)

class MotionProfile:
    def __init__(self):
        self.time_array = np.arange(0, SIM_TIME_SECONDS, DT)

    def generate(self):
        t = self.time_array

        pitch = PITCH_AMPLITUDE_DEG * np.sin(2 * np.pi * PITCH_FREQ_HZ * t)
        roll  = ROLL_AMPLITUDE_DEG  * np.sin(2 * np.pi * ROLL_FREQ_HZ  * t)
        yaw   = YAW_AMPLITUDE_DEG   * np.sin(2 * np.pi * YAW_FREQ_HZ   * t)

        disturbance = DISTURBANCE_AMPLITUDE * np.sin(2 * np.pi * DISTURBANCE_FREQ_HZ * t)
        pitch += disturbance * np.exp(-DISTURBANCE_DECAY * t)

        return pitch, roll, yaw

    def get_time(self):
        return self.time_array
