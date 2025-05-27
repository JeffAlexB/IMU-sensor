# IMU Sensor Fusion Simulator – Using Complementary Filter (Pitch, Roll, Yaw)

## Overview
This project simulates a 3-axis Inertial Measurement Unit (IMU) and demonstrates real-time orientation estimation using a complementary filter. It fuses synthetic gyroscope data (angular rate)  to estimate the pitch, roll, and yaw of a moving object.

The purpose of the simulation is to explore how embedded systems process raw sensor signals into meaningful, usable orientation data — as seen in AHRS (Attitude and Heading Reference Systems) used in robotics, drones, underwater vehicles, and spacecraft.

The project was created as part of a self-study effort to understand embedded systems and sensor fusion while transitioning from computer science to aerospace and embedded engineering. Due to limited time while wrapping up studies and work, this represents an early proof-of-concept rather than a complete solution.

---

## Key Features
-  Simulates 3-axis motion (pitch, roll, yaw) using sinusoidal motion profiles
-  Injects a decaying pitch disturbance to mimic external forces or turbulence
-  Generates noisy gyroscope, accelerometer, and magnetometer signals
-  Applies a complementary filter per axis to fuse and clean the data
-  Includes an interactive slider to tune the filter coefficient (`alpha`)
-  Visualizes each axis in real time: true angle, noisy sensor, and fused output

---

## Why This Matters

Writing software for real sensors requires understanding:
- How raw signals are noisy, incomplete, or drift over time
- That no single sensor gives perfect results — fusion is necessary
- That embedded filters must be fast, stable, and tunable

In this project:
- The gyro gives short-term angular velocity but drifts / has turbulence.

This mirrors what real embedded software does on IMU-based navigation systems in drones, AUVs, or satellite attitude control.

---

## How It Works

1. Simulated Motion: Sinusoidal pitch, roll, and yaw profiles plus a decaying disturbance.
2. Sensor Generation:
   - Gyroscope = angular derivative + noise
3. Filtering: Complementary filter per axis fuses gyro and absolute reference.
4. Visualization: Real-time plots compare ground truth, raw sensor, and fused estimate.
5. Interactivity: Slider allows tuning of `alpha`, adjusting gyro-vs-sensor weighting.

---

## How to Run
```bash
pip install numpy matplotlib
python imu_fusion_simulator.py
```
A GUI window will open with 3 plots and a slider at the bottom.
- Move the slider to adjust filter responsiveness.
- Observe how the fused angle tracks true motion while rejecting sensor noise.

---

## Talking Points
- Demonstrates real-time sensor fusion principles
- Filter mimics what’s deployed on embedded MCUs or sensor hubs
- Visualizes tradeoffs in tuning `alpha` (gyro weight)
- Shows how software gives meaning to messy real-world sensor data

---

## Limitations & Next Steps
- Currently uses Euler angles (not quaternions)
- Complementary filter only — no Kalman or Madgwick comparison
- All motion is simulated — no hardware integration yet

### Possible Improvements
- Extend to 9-axis simulation (full IMU + magnetometer + barometer / accelerometer)
- Switch to quaternion math for full 3D orientation(?)
- Add real IMU data (e.g., MPU6050 + Arduino) or use a board
- Implement real-time constraints (e.g., bounded latency + update loop)

---

## Notes
<p> This project confirmed my interest in embedded systems and aerospace applications. 
Even with limited time, simulating sensor behavior and writing the fusion logic helped 
me understand what it really means to write software that interprets noisy physical data. 
I hope to build on this in future projects.</p>

---

## License
MIT License(?)
