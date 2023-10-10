"""
question5.py - numpy

We are going to model vibrations on a wire using finite differences.

The current displacement of a wire is represented by a numpy array of floats, current.
We also hold the displacement of the wire in the previous time step, previous.

Each timestep, the displacement is updated with the following update equation.
    next = 2 * current - previous + k * laplace(current)

where laplace(array) returns an array of the same size such that,
    laplace(array)[i] == 2 * array[i] - array[i + 1] - array[i - 1]
where array[i + 1] and array[i - 1] are treated as 0 if they are out of bounds.

a) implement the laplace function.

b) the update function will take the current and previous value,
   and update these to return new current and previous values one timestep on.

if implemented correctly, running the program will show an animation of the
displacement bouncing off the sides.

Code Functionality (5)
a) 3 POINTS
b) 2 POINTS
"""
import numpy as np
import matplotlib.pyplot as plt

k = 0.1

def laplace(array):
    return array

def update(current, previous):
    return (current, current)


## Plotting Code - No need to change the code below.
xs = np.arange(-15, 15, 0.1)
current = np.exp(-xs * xs / 2)
previous = np.exp(-(xs - 0.03) * (xs - 0.03) / 2)

## Pyplot Setup
plt.ylim(-3, 3)
plot, = plt.plot(xs, current)
plt.show(block=False)

## Simulation and Display
while(plt.get_fignums()):
    (current, previous) = update(current, previous)
    plot.set_ydata(current)
    plt.pause(1 / 60)
