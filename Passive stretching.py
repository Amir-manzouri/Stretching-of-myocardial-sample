import numpy as np

def calculate_uniaxial_stretch():
    """
    Solves the uniaxial stretch of a unit cube by stretching it 50% in the x-direction.
    Guccione equation has been used as the passive constitutie law
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
    Ad = lambda_z * lambda_y  # Deformed area
    RF = Sigma[0, 0] * Ad / 4  # Nodal force for each node
    print(f"\nNodal force: {RF:.6f}")

    return F, ST, Sigma, RF


def main():
    F, ST, Sigma, RF = calculate_uniaxial_stretch()

if __name__ == "__main__":
    main()