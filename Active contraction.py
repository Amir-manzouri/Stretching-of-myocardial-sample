import numpy as np

def calculate_uniaxial_stretch():
    """
    Solves the uniaxial stretch of a unit cube by stretching it 50% in the x-direction.
    Guccione equation has been used as the passive constitutie law
    This function also adds active contraction (isometric contraction) using two different formulations
    Default formualtion is simple TCa parameter
    The second formualtion (which is commented out): Hunter equation
    """
    # Stretching ratio in x direction (50% stretch)
    lambda_x = 1.5

    # Calculate lambda_y and lambda_z based on incompressibility
    lambda_y = lambda_z = 1 / np.sqrt(lambda_x)

    # Define deformation gradient tensor
    F = np.array([[lambda_x, 0, 0],
                  [0, lambda_y, 0],
                  [0, 0, lambda_z]])

    print("Deformation gradient tensor:")
    print(F)

    # Calculate right Cauchy-Green deformation tensor
    C = np.dot(F.T, F)
    print("\nRight Cauchy-Green deformation tensor:")
    print(C)

    C_inv = np.linalg.inv(C)

    # Calculate Green-Lagrange strain tensor
    I = np.eye(3)
    E = 0.5 * (C - I)
    print("\nGreen-Lagrange strain tensor:")
    print(E)

    # Guccione constitutive equation parameters
    C1, C2, C3, C4 = 0.002, 8, 2, 4

    # Calculate strain energy
    Q = (C2 * E[0, 0]**2 + 
         C3 * (E[1, 1]**2 + E[2, 2]**2 + 2*E[1, 2]**2) + 
         2 * C4 * (E[0, 1]**2 + E[0, 2]**2))
    W = 0.5 * C1 * (np.exp(Q) - 1)
    WP = 0.5 * C1 * np.exp(Q)

    # Calculate distortional part of second Piola-Kirchhoff stress
    S = np.zeros((3, 3))
    S[0, 0] = WP * 2 * C2 * E[0, 0]
    S[1, 1] = WP * 2 * C3 * E[1, 1]
    S[2, 2] = WP * 2 * C3 * E[2, 2]
    S[0, 1] = S[1, 0] = WP * 4 * C4 * E[0, 1]
    S[0, 2] = S[2, 0] = WP * 4 * C4 * E[0, 2]
    S[1, 2] = S[2, 1] = WP * 4 * C3 * E[1, 2]

    # Calculate hydrostatic pressure
    # Since there is no force in y or z direction, total stress in these directions equals zero
    P = S[1, 1] / C_inv[1, 1]
    print(f"\nHydrostatic pressure: {P:.6f}")

    # Calculate total second Piola-Kirchhoff stress
    ST = S - P * C_inv
    print("\nTotal second Piola-Kirchhoff stress:")
    print(ST)

    # Calculate Cauchy stress
    Sigma = np.dot(F, np.dot(ST, F.T))
    print("\nCauchy stress:")
    print(Sigma)

    # Calculate nodal forces
    Ad = lambda_y * lambda_z  # Deformed area
    RF = Sigma[0, 0] * Ad / 4  # Nodal force for each node
    print(f"\nNodal force: {RF:.6f}")

    return F, ST, Sigma, RF

def add_active_contraction(F, ST, TCa):
    """
    Adds active contraction to the passive stress using two different formulations.
    
    Args:
    F (ndarray): Deformation gradient tensor
    ST (ndarray): Total second Piola-Kirchhoff stress
    TCa (float): Active contraction magnitude
    
    Returns:
    tuple: Updated second Piola-Kirchhoff stress, Cauchy stress, and nodal force
    """
    ST2 = ST.copy()

    # Two different formulations for adding active contraction:
    
    # 1. Simple equation: T_tot = Tp + Ta
    ST2[0, 0] = ST[0, 0] + TCa

    # 2. Hunter formulation: T_tot = Tp + T_ca(1 + Beta(lambda - 1))
    # Beta = 1.45
    # ST2[0, 0] = ST[0, 0] + TCa * (1 + Beta * (F[0, 0] - 1))

    Sigma2 = np.dot(F, np.dot(ST2, F.T))
    Ad = F[1, 1] * F[2, 2]  # Deformed area
    RF2 = Sigma2[0, 0] * Ad / 4  # Updated nodal force

    return ST2, Sigma2, RF2

def main():
    F, ST, Sigma, RF = calculate_uniaxial_stretch()
    
    print("\nAdding active contraction:")
    TCa = 3  # Active contraction magnitude
    ST2, Sigma2, RF2 = add_active_contraction(F, ST, TCa)
    
    print("\nUpdated second Piola-Kirchhoff stress:")
    print(ST2)
    print("\nUpdated Cauchy stress:")
    print(Sigma2)
    print(f"\nUpdated nodal force: {RF2:.6f}")

if __name__ == "__main__":
    main()