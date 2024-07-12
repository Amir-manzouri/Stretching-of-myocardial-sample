import numpy as np

def calculate_biaxial_stretch_with_fiber(theta):
    """
    Calculates biaxial stretching of a unit cube to 1.25 in x and y directions,
    then applies active contraction of TCa=3 in the fiber direction.
    The fiber is oriented at an angle theta with respect to the x-axis.

    Args:
    theta (float): Fiber angle in radians (rotation around Z axis)

    Returns:
    tuple: Contains various tensors and forces calculated
    """
    lambda_x = 1.25
    lambda_y = 1.25
    
    # Calculate lambda_y and lambda_z based on incompressibility
    lambda_z = 1 / (lambda_x*lambda_y)
    
    # Define deformation gradient tensor for biaxial stretch
    F = np.array([[lambda_x, 0, 0],
                  [0, lambda_y, 0],
                  [0, 0, lambda_z]])

    # Calculate right Cauchy-Green deformation tensor and its inverse
    C = np.dot(F.T, F)
    C_inv = np.linalg.inv(C)

    # Calculate Green-Lagrange strain tensor
    I = np.eye(3)
    E = 0.5 * (C - I)

    # Define rotation matrix for fiber orientation
    QT = np.array([[np.cos(theta), -np.sin(theta), 0],
                   [np.sin(theta), np.cos(theta), 0],
                   [0, 0, 1]])

    # Calculate strain tensor in fiber coordinate system
    E_fib = np.dot(QT.T, np.dot(E, QT))

    # Guccione constitutive equation parameters
    C1, C2, C3, C4 = 0.002, 8, 2, 4

    # Calculate strain energy
    Q = (C2 * E[0, 0]**2 + 
         C3 * (E[1, 1]**2 + E[2, 2]**2 + 2*E[1, 2]**2) + 
         2 * C4 * (E[0, 1]**2 + E[0, 2]**2))
    W = 0.5 * C1 * (np.exp(Q) - 1)
    WP = 0.5 * C1 * np.exp(Q)

    # Calculate distortional part of second Piola-Kirchhoff stress in fiber coordinates
    S_fib = np.zeros((3, 3))
    S_fib[0, 0] = WP * 2 * C2 * E_fib[0, 0]
    S_fib[1, 1] = WP * 2 * C3 * E_fib[1, 1]
    S_fib[2, 2] = WP * 2 * C3 * E_fib[2, 2]
    S_fib[0, 1] = S_fib[1, 0] = WP * 4 * C4 * E_fib[0, 1]
    S_fib[0, 2] = S_fib[2, 0] = WP * 4 * C4 * E_fib[0, 2]
    S_fib[1, 2] = S_fib[2, 1] = WP * 4 * C3 * E_fib[1, 2]

    # Add active stress to the distortional SP stress in the fiber direction
    TCa = 3
    S_fib[0, 0] += TCa

    # Calculate distortional SP stress in the reference coordinate system
    QT_rev = QT.T
    S = np.dot(QT_rev.T, np.dot(S_fib, QT_rev))

    # Calculate hydrostatic pressure (total SP stress in the third direction is zero)
    p = S[2, 2] / C_inv[2, 2]

    # Calculate total SP stress in the reference and fiber coordinate systems
    ST = S - p * C_inv
    ST_fib = S_fib - p * C_inv

    # Calculate total Cauchy stress in reference and fiber coordinates
    SigmaT = np.dot(F, np.dot(ST, F.T))
    SigmaT_fib = np.dot(F, np.dot(ST_fib, F.T))

    # Calculate deformed surface area and nodal forces
    Area_dia = 0.64 * 1.25 * np.sqrt(2)
    F_upper = SigmaT_fib[0, 0] * Area_dia / (4 * np.sqrt(2))
    F_lower = SigmaT_fib[1, 1] * Area_dia / (4 * np.sqrt(2))

    return F, C, E, E_fib, S, S_fib, ST, ST_fib, SigmaT, SigmaT_fib, p, F_upper, F_lower

def main():
    # Set fiber angle (45 degrees in radians)
    theta = np.pi / 4

    # Perform calculations
    results = calculate_biaxial_stretch_with_fiber(theta)
    F, C, E, E_fib, S, S_fib, ST, ST_fib, SigmaT, SigmaT_fib, p, F_upper, F_lower = results

    # Print results
    np.set_printoptions(precision=5)
    print("Deformation gradient tensor F:")
    print(F)
    print("\nRight Cauchy-Green deformation tensor C:")
    print(C)
    print("\nGreen-Lagrange strain tensor E:")
    print(E)
    print("\nGreen-Lagrange strain tensor in fiber coordinates E_fib:")
    print(E_fib)
    print("\nDistortional second Piola-Kirchhoff stress in reference coordinates S:")
    print(S)
    print("\nDistortional second Piola-Kirchhoff stress in fiber coordinates S_fib:")
    print(S_fib)
    print("\nTotal second Piola-Kirchhoff stress in reference coordinates ST:")
    print(ST)
    print("\nTotal second Piola-Kirchhoff stress in fiber coordinates ST_fib:")
    print(ST_fib)
    print("\nTotal Cauchy stress in reference coordinates SigmaT:")
    print(SigmaT)
    print("\nTotal Cauchy stress in fiber coordinates SigmaT_fib:")
    print(SigmaT_fib)
    print(f"\nHydrostatic pressure p: {p:.5f}")
    print(f"\nUpper nodal force F_upper: {F_upper:.5f}")
    print(f"\nLower nodal force F_lower: {F_lower:.5f}")

if __name__ == "__main__":
    main()