# IMU Sensor Fusion Simulator – Using Complementary Filter (Pitch, Roll, Yaw)

"""
Student: Alex (BSCS - Computation)
Date: 2025

This project simulates a 3-axis IMU and applies a complementary filter to fuse
accelerometer, gyroscope, and magnetometer data for pitch, roll, and yaw estimation.
Built as a self-study exploration of orientation estimation for robotics class and proof-of-concept.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# bypass for pycharm ide plots not coming out as interactive - forces independent interactive window/GUI
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg' depending on your system

# simulation parameters
sampling_rate_hz = 100  # Hz
dt = 1 / sampling_rate_hz
sim_time_seconds = 10

# basic time array
t = np.arange(0, sim_time_seconds, dt)

# 'true' motion profiles used for the sim
# Sims the sinusoidal pitch, roll, yaw motion - in degrees
true_pitch = 20 * np.sin(2 * np.pi * 0.2 * t)
true_roll  = 10 * np.sin(2 * np.pi * 0.1 * t)
true_yaw   = 30 * np.sin(2 * np.pi * 0.15 * t)

# adds pitch disturbances a.k.a turbulance
disturbance = 5 * np.sin(2 * np.pi * 1.5 * t)
true_pitch += disturbance * np.exp(-0.5 * t)  # decaying oscillation

# 'synthetic' noise for the sim
gyro_noise_stddev = 0.5
accel_noise_stddev = 2.0
mag_noise_stddev = 2.0

def simulate_sensor_reading(true_signal, noise_std):
    return true_signal + np.random.normal(0, noise_std, size=true_signal.shape)

# a-rates from true angle derivatives & gyro 'noise'
gyro_pitch_rate = np.gradient(true_pitch, dt) + np.random.normal(0, gyro_noise_stddev, size=t.shape)
gyro_roll_rate  = np.gradient(true_roll, dt) + np.random.normal(0, gyro_noise_stddev, size=t.shape)
gyro_yaw_rate   = np.gradient(true_yaw, dt) + np.random.normal(0, gyro_noise_stddev, size=t.shape)

# simulated tilt and heading estimates (accel + mag)
accel_pitch = simulate_sensor_reading(true_pitch, accel_noise_stddev)
accel_roll  = simulate_sensor_reading(true_roll, accel_noise_stddev)
mag_yaw     = simulate_sensor_reading(true_yaw, mag_noise_stddev)

# labeling the visual graphs
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))
plt.subplots_adjust(left=0.1, bottom=0.25)

# siming pitch
l_true_pitch, = ax1.plot(t, true_pitch, label='True Pitch', linewidth=2)
l_accel_pitch, = ax1.plot(t, accel_pitch, label='Accel Pitch (Noisy)', alpha=0.5)
l_fused_pitch, = ax1.plot([], [], label='Fused Pitch', linestyle='--')
ax1.set_ylabel('Pitch (°)')
ax1.set_title('Pitch Axis')
ax1.legend()
ax1.grid(True)

# siming roll
l_true_roll, = ax2.plot(t, true_roll, label='True Roll', linewidth=2)
l_accel_roll, = ax2.plot(t, accel_roll, label='Accel Roll (Noisy)', alpha=0.5)
l_fused_roll, = ax2.plot([], [], label='Fused Roll', linestyle='--')
ax2.set_ylabel('Roll (°)')
ax2.set_title('Roll Axis')
ax2.legend()
ax2.grid(True)

# siming yaw
l_true_yaw, = ax3.plot(t, true_yaw, label='True Yaw', linewidth=2)
l_mag_yaw, = ax3.plot(t, mag_yaw, label='Mag Yaw (Noisy)', alpha=0.5)
l_fused_yaw, = ax3.plot([], [], label='Fused Yaw', linestyle='--')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Yaw (°)')
ax3.set_title('Yaw Axis')
ax3.legend()
ax3.grid(True)

# Complementary Filter Logic
def apply_complementary_filter(gyro_data, reference_data, alpha):
    fused = np.zeros_like(t)
    fused[0] = reference_data[0]  # start with absolute reference
    for i in range(1, len(t)):
        gyro_integrated = fused[i-1] + gyro_data[i] * dt
        fused[i] = alpha * gyro_integrated + (1 - alpha) * reference_data[i]
    return fused

# slider Setup & basic logic
def update(val):
    alpha_val = slider_alpha.val
    fused_pitch = apply_complementary_filter(gyro_pitch_rate, accel_pitch, alpha_val)
    fused_roll  = apply_complementary_filter(gyro_roll_rate, accel_roll, alpha_val)
    fused_yaw   = apply_complementary_filter(gyro_yaw_rate, mag_yaw, alpha_val)
    l_fused_pitch.set_data(t, fused_pitch)
    l_fused_roll.set_data(t, fused_roll)
    l_fused_yaw.set_data(t, fused_yaw)
    for ax in [ax1, ax2, ax3]:
        ax.relim()
        ax.autoscale_view()
    fig.canvas.draw_idle()

# interactive slider to tune 'alpha'
ax_alpha = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_alpha = Slider(ax_alpha, 'Alpha / gyro weight', 0.0, 1.0, valinit=0.97)  # hand-tuned
slider_alpha.on_changed(update)

# initial filter
l_fused_pitch.set_data(t, apply_complementary_filter(gyro_pitch_rate, accel_pitch, slider_alpha.val))
l_fused_roll.set_data(t, apply_complementary_filter(gyro_roll_rate, accel_roll, slider_alpha.val))
l_fused_yaw.set_data(t, apply_complementary_filter(gyro_yaw_rate, mag_yaw, slider_alpha.val))
for ax in [ax1, ax2, ax3]:
    ax.relim()
    ax.autoscale_view()

# launch plot / visual
plt.show()

# Final Note:
# This started as a way to better understand how real-world INS and AHRS systems use fused sensor data
# to produce stable, low-drift orientation. Adding disturbances and multiple axes helped me appreciate
# the filter’s simplicity and limitations. I'd like to eventually compare this to Madgwick or Kalman filtering
# Or implement accelerometer or magnetometer for complete 9-axis IMU for absolute positioning.
