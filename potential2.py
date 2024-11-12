# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:59:46 2024

@author: joahb
"""

import numpy as np
import matplotlib.pyplot as plt
import creategrid

# Constants
epsilon_0 = 8.854e-12  # permittivity of free space
min_distance = 0.001  # minimum distance to avoid singularity

# Generate 50 random charges
data = creategrid.qgrid(50)
charges = data['charges']
coordinates = data['coordinates']

# Set up the grid
x = np.arange(-10, 10, 0.5)
y = np.arange(-20, 20, 0.5)
X, Y = np.meshgrid(x, y)

# Define a function to calculate potential at each point due to a charge
def calculate_potential(xp, yp, q):
    r = np.sqrt((X - xp)**2 + (Y - yp)**2)
    r = np.maximum(r, min_distance)  # Set minimum distance to avoid infinity
    V = q / (4 * np.pi * epsilon_0 * r)
    return V

# Calculate total potential from all charges
V_total = np.zeros_like(X)
for charge, coord in zip(charges, coordinates):
    V_total += calculate_potential(coord[0], coord[1], charge)

# Plot the potential
plt.figure()
plt.contourf(X, Y, V_total, levels=100, cmap='RdYlBu')
plt.colorbar(label="Potential (V)")
plt.title("Electric Potential of Random Point Charges")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.savefig("potential_random.png")
plt.show()

# Calculate electric field as the negative gradient of the potential
Ey, Ex = np.gradient(-V_total, y, x)  # Note: np.gradient returns (y, x) gradients

# Plot the electric field using quiver
plt.figure()
plt.quiver(X, Y, Ex, Ey, color='black', scale=1e11)  # Adjust the scale as needed
plt.title("Electric Field of Random Point Charges")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.savefig("efield_random.png")
plt.show()