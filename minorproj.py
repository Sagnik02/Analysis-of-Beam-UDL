def udl_beam_deflection_and_max_deflection(w, L, E, I, x):
    """
    Calculate the deflection of a simply supported UDL beam and its maximum deflection.

    Parameters:
    - w: Uniformly distributed load (force per unit length)
    - L: Span of the beam
    - E: Modulus of elasticity
    - I: Moment of inertia
    - x: Distance along the beam

    Returns:
    - deflection: Deflection at distance x
    - max_deflection: Maximum deflection
    """
    # Calculate the deflection directly
    deflection = (w * x / (24 * E * I)) * (L**3 - 2 * L * x**2 + x**3)

    # Calculate the maximum deflection directly
    max_deflection = 5*(w * L**4) / ( 384 * E * I)

    shearstress=w*(L/2-x)

    return deflection, max_deflection,shearstress
'''
# Example usage:
w = 120000  # UDL in N/m
L = 15   # Span in meters
E = 200000000000  # Modulus of elasticity in N/m^2
I = 0.00421875  # Moment of inertia in m^4
x_value = 15  # Distance along the beam where deflection is calculated

'''
# Example usage:
w = 120000
  # UDL in N/m
L = 15   # Span in meters
E =200000000000 # Modulus of elasticity in N/m^2
I =0.00421875 # Moment of inertia in m^4
x_value = 10  # Distance along the beam where deflection is calculated

deflection_result, max_deflection_result, shearstress = udl_beam_deflection_and_max_deflection(w, L, E, I, x_value)

print(f"The deflection at x={x_value} is: {deflection_result} meters")
print(f"The maximum deflection is: {max_deflection_result} meters")
print(f"The shear stress at x={x_value} is: {shearstress} N")
