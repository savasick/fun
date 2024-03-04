import math
import matplotlib.pyplot as plt
import numpy as np

def calculate_pi(n: int) -> float:
    pi = 0
    for i in range(n):
        term = math.pow(-1, i) / (2 * i + 1)
        pi += term
    pi *= 4
    return pi

def animate_pi_calculation(n: int, interval: int = 100):
    fig, ax = plt.subplots()
    x = np.linspace(0, n, n)
    y = np.zeros(n)
    line, = ax.plot(x, y)

    ax.set_xlim(0, n)
    ax.set_ylim(0, 4)
    ax.set_xlabel('Term')
    ax.set_ylabel('Pi Value')
    ax.set_title('Calculation of Pi using the Leibniz Formula')

    for i in range(n):
        term = math.pow(-1, i) / (2 * i + 1)
        y[i] = calculate_pi(i + 1)
        line.set_ydata(y)
        ax.set_title(f'Term {i + 1}: Pi Value = {y[i]:.15f}')
        plt.pause(interval / 1000)

    plt.show()

animate_pi_calculation(100000)