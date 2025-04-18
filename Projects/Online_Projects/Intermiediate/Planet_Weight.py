def planetary_weight_calculator():
    gravity_factors = {
        "mercury": 0.376,
        "venus": 0.889,
        "mars": 0.378,
        "jupiter": 2.36,
        "saturn": 1.081,
        "uranus": 0.815,
        "neptune": 1.14
    }

    earth_weight = float(input("Enter your weight on Earth (kg): "))

    planet = input("Enter the name of a planet (e.g., Mars, Jupiter, etc.): ").strip().lower()

    if planet in gravity_factors:
        planet_weight = round(earth_weight * gravity_factors[planet], 2)
        print(f"Your weight on {planet.capitalize()} would be {planet_weight} kg.")
    else:
        print("Sorry, that planet is not in our solar system list.")

# Call function
planetary_weight_calculator()
