"""
Handles all plotting and visualization for the IMU sensor fusion simulator.

- Generates 3 time-series plots for pitch, roll, and yaw
- Displays true angles, noisy reference inputs (accel or mag), and fused output
- Adds an interactive slider to tune the alpha parameter in the complementary filter
"""

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from filter.complementary_filter import ComplementaryFilter

class PlotManager:
    def __init__(self, time_array, raw_data, dt, initial_alpha=0.97):
        """
        Parameters:
        - time_array: np.ndarray, x-axis for the plots in seconds
        - raw_data: dictionary with sensor data
            example for synth data:
            {
                "gyro":      {"pitch": ..., "roll": ..., "yaw": ...},
                "reference": {"pitch": ..., "roll": ..., "yaw": ...},
                "true":      {"pitch": ..., "roll": ..., "yaw": ...}
            }
        - dt: time step in seconds
        - initial_alpha: starting weight for the complementary filter
        """
        self.t = time_array
        self.raw = raw_data
        self.dt = dt
        self.alpha = initial_alpha

        self.filter = ComplementaryFilter(alpha=self.alpha)

        self.fig, (self.ax_pitch, self.ax_roll, self.ax_yaw) = plt.subplots(3, 1, figsize=(12, 10))
        plt.subplots_adjust(left=0.1, bottom=0.25)

        self._init_pitch_plot()
        self._init_roll_plot()
        self._init_yaw_plot()

        self._add_slider()
        self.update_plots(self.alpha)

    def _init_pitch_plot(self):
        self.l_true_pitch, = self.ax_pitch.plot(self.t, self.raw["true"]["pitch"], label="True Pitch", linewidth=2)
        self.l_ref_pitch, = self.ax_pitch.plot(self.t, self.raw["reference"]["pitch"], label="Accel Pitch", alpha=0.5)
        self.l_fused_pitch, = self.ax_pitch.plot([], [], label="Fused Pitch", linestyle="--")
        self.ax_pitch.set_title("Pitch Axis")
        self.ax_pitch.set_ylabel("Pitch (°)")
        self.ax_pitch.legend()
        self.ax_pitch.grid(True)

    def _init_roll_plot(self):
        self.l_true_roll, = self.ax_roll.plot(self.t, self.raw["true"]["roll"], label="True Roll", linewidth=2)
        self.l_ref_roll, = self.ax_roll.plot(self.t, self.raw["reference"]["roll"], label="Accel Roll", alpha=0.5)
        self.l_fused_roll, = self.ax_roll.plot([], [], label="Fused Roll", linestyle="--")
        self.ax_roll.set_title("Roll Axis")
        self.ax_roll.set_ylabel("Roll (°)")
        self.ax_roll.legend()
        self.ax_roll.grid(True)

    def _init_yaw_plot(self):
        self.l_true_yaw, = self.ax_yaw.plot(self.t, self.raw["true"]["yaw"], label="True Yaw", linewidth=2)
        self.l_ref_yaw, = self.ax_yaw.plot(self.t, self.raw["reference"]["yaw"], label="Mag Yaw", alpha=0.5)
        self.l_fused_yaw, = self.ax_yaw.plot([], [], label="Fused Yaw", linestyle="--")
        self.ax_yaw.set_title("Yaw Axis")
        self.ax_yaw.set_ylabel("Yaw (°)")
        self.ax_yaw.set_xlabel("Time (s)")
        self.ax_yaw.legend()
        self.ax_yaw.grid(True)

    def _add_slider(self):
        ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
        self.slider = Slider(ax_slider, "Alpha (gyro weight)", 0.0, 1.0, valinit=self.alpha)
        self.slider.on_changed(self.update_plots)

    def update_plots(self, alpha_val):
        self.alpha = alpha_val
        self.filter.alpha = alpha_val

        fused_pitch = self.filter.apply(self.raw["gyro"]["pitch"], self.raw["reference"]["pitch"], self.dt)
        fused_roll  = self.filter.apply(self.raw["gyro"]["roll"],  self.raw["reference"]["roll"],  self.dt)
        fused_yaw   = self.filter.apply(self.raw["gyro"]["yaw"],   self.raw["reference"]["yaw"],   self.dt)

        self.l_fused_pitch.set_data(self.t, fused_pitch)
        self.l_fused_roll.set_data(self.t, fused_roll)
        self.l_fused_yaw.set_data(self.t, fused_yaw)

        for ax in (self.ax_pitch, self.ax_roll, self.ax_yaw):
            ax.relim()
            ax.autoscale_view()

        self.fig.canvas.draw_idle()

    def show(self):
        plt.show()
