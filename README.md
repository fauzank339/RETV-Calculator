# Residential Envelope Transmission Value (RETV) Calculator

This Python script calculates the Residential Envelope Transmission Value (RETV) for a given building envelope configuration based on various parameters including climate zone, orientation factors, and component characteristics. The RETV is an important metric used in building energy efficiency assessments.

## Usage

1. **Input Parameters:**
   - Climate Zone: Choose one of the following climate zones: Composite, Hot-Dry, Warm-Humid, or Temperate.
   - Opaque Components: Enter the area and U-value (thermal transmittance) for opaque components (walls) associated with each cardinal direction (North, South, East, West).
   - Non-Opaque Components: Enter the area and U-value for non-opaque components (windows, doors) associated with North and South cardinal directions.
   - SHGC Equivalent: Enter the Solar Heat Gain Coefficient (SHGC) for non-opaque components associated with North and South cardinal directions.
   - Latitude: Enter the latitude of the location where the building is situated.

2. **Output:**
   - The calculated RETV value will be displayed based on the provided inputs.

## Climate Zone Coefficients

The script utilizes coefficients specific to each climate zone for RETV calculation. These coefficients are predefined based on typical climate characteristics.

## Orientation Factors

Orientation factors are determined based on the latitude of the location and the cardinal direction. These factors affect the energy performance of the building envelope.

## Function Overview

- `get_orientation_factor`: Calculates the orientation factor based on the latitude and cardinal direction.
- `calculate_RETV`: Computes the RETV using the given parameters and coefficients.

## How to Run

1. Ensure you have Python installed on your system.
2. Download the script `retv_calculator.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the script using the command: `python retv_calculator.py`.
6. Follow the on-screen instructions to input the required parameters.
7. The calculated RETV will be displayed as output.

This script provides a convenient tool for architects, engineers, and building designers to evaluate the energy performance of residential buildings and make informed decisions regarding building envelope design and energy efficiency measures.

For any further inquiries or issues, please contact the developer.
