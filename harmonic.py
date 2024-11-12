# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:19:37 2024

@author: joahb
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 2.0     # mass in kg
k = 3.0     # spring constant in N/m
y0 = 2.0    # initial position
V0 = 0.0    # initial velocity
t_max = 20  # maximum time in seconds
dt = 0.01   # time step

def euler_solver(C, t_max, dt):
    # Number of time steps
    steps = int(t_max / dt)
    
    # Arrays to store time, displacement (y), and velocity (V)
    t = np.linspace(0, t_max, steps)
    y = np.zeros(steps)
    V = np.zeros(steps)
    
    # Initial conditions
    y[0] = y0
    V[0] = V0

    # Euler method loop
    for i in range(steps - 1):
        # Update y and V using the differential equations
        dy_dt = V[i]
        dV_dt = -C / m * V[i] - (k / m) * y[i]
        
        y[i + 1] = y[i] + dy_dt * dt
        V[i + 1] = V[i] + dV_dt * dt

    # Plot displacement vs time
    plt.figure()
    plt.plot(t, y, label=f"C = {C}")
    plt.xlabel("Time (s)")
    plt.ylabel("Displacement (m)")
    plt.title(f"Damped Harmonic Oscillator (C = {C})")
    plt.legend()
    plt.savefig(f"harmonic_C_{C}.png")
    plt.show()

# Define values for C for each case
C_values = {
    "No Damping": 0,
    "Critically Damped": 4 * np.sqrt(k * m),
    "Underdamped": 2,
    "Overdamped": 10,
}

# Run the solver for each damping case
for label, C in C_values.items():
    print(f"Running simulation for: {label}")
    euler_solver(C, t_max, dt)
