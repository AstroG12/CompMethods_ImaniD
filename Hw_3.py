import numpy as np
import matplotlib.pyplot as plt
from Electric_pot import Electric_pot
from gradient import Grad
plt.rcParams["font.family"] = "helvetica"
plt.style.use('seaborn-white')


# point charge 1 info
dist_1 = 0.5

# point charge 2 info

dist_2 = -0.5

# Creating points in a square grid

x = np.linspace(-1.0, 1.0, 201)
y = np.linspace(-1.0, 1.0, 201)
X, Y = np.meshgrid(x, y)

# These points are used to just show the region 
x_s = np.linspace(-1.0, 1.0, 11)
y_s = np.linspace(-1.0, 1.0, 11)
X_s, Y_s = np.meshgrid(x_s, y_s)

# Calculating electric potential at all points

potential = Electric_pot(-0.52, 0, X, Y, 1) + Electric_pot(.52, 0, X, Y, 1)

# Calculating the E field at those points & and the speed for vector field

field = Grad(potential, 0.1)

# Create figure

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(11, 11), gridspec_kw={
    'width_ratios': [5, 5],
    'height_ratios': [5, 5]})

axes[1, 1].axis("off")

# Plot the points made(gray) and particle (red and blue)


# axes[0, 0].scatter(X, Y, color="grey")  # True points measured
axes[0, 0].scatter(X_s, Y_s, color="grey")  # Points for a visual understanding
axes[0, 0].grid()
axes[0, 0].scatter(dist_1, 0, color="r")
axes[0, 0].scatter(dist_2, 0, color="b")
axes[0, 0].title.set_text("Region to Find Potentials(Charges are the red and blue points)")
axes[0, 0].set_xlabel("X(m)")
axes[0, 0].set_ylabel("Y(m)")

# Plots image of potential

cmap = axes[0, 1].imshow(potential / 1e10, vmin=0, vmax=5, extent=[
    0, 1, 0, 1], origin="lower", cmap="copper_r")
axes[0, 1].title.set_text("Map of Potentials (Volts * 10e10)")
axes[0, 1].set_xlabel("X(m)")
axes[0, 1].set_ylabel("Y(m)")

# Plots E-field

axes[1, 0].streamplot(X, Y, field[0] * -1, field[1] * -1, color="k", density=[
    0.5, 1])
axes[1, 0].scatter(dist_1, 0, color="r")
axes[1, 0].scatter(dist_2, 0, color="b")
axes[1, 0].title.set_text("Electric Field (Volts / m)")
axes[1, 0].set_xlabel("X(m)")
axes[1, 0].set_ylabel("Y(m)")

plt.colorbar(cmap, ax=axes[0, 1], fraction=0.046, pad=0.04)
fig.suptitle("Homework #3")
plt.show()
