"""
Generating the pitch, roll, and yaw motion profiles for the IMU simulation.
Also includes a decaying disturbance for pitch aka turbulence.
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
        # Create a time array from 0 to SIM_TIME_SECONDS, spaced by DT
        self.t = np.arange(0, SIM_TIME_SECONDS, DT)

    def generate(self):
        # Create the base sinusoidal motion for each axis
        pitch = PITCH_AMPLITUDE_DEG * np.sin(2 * np.pi * PITCH_FREQ_HZ * self.t)
        roll  = ROLL_AMPLITUDE_DEG  * np.sin(2 * np.pi * ROLL_FREQ_HZ  * self.t)
        yaw   = YAW_AMPLITUDE_DEG   * np.sin(2 * np.pi * YAW_FREQ_HZ   * self.t)

        # Add turbulence to pitch (decaying sinusoid)
        disturbance = DISTURBANCE_AMPLITUDE * np.sin(2 * np.pi * DISTURBANCE_FREQ_HZ * self.t)
        pitch += disturbance * np.exp(-DISTURBANCE_DECAY * self.t)

        return pitch, roll, yaw

    def get_time(self):
        return self.t
