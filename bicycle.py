# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:03:11 2024

@author: joahb
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
v0 = 4.0       # initial velocity in m/s
m = 70.0       # mass of the cyclist in kg
P = 400.0      # power output in watts
dt = 0.1       # time step in seconds
t_max = 200.0  # total simulation time in seconds

# Time array and velocity array
t = np.arange(0, t_max + dt, dt)
v = np.zeros_like(t)
v[0] = v0  # initial velocity

# Euler method to solve the equation dv/dt = P / (m * v)
for i in range(1, len(t)):
    dv_dt = P / (m * v[i - 1])
    v[i] = v[i - 1] + dv_dt * dt

# Plot the velocity over time
plt.figure(figsize=(10, 6))
plt.plot(t, v, label="Velocity of Cyclist", color="blue")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity of a Cyclist Without Drag Over Time")
plt.legend()
plt.grid(True)
plt.savefig("bicycle_velocity.png")
plt.show()