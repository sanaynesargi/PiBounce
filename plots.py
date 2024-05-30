import sys

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pylab
import time
import math

from aquarel import load_theme
from utils import get_window_size
from sim import run_sim
from multiprocessing import Process, Queue



# courtesy of https://stackoverflow.com/questions/7449585/how-do-you-set-the-absolute-position-of-figure-windows-with-matplotlib
def move_figure(f, x, y):
    """Move figure's upper left corner to pixel (x, y)"""
    backend = matplotlib.get_backend()
    if backend == 'TkAgg':
        f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
    elif backend == 'WXAgg':
        f.canvas.manager.window.SetPosition((x, y))
    else:
        # This works for QT and GTK
        # You can also use window.setGeometry
        f.canvas.manager.window.move(x, y)



theme = load_theme("minimal_dark")
theme.apply()

fig, axs = plt.subplots(2, 2, figsize=(7.5, 9), dpi=100)

axs[0, 0].set_title('Axis [0, 0]')
axs[0, 1].set_title('Axis [0, 1]')
axs[1, 0].set_title('Axis [1, 0]')
axs[1, 1].set_title('Axis [1, 1]')

# fig = pylab.gcf()
# fig.canvas.manager.set_window_title('Graph Visualization')

plt.tight_layout(pad=3.0)

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

w, h = get_window_size()
# move_figure(fig, w, h)

xdata1, ydata1 = [], []
xdata2, ydata2 = [], []
xdata3, ydata3 = [], []
xdata4, ydata4 = [], []
last_position = 0

line1,  = axs[0, 0].plot([], [], "b-")
pow = 3

theme.apply_transforms()


def read_new_lines(filename, lp):
    new_data = []
    with open(filename, 'r') as file:
        file.seek(lp)
        lines = file.readlines()
        lasp = file.tell()

        for line in lines:
            parts = line.strip().split(',')
            if len(parts) >= 2:  # Ensure there are at least two columns
                try:
                    t, y, z, k = float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3])
                    new_data.append((t, y, z, k))
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")

    return new_data, lasp


def init():
    line1.set_data([], [])
    return line1,


def update(frame):
    global pow
    global last_position, xdata1, ydata1

    # Read new data from file
    new_data, last_position = read_new_lines(filename, last_position)
    m1 = 0
    m2 = 0

    if new_data:
        for a, b, c, d in new_data:
            xdata1.append(a)
            ydata1.append(b)

            xdata2.append(math.sqrt(c) * a)
            ydata2.append(math.sqrt(d) * b)

            m1 = c
            m2 = d

        axs[0, 0].cla()
        axs[0, 1].cla()
        axs[1, 0].cla()

        # Keep the plot within a certain range
        # axs[0, 0].set_ylim([-1, 1])
        base = -150/1000
        lim = base * (10 ** pow)

        axs[0, 0].set_ylim([-0.25, 0.25])

        # axs[0, 1].set_ylim([-5, 5])
        axs[0, 1].set_ylim([lim, -lim])

        # axs[1, 0].set_ylim([-5, 5])
        axs[1, 0].set_ylim([lim, -lim])

        print(xdata2)
        print(ydata2)

        axs[0, 0].plot(xdata1, ydata1)
        axs[0, 1].plot(xdata2, ydata2)

        axs[1, 0].axline((xdata2[-1], ydata2[-1]), slope=-math.sqrt(m1 / m2), linewidth=2, color='r')
        axs[1, 0].plot(xdata2, ydata2, "o")



if __name__ == "__main__":
    p1 = Process(target=run_sim, args=(pow,))

    with open("data.txt", "w") as out:
        pass

    # File and queue setup
    filename = 'data.txt'

    # Start the file reading process
    file_reader_process = Process(target=read_new_lines, args=(filename, last_position))
    file_reader_process.start()

    p1.start()

    ani = animation.FuncAnimation(plt.gcf(), update, interval=100, frames=60)

    plt.show()

