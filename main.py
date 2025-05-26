# IMU Sensor Fusion: Complementary Filter Simulation (Pitch and Roll)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg' depending on your system

# Simulation parameters
sampling_rate = 100  # Hz
dt = 1 / sampling_rate
sim_time = 10  # seconds
t = np.arange(0, sim_time, dt)

# Simulate true pitch and roll angles (oscillating + disturbance)
true_pitch = 20 * np.sin(2 * np.pi * 0.2 * t)
true_roll = 10 * np.sin(2 * np.pi * 0.1 * t)

# Add disturbances (e.g. wave or gusts)
disturbance = 5 * np.sin(2 * np.pi * 1.5 * t)
true_pitch += disturbance * np.exp(-0.5 * t)  # decay over time

# Simulated gyro data (rate of change + noise)import matplotlib
gyro_pitch_rate = np.gradient(true_pitch, dt) + np.random.normal(0, 0.5, size=t.shape)
gyro_roll_rate = np.gradient(true_roll, dt) + np.random.normal(0, 0.5, size=t.shape)

# Simulated accelerometer angle (tilt) + noise
accel_pitch = true_pitch + np.random.normal(0, 2.0, size=t.shape)
accel_roll = true_roll + np.random.normal(0, 2.0, size=t.shape)

# Interactive plot setup
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
plt.subplots_adjust(left=0.1, bottom=0.25)

# Pitch plot
l_true_pitch, = ax1.plot(t, true_pitch, label='True Pitch', linewidth=2)
l_accel_pitch, = ax1.plot(t, accel_pitch, label='Accel Pitch (Noisy)', alpha=0.5)
l_fused_pitch, = ax1.plot([], [], label='Fused Pitch', linestyle='--')
ax1.set_ylabel('Pitch (degrees)')
ax1.set_title('Pitch Axis')
ax1.legend()
ax1.grid(True)

# Roll plot
l_true_roll, = ax2.plot(t, true_roll, label='True Roll', linewidth=2)
l_accel_roll, = ax2.plot(t, accel_roll, label='Accel Roll (Noisy)', alpha=0.5)
l_fused_roll, = ax2.plot([], [], label='Fused Roll', linestyle='--')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Roll (degrees)')
ax2.set_title('Roll Axis')
ax2.legend()
ax2.grid(True)

# Slider for alpha
ax_alpha = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_alpha = Slider(ax_alpha, 'Alpha (gyro weight)', 0.0, 1.0, valinit=0.98)

# Complementary filter function for a single axis
def compute_fused(gyro, accel, alpha):
    fused = np.zeros_like(t)
    fused[0] = accel[0]
    for i in range(1, len(t)):
        gyro_integrated = fused[i-1] + gyro[i] * dt
        fused[i] = alpha * gyro_integrated + (1 - alpha) * accel[i]
    return fused

# Update plot when slider changes
def update(val):
    alpha_val = slider_alpha.val
    fused_pitch = compute_fused(gyro_pitch_rate, accel_pitch, alpha_val)
    fused_roll = compute_fused(gyro_roll_rate, accel_roll, alpha_val)
    l_fused_pitch.set_data(t, fused_pitch)
    l_fused_roll.set_data(t, fused_roll)
    ax1.relim()
    ax1.autoscale_view()
    ax2.relim()
    ax2.autoscale_view()
    fig.canvas.draw_idle()

slider_alpha.on_changed(update)

# Initial plot
l_fused_pitch.set_data(t, compute_fused(gyro_pitch_rate, accel_pitch, slider_alpha.val))
l_fused_roll.set_data(t, compute_fused(gyro_roll_rate, accel_roll, slider_alpha.val))
ax1.relim()
ax1.autoscale_view()
ax2.relim()
ax2.autoscale_view()

plt.show()
