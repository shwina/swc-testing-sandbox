from matplotlib.pyplot import *
import matplotlib.animation as animation
from nbody import *

ims = []

fig, ax = subplots()

def step(i):
    cla()
    offset_momentum(BODIES['sun'])
    advance(0.01, 10)

    x_list = []
    y_list = []

    for body in BODIES:
        [x, y, z] = BODIES[body][0]
        x_list.append(x)
        y_list.append(y)

    line = plot(x_list, y_list, '.')
    axis([-40, 40, -40, 40])
    return line,

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, bitrate=1800)

im_ani = animation.FuncAnimation(fig, step, range(500))
im_ani.save('planets.mp4', writer=writer)
