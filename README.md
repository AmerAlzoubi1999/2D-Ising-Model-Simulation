# 2D Ising Model Simulation

This Python code simulates the 2D Ising model using the Metropolis algorithm. The Ising model is a mathematical model in statistical mechanics that describes the behavior of magnetic spins in a lattice. In this simulation, we explore the behavior of spins on a 2D square lattice with interactions.

## Features

- Simulates the 2D Ising model with user-defined parameters.
- Visualizes the evolution of the lattice configurations over time.
- Plots the energy and magnetization as a function of Monte Carlo steps.

## Prerequisites

- Python 3.x
- `numpy` library
- `matplotlib` library

Install the required libraries using `pip`:

```bash
pip install numpy matplotlib
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/amer-alzoubi/ising-model-simulation.git
cd ising-model-simulation
```

2. Run the simulation:

```bash
python ising_model_simulation.py
```

3. The simulation will generate an animated GIF showing the evolution of the Ising model. The GIF will be saved as `ising_model_animation.gif`.

## Configuration

You can modify the following parameters in the code to customize the simulation:

- `L`: Size of the lattice (LxL).
- `J`: Interaction strength.
- `T`: Temperature (in energy units, kT).
- `num_steps`: Number of Monte Carlo steps in the simulation.
- `frames`: Number of frames in the output GIF.
- You can also customize the GIF frame rate and appearance in the code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This code is based on the Metropolis algorithm for simulating the Ising model.
- The Ising model is a classic problem in statistical physics and condensed matter physics.

## Author

- [Amer Alzoubi]
