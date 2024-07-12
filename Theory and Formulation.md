# Theory and Formulation for Mechanics Simulation of a unit cube

## 1. Introduction

This document details the theoretical framework and formulations used in simulating the active contraction of ventricular muscle samples (unit cube).

## 2. Uniaxial Extension of a Unit Cube

We begin with the extension of a unit cube subjected to a deformation gradient tensor F, which increases the x-length of the cube by 50%.

!(Figures/pic1.png)

### Constitutive Law

We employ the transversely isotropic constitutive law by Guccione:

$$
W = \frac{C}{2}(e^Q - 1)
$$

Where:

$$
Q = b_f E_{ff}^2 + b_t(E_{ss}^2 + E_{nn}^2 + 2E_{sn}^2) + 2b_{fs}(E_{fs}^2 + E_{fn}^2)
$$

- $W$ represents the strain energy function
- $E_{ij}$ denotes components of the Green–Lagrange strain tensor E
- Fibers are aligned in the x-direction
- Constitutive parameters: $C = 2$ Pa, $b_f = 8$, $b_t = 2$, $b_{fs} = 4$

### Deformation Gradient Tensor

The deformation gradient tensor F is defined as:

$$
F = \begin{bmatrix}
1.5 & 0 & 0 \\
0 & \lambda_y & 0 \\
0 & 0 & \lambda_z
\end{bmatrix}
$$

Due to incompressibility:

$$
\lambda_x \times \lambda_y \times \lambda_z = 1
$$

$$
1.5 \times \lambda_y^2 = 1
$$

$$
\lambda_y = \lambda_z = 0.82
$$

### Stress Calculations

Right Cauchy-Green deformation tensor C is defined as:

$$
C  = \begin{bmatrix}
2.25 & 0 & 0 \\
0 & 0.67 & 0 \\
0 & 0 & 0.67
\end{bmatrix}
$$

Green-Lagrange strain tensor:

   $$
   E = \frac{1}{2}(C - I) = \begin{bmatrix}
   0.625 & 0 & 0 \\
   0 & -0.17 & 0 \\
   0 & 0 & -0.17
   \end{bmatrix}
   $$

Distortional component of second Piola-Kirchhoff stress
   
   $$
   S = \frac{\partial W}{\partial E} = \begin{bmatrix}
   0.25 & 0 & 0 \\
   0 & -0.017 & 0 \\
   0 & 0 & -0.017
   \end{bmatrix} \text{ Pa}
   $$

Total second Piola-Kirchhoff stress (including hydrostatic pressure):

   $$
   S_{ij} = \frac{\partial W}{\partial E_{ij}} - p_{hyd} C_{ij}^{-1}
   $$
   where \( p_{hyd} = -0.0113 \) Pa

Cauchy stress:

   $$
   \sigma_{total} = FSF^T = \begin{bmatrix}
   0.58 & 0 & 0 \\
   0 & 0 & 0 \\
   0 & 0 & 0
   \end{bmatrix} \text{ Pa}
   $$

Nodal force:

   $$
   RF_{nodal} = \frac{\sigma_{xx} \times A_{def}}{4} = 0.097 \text{ N}
   $$

## 3. Active Tension

Active contraction is modelled by superimposing passive stress and active contractile stress:

$$
S = S_{passive} + S_{active}
$$

We use a simplified approach with a constant term $T_{ca}$ to represent active stress:

$$
S_{active} = T_{ca} \hat{e}_x \otimes \hat{e}_x
$$

Where $\hat{e}_x$ is the unit vector in the fibre direction.

For $T_{ca} = 3$ Pa, the updated stresses and nodal force are:

$$
S_{xx} = S_{passive,xx} + S_{active,xx} = 0.26 + 3 = 3.26 \text{ Pa}
$$

$$
\sigma = \begin{bmatrix}
7.33 & 0 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{bmatrix} \text{ Pa}
$$

$$
RF_{nodal} = 1.222 \text{ N}
$$

## 4. Arbitrary Fiber Direction

We now consider biaxial stretching with fibres oriented at an arbitrary angle. We present calculations for a fibre angle of 45°.



$$
F_{ref} = \begin{bmatrix}
1.25 & 0 & 0 \\
0 & 1.25 & 0 \\
0 & 0 & 0.64
\end{bmatrix}
$$

### Coordinate Systems

We use two coordinate systems:
- Reference coordinate system (XYZ)
- Fiber coordinate system (fiber-sheet-normal)

The rotation matrix between these systems is:

$$
R = \begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0 \\
\sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

### Stress Calculations

Second Piola-Kirchhoff stress in fibre coordinates:
   
   $$
   S_{fib} = \frac{\partial W}{\partial E_{fib}} = \begin{bmatrix}
   0.012 & 0 & 0 \\
   0 & 0.0029 & 0 \\
   0 & 0 & -0.0031
   \end{bmatrix} \text{ Pa}
   $$

Adding active stress:
   
   $$
   S_{fib,ff} = S_{fibr,passive,ff} + S_{fib,active,ff} = 0.012 + 3 = 3.012 \text{ Pa}
   $$

Total second Piola-Kirchhoff stress in reference coordinates:
   
   $$
   S_{total,ref} = \begin{bmatrix}
   1.51 & 1.50 & 0 \\
   1.50 & 1.51 & 0 \\
   0 & 0 & 0
   \end{bmatrix} \text{ Pa}
   $$

Total Cauchy stress in reference coordinates:
   
   $$
   \sigma_{total,ref} = \begin{bmatrix}
   2.36 & 2.35 & 0 \\
   2.35 & 2.36 & 0 \\
   0 & 0 & 0
   \end{bmatrix} \text{ Pa}
   $$

Nodal reaction forces:
    
   $$
   RF_1 = 0.94 \text{ N}
   $$
   $$
   RF_2 = 0.0012 \text{ N}
   $$
