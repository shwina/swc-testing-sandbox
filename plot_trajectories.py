from matplotlib.pyplot import *
import matplotlib.animation as animation
from nbody import *


nsteps = 500
ims = []

fig, ax = subplots()

def step(i):

    offset_momentum(BODIES['sun'])
    advance(0.1, nsteps)

    x_list = []
    y_list = []

    for body in BODIES:
        [x, y, z] = BODIES[body][0]
        x_list.append(x)
        y_list.append(y)

    line = plot(x_list, y_list, '.')
    axis([-40, 40, -40, 40])
    return line,

im_ani = animation.FuncAnimation(fig, step, range(20))
show()
