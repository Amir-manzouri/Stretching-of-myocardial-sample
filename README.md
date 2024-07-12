# Unit Cube Mechanics Simulation

This repository contains a set of Python scripts for simulating various mechanical behaviours of a unit cube, including passive stretching, active contraction, and fiber-oriented deformation.

## Scripts

### 1. Passive Stretching (`Passive_stretching.py`)

This script simulates the uniaxial stretching of a unit cube by 50% in the x-direction. It uses the Guccione constitutive equation to model the passive mechanical behaviour of the material.

Key features:
- Calculates deformation gradient, right Cauchy-Green deformation tensor, and Green-Lagrange strain tensor
- Implements the Guccione constitutive equation for passive stress
- Computes second Piola-Kirchhoff stress, Cauchy stress, and nodal forces

### 2. Active Contraction (`Active_contraction.py`)

Building upon the passive stretching model, this script adds active contraction to the simulation. It provides two different formulations for incorporating active stress:
1. A simple additive model (default)
2. The Hunter formulation (commented out by default)

Key features:
- Includes all calculations from the passive stretching model
- Adds active contraction stress to the passive stress
- Allows switching between different active stress formulations

### 3. Fiber Angle Deformation (`Fiber_angle.py`)

This script simulates the biaxial stretching of a unit cube with a defined fibre direction. It stretches the cube to 1.25 in both the x and y directions and applies active contraction along the fibre direction.

Key features:
- Implements biaxial stretching
- Incorporates fibre orientation at a specified angle
- Calculates stresses and strains in both reference and fibre coordinate systems
- Computes nodal forces for the deformed geometry

## Usage

To run any scripts, you only need to install Python and NumPy.
