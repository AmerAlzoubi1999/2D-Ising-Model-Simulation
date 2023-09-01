import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define constants
L = 20          # Size of the lattice (LxL)
J = 1.0         # Interaction strength
T = 2.0         # Temperature (in energy units, kT)

# Initialize the lattice with random spins (+1 or -1)
spins = np.random.choice([1, -1], size=(L, L))

# Function to calculate the energy of a given configuration
def calculate_energy(spins):
    energy = 0
    for i in range(L):
        for j in range(L):
            nb_sum = spins[i, (j+1)%L] + spins[i, (j-1)%L] + spins[(i+1)%L, j] + spins[(i-1)%L, j]
            energy += -J * spins[i, j] * nb_sum
    return energy / 2  # Divide by 2 to avoid double-counting

# Function to perform a Metropolis update for a single spin
def metropolis_update(spins, temperature):
    i, j = np.random.randint(0, L, 2)  # Randomly select a spin
    delta_energy = 2 * J * spins[i, j] * (spins[i, (j+1)%L] + spins[i, (j-1)%L] + spins[(i+1)%L, j] + spins[(i-1)%L, j])
    
    if delta_energy <= 0 or np.random.rand() < np.exp(-delta_energy / temperature):
        spins[i, j] *= -1  # Flip the spin with Metropolis probability

# Parameters for the simulation
num_steps = 100
frames = 100  # Number of frames for the GIF

# Lists to store data for plotting
energies = []
magnetizations = []

# Function to update the animation
def update(frame):
    plt.clf()
    for _ in range(num_steps // frames):
        metropolis_update(spins, T)
    energy = calculate_energy(spins)
    magnetization = np.sum(spins)
    energies.append(energy)
    magnetizations.append(magnetization)
    plt.imshow(spins, cmap='coolwarm', vmin=-1, vmax=1)
    plt.colorbar(label='Spin', ticks=[-1, 0, 1])
    plt.title(f'Step: {frame*num_steps//frames}, Energy: {energy}, Magnetization: {magnetization}')
    plt.xlabel('X')
    plt.ylabel('Y')

# Create the animation
fig, ax = plt.subplots(figsize=(6, 6))
ani = FuncAnimation(fig, update, frames=frames, repeat=False)

# Save the animation as a GIF
ani.save('ising_model_animation.gif', writer='pillow', fps=10)
plt.show()
