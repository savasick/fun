import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
n_points = 10000

n_frames = 100

n_inside = 0
n_total = 0

def update(frame):
    global n_inside, n_total

    x = np.random.rand(n_points)
    y = np.random.rand(n_points)

    inside = (x**2 + y**2) <= 1
    n_inside += np.sum(inside)
    n_total += n_points

    ax.clear()

    ax.scatter(x[inside], y[inside], color='red', s=10)
    ax.scatter(x[~inside], y[~inside], color='blue', s=10)

    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(np.cos(theta), np.sin(theta), color='green', linestyle='--')

    pi_estimate = 4 * n_inside / n_total

    ax.set_title(f'Estimate of Pi: {pi_estimate:.4f}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

fig, ax = plt.subplots()

ani = FuncAnimation(fig, update, frames=n_frames, interval=100)

plt.show()

pi_estimate = 4 * n_inside / n_total
print(f'Final Estimation of Pi: {pi_estimate:.4f}')