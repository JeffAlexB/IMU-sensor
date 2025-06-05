"""
contains abstract base classes and specific simulated sensor types
like gyroscopes, accelerometers, and magnetometers. Each sensor should apply its own
noise model and interface for integration into the fusion pipeline.
"""

from .base_sensor import BaseSensor
from .gyro_sensor import GyroSensor
from .accelerometer_sensor import AccelerometerSensor
from .magnetometer_sensor import MagnetometerSensor

__all__ = [
    "BaseSensor",
    "GyroSensor",
    "AccelerometerSensor",
    "MagnetometerSensor",
]

