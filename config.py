"""
Configuration constants and tunable parameters for the IMU Fusion Simulator.
This file isolates settings so that tuning or adapting the simulation can be
handled without modifying the core logic.
"""

# sampling rate and sim timing
SAMPLING_RATE_HZ = 100
SIM_TIME_SECONDS = 10
DT = 1.0 / SAMPLING_RATE_HZ      # Time step per sample

# motion parameters
PITCH_AMPLITUDE_DEG = 20
ROLL_AMPLITUDE_DEG = 10
YAW_AMPLITUDE_DEG = 30
PITCH_FREQ_HZ = 0.2
ROLL_FREQ_HZ = 0.1
YAW_FREQ_HZ = 0.15

# simulate turbulence on pitch
DISTURBANCE_AMPLITUDE = 5        # degrees
DISTURBANCE_FREQ_HZ = 1.5
DISTURBANCE_DECAY = 0.5          # Exponential decay factor

# sensor noise params
GYRO_NOISE_STDDEV = 0.5          # deg/sec
ACCEL_NOISE_STDDEV = 2.0
MAG_NOISE_STDDEV = 2.0

# Complementary filter default 'alpha' / gyro weight
DEFAULT_ALPHA = 0.97

# plotting values for visualization
PLOT_WIDTH = 12
PLOT_HEIGHT = 10
SLIDER_START = 0.25              # relative X position for slider
SLIDER_WIDTH = 0.65              # relative width of slider
SLIDER_HEIGHT = 0.03             # relative height of slider
