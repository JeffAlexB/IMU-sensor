"""
Configuration file for IMU Fusion Simulator
All key simulation settings live here for easier tweaking.
"""

# timing
SAMPLING_RATE_HZ = 100           # how many samples per second, aka "refresh" rate
SIM_TIME_SECONDS = 10            # total simulation time in seconds
D_TIME = 1.0 / SAMPLING_RATE_HZ  # delta time between each sample

# motion params
PITCH_AMPLITUDE_DEG = 20
ROLL_AMPLITUDE_DEG = 10
YAW_AMPLITUDE_DEG = 30

PITCH_FREQ_HZ = 0.2
ROLL_FREQ_HZ = 0.1
YAW_FREQ_HZ = 0.15

# artificial disturbance / turbulence
DISTURBANCE_AMPLITUDE = 5        # how strong the pitch disturbance is
DISTURBANCE_FREQ_HZ = 1.5        # frequency of the disturbance
DISTURBANCE_DECAY = 0.5          # exponential decay rate (lower = faster fade)

# sensor 'noise' for sim sensor inputs
GYRO_NOISE_STDDEV = 0.5          # gyro noise (deg/s)
ACCEL_NOISE_STDDEV = 2.0         # accel noise (deg)
MAG_NOISE_STDDEV = 2.0           # mag noise (deg)

# Comp filter settings
DEFAULT_ALPHA = 0.97             # default complementary filter weighting

# visualization options
PLOT_WIDTH = 12
PLOT_HEIGHT = 10
SLIDER_START = 0.25              # x-axis
SLIDER_WIDTH = 0.65
SLIDER_HEIGHT = 0.03
