# IMU Sensor Fusion Simulator – Complementary Filter (Pitch & Roll)

## Overview

This project simulates a simplified 2-axis Inertial Measurement Unit (IMU) and demonstrates **real-time sensor fusion** using a **complementary filter** to estimate orientation (pitch and roll). The filter fuses noisy accelerometer data with drifting gyroscope data to produce stable, real-time orientation estimates — a foundational technique in embedded aerospace and marine systems such as AUVs, drones, and spacecraft.

It was built as a personal challenge to explore embedded systems principles in simulation and as an interview-ready demonstration of how I approach engineering problems, real-time signal processing, and control.

---

## Features

-  Simulated pitch and roll dynamics using sine wave motion profiles
-  Disturbance model on the pitch axis to mimic environmental effects (e.g., wave force or mechanical shock)
-  Synthetic gyro and accelerometer data streams with configurable noise
-  Real-time complementary filter blending inertial data streams
-  Interactive `matplotlib` slider to adjust filter gain (`α`) and visualize performance trade-offs

---

## How It Works

1. Sensor Simulation
   - `true_pitch` and `true_roll` are generated as smooth sinusoidal signals.
   - `gyro_rate` is derived from the angle's time derivative + noise (mimics drift-prone gyros).
   - `accel_angle` is the true angle + noise (mimics noisy tilt detection).

2. Complementary Filter
   - A fast, embedded-friendly algorithm that combines the short-term precision of gyroscopes with the long-term stability of accelerometers.
   - Formula:  
     `fused[i] = α * (fused[i-1] + gyro[i] * dt) + (1 - α) * accel[i]`

3. Visualization
   - Two real-time plots (pitch and roll) show:
     - The true angle (ideal)
     - The accelerometer-only estimate (noisy)
     - The fused output (filtered result)
   - A slider controls `α`, the weight given to gyro data.

---

## Why It Matters

This project replicates a simplified version of what an actual **Attitude and Heading Reference System (AHRS)** or **INS** would do inside an embedded system — fusing inertial data to calculate orientation in real-time.

It demonstrates understanding of:
- Sensor noise characteristics and signal integration
- Stability vs. responsiveness tradeoffs
- Lightweight control/filtering code appropriate for microcontrollers


---

## Potential Extensions

-  Add yaw estimation with a 3rd axis (simulate 9DOF IMU)
-  Fuse magnetometer data for full AHRS orientation
-  Add Kalman or Madgwick filters for comparison
-  Port to C++ or deploy on embedded target (e.g., Arduino with MPU6050)

---

## Screenshots


---

## How to Run

```bash
pip install matplotlib numpy
python imu_fusion_simulator.py
