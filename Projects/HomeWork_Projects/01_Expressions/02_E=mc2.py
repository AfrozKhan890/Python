"""
Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
E = m * c**2
Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.
"""


def mass_to_energy():
    C = 299792458  # Speed of light
    
    while True:
        MassInput = input("Enter mass in kg (or type 'exit' to quit): ")
        
        #  User input ko lowercase m convert krny k lie .lower use kia h 
        if MassInput.lower() == "exit":
            print("You Exit the program.")
            break  # Program band karne ke liye break use kia g
        
        try:
            energy = float(MassInput) * C**2  # Mass input lene ke baad calculation
            print(f"Equivalent Energy: {energy:,.0f} Joules\n")  # Normal decimal format with commas
        except ValueError:
            print("Invalid input! Please enter a valid number or type 'exit' to quit.\n")

mass_to_energy()
