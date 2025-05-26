# IMU Sensor Fusion: Complementary Filter Simulation (1D Pitch Angle)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Simulation parameters
sampling_rate = 100  # Hz
dt = 1 / sampling_rate
sim_time = 10  # seconds
t = np.arange(0, sim_time, dt)

# Simulated true angle (e.g. sinusoidal pitch change)
true_angle = 20 * np.sin(2 * np.pi * 0.2 * t)  # oscillates between -20 and 20 degrees

# Simulated gyro data (angular velocity) = derivative of angle + noise
gyro_rate = np.gradient(true_angle, dt) + np.random.normal(0, 0.5, size=t.shape)

# Simulated accelerometer angle from tilt + noise
accel_angle = true_angle + np.random.normal(0, 2.0, size=t.shape)

# Interactive plot setup
fig, ax = plt.subplots(figsize=(12, 6))
plt.subplots_adjust(left=0.1, bottom=0.25)

l_true, = ax.plot(t, true_angle, label='True Angle (Pitch)', linewidth=2)
l_accel, = ax.plot(t, accel_angle, label='Accel Angle (Noisy)', alpha=0.5)
l_fused, = ax.plot([], [], label='Fused Angle (Complementary Filter)', linestyle='--')

ax.set_xlabel('Time (s)')
ax.set_ylabel('Angle (degrees)')
ax.set_title('IMU Sensor Fusion - Complementary Filter (1D Pitch Simulation)')
ax.legend()
ax.grid(True)

# Slider for alpha (complementary filter coefficient)
ax_alpha = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_alpha = Slider(ax_alpha, 'Alpha (gyro weight)', 0.0, 1.0, valinit=0.98)

# Complementary filter function
def compute_fused_angle(alpha):
    fused = np.zeros_like(t)
    fused[0] = accel_angle[0]
    for i in range(1, len(t)):
        gyro_integrated = fused[i-1] + gyro_rate[i] * dt
        fused[i] = alpha * gyro_integrated + (1 - alpha) * accel_angle[i]
    return fused

# Update plot when slider changes
def update(val):
    alpha_val = slider_alpha.val
    fused_angle = compute_fused_angle(alpha_val)
    l_fused.set_data(t, fused_angle)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()

slider_alpha.on_changed(update)

# Initial plot
l_fused.set_data(t, compute_fused_angle(slider_alpha.val))
ax.relim()
ax.autoscale_view()

plt.show()
