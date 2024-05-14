def get_orientation_factor(cardinal_direction, latitude):
    """
    Calculate the orientation factor based on the cardinal direction and latitude.

    Args:
    - cardinal_direction (str): Cardinal direction (e.g., "North", "South").
    - latitude (float): Latitude of the location.

    Returns:
    - float: Orientation factor.
    """
    if latitude >= 23.5:
        omega_factors = {
            "North": 0.659,
            "North-east": 0.906,
            "East": 1.155,
            "South-east": 1.125,
            "South": 0.966,
            "South-west": 1.124,
            "West": 1.156,
            "North-west": 0.908
        }
    else:
        omega_factors = {
            "North": 0.550,
            "North-east": 0.829,
            "East": 1.155,
            "South-east": 1.211,
            "South": 1.089,
            "South-west": 1.202,
            "West": 1.143,
            "North-west": 0.821
        }

    if cardinal_direction in omega_factors:
        return omega_factors[cardinal_direction]
    else:
        print("Invalid cardinal direction. Please enter a valid cardinal direction.")
        return None


def calculate_RETV(A_envelope, a, b, c, opaque_components, non_opaque_components, SHGC_eq, omega_factors):
    """
    Calculate Residential Envelope Transmission Value (RETV) based on the given parameters.

    Args:
    - A_envelope (float): Envelope area (excluding roof) of dwelling units (m²).
    - a (float): Coefficient 'a' for the specific climate zone.
    - b (float): Coefficient 'b' for the specific climate zone.
    - c (float): Coefficient 'c' for the specific climate zone.
    - opaque_components (dict): Dictionary containing areas and U-values of opaque components.
    - non_opaque_components (dict): Dictionary containing areas and U-values of non-opaque components.
    - SHGC_eq (dict): Dictionary containing SHGC equivalent values of non-opaque components.
    - omega_factors (dict): Dictionary containing orientation factors for cardinal directions.

    Returns:
    - float: Calculated RETV.
    """
    sum_opaque = sum(sum(component['area'] * component['U'] * omega_factors[dir] for component in components) for dir, components in opaque_components.items())
    sum_non_opaque = sum(sum(component['area'] * component['U'] * SHGC_eq[dir] * omega_factors[dir] for component in components) for dir, components in non_opaque_components.items())
    sum_SHGC_eq = sum(sum(component['area'] * SHGC_eq[dir] * omega_factors[dir] for component in components) for dir, components in non_opaque_components.items())
    
    retv = (1 / A_envelope) * (a * sum_opaque + b * sum_non_opaque + c * sum_SHGC_eq)
    return retv


# Coefficients for different climate zones
coefficients = {
    "Composite": (6.06, 1.85, 68.99),
    "Hot-Dry": (6.06, 1.85, 68.99),
    "Warm-Humid": (5.15, 1.31, 65.21),
    "Temperate": (3.38, 0.37, 63.69)
}

# Example usage:
print("Please enter the required information:")
climate_zone = input("Enter climate zone (Composite, Hot-Dry, Warm-Humid, or Temperate): ").strip()

# Ensure valid climate zone input
while climate_zone not in coefficients:
    print("Invalid climate zone. Please enter a valid climate zone.")
    climate_zone = input("Enter climate zone (Composite, Hot-Dry, Warm-Humid, or Temperate): ").strip()

# Clarify units for user inputs
print("Please enter the following values in the specified units:")

# User input for opaque components associated with cardinal directions
opaque_components = {}
for dir in ["North", "South", "East", "West"]:
    num_opaque_components = int(input(f"How many opaque components do you have for {dir}? "))
    opaque_components[dir] = []
    for _ in range(num_opaque_components):
        area = float(input(f"Enter area of opaque component for {dir} (m²): "))
        U = float(input(f"Enter U-value of opaque component for {dir} (W/m².K): "))
        opaque_components[dir].append({"area": area, "U": U})

# User input for non-opaque components associated with cardinal directions
non_opaque_components = {}
for dir in ["North", "South"]:
    num_non_opaque_components = int(input(f"How many non-opaque components do you have for {dir}? "))
    non_opaque_components[dir] = []
    for _ in range(num_non_opaque_components):
        area = float(input(f"Enter area of non-opaque component for {dir} (m²): "))
        U = float(input(f"Enter U-value of non-opaque component for {dir} (W/m².K): "))
        non_opaque_components[dir].append({"area": area, "U": U})

# Calculate total envelope area by summing up areas of all opaque and non-opaque components
A_envelope = sum(sum(component['area'] for component in components) for components in opaque_components.values()) + \
             sum(sum(component['area'] for component in components) for components in non_opaque_components.values())

# User input for SHGC equivalent values associated with cardinal directions
SHGC_eq = {}
for dir in ["North", "South"]:
    SHGC_eq[dir] = float(input(f"Enter SHGC of non-opaque component for {dir}: "))

# Calculate latitude from user input
latitude = float(input("Enter the latitude of the location: "))

# Calculate omega factors for each cardinal direction based on latitude
omega_factors = {dir: get_orientation_factor(dir, latitude) for dir in opaque_components}

# Get coefficients for the selected climate zone
a, b, c = coefficients[climate_zone]

# Calculate RETV
retv = calculate_RETV(A_envelope, a, b, c, opaque_components, non_opaque_components, SHGC_eq, omega_factors)
print("RETV:", retv)
