import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation


class CubeAnimator:
    def __init__(self, pitch, roll, yaw, interval=50, size=1.0):
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw
        self.interval = interval
        self.size = size
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self._initialize_plot()  # setup

    def _initialize_plot(self):
        # set up axes
        self.ax.set_xlim([-1.5, 1.5])
        self.ax.set_ylim([-1.5, 1.5])
        self.ax.set_zlim([-1.5, 1.5])
        self.ax.set_box_aspect([1, 1, 1])  # to force cube to look square visually
        self.ax.axis('off')

        size = self.size

        # draw reference arrows
        self.ax.quiver(0, 0, 0, 1.5, 0, 0, color='red')  # X
        self.ax.quiver(0, 0, 0, 0, 1.5, 0, color='green')  # Y
        self.ax.quiver(0, 0, 0, 0, 0, 1.5, color='blue')  # Z
        # axis labels
        self.ax.text(1.5, 0, 0, 'X', color='red')
        self.ax.text(0, 1.5, 0, 'Y', color='green')
        self.ax.text(0, 0, 1.5, 'Z', color='blue')

        # Scaled cube vertices
        self.vertices = np.array([
            [x * size, y * size, z * size]
            for x in [-1, 1]
            for y in [-1, 1]
            for z in [-1, 1]
        ])

        # draw cube
        cube_faces = [
            [0, 1, 3, 2],
            [4, 5, 7, 6],
            [0, 1, 5, 4],
            [2, 3, 7, 6],
            [0, 2, 6, 4],
            [1, 3, 7, 5],
        ]
        faces = [[self.vertices[i] for i in face] for face in cube_faces]
        self.cube = Poly3DCollection(faces, facecolors='skyblue', edgecolors='black', alpha=0.5)
        self.ax.add_collection3d(self.cube)

        # grid plane
        x = np.linspace(-3, 3, 7)
        y = np.linspace(-3, 3, 7)
        grid_range = np.linspace(-size * 1.5, size * 1.5, 7)
        X, Y = np.meshgrid(grid_range, grid_range)
        Z = np.full_like(X, -size * 1.2)
        self.ax.plot_wireframe(X, Y, Z, color='gray', linestyle='--', alpha=0.3)

    """def _draw_axes(self):
        # draws coordinate arrows
        origin = np.array([0, 0, 0])
        axes_length = 1.5

        self.ax.quiver(*origin, axes_length, 0, 0, color='r', arrow_length_ratio=0.1)
        self.ax.quiver(*origin, 0, axes_length, 0, color='g', arrow_length_ratio=0.1)
        self.ax.quiver(*origin, 0, 0, axes_length, color='b', arrow_length_ratio=0.1)

        self.ax.text(axes_length, 0, 0, 'X', color='r', fontsize=12)
        self.ax.text(0, axes_length, 0, 'Y', color='g', fontsize=12)
        self.ax.text(0, 0, axes_length, 'Z', color='b', fontsize=12)
    """

    def _rotation_matrix(self, p, r, y):
        p = np.radians(p)
        r = np.radians(r)
        y = np.radians(y)

        # rotation about X
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(p), -np.sin(p)],
            [0, np.sin(p), np.cos(p)],
        ])

        # rotation about Y
        Ry = np.array([
            [np.cos(r), 0, np.sin(r)],
            [0, 1, 0],
            [-np.sin(r), 0, np.cos(r)],
        ])

        # rotation about Z
        Rz = np.array([
            [np.cos(y), -np.sin(y), 0],
            [np.sin(y), np.cos(y), 0],
            [0, 0, 1],
        ])

        # multiply all
        R = Rz @ Ry @ Rx
        return R

    def _update(self, i):
        if i >= len(self.pitch):
            return
        pitch = self.pitch[i]
        roll = self.roll[i]
        yaw = self.yaw[i]

        rot = self._rotation_matrix(pitch, roll, yaw)
        rotated_vertices = (rot @ self.vertices.T).T

        cube_faces = [
            [0, 1, 3, 2],
            [4, 5, 7, 6],
            [0, 1, 5, 4],
            [2, 3, 7, 6],
            [0, 2, 6, 4],
            [1, 3, 7, 5],
        ]
        new_faces = [[rotated_vertices[i] for i in face] for face in cube_faces]
        self.cube.set_verts(new_faces)

    def run(self):
        # animates cube
        self.anim = FuncAnimation(self.fig, self._update, frames=len(self.pitch), interval=self.interval)
        plt.show()