def available_power(voltage, current):
    """
    Calculates the instantaneous incoming power from the solar panels,
    checking for inputs that exceed the solar panels' maximum limits.
    """
    max_voltage = 28  #  Maximum voltage limit
    max_current = 10  # Maximum current limit
    voltage = min(voltage, max_voltage) # Limit voltage to max
    current = min(current, max_current) # Limit current to max
    # Power = Voltage * Current
    power = voltage * current
    return power



def battery_charging(power_delivered, time_elapsed):
    """ Calculates the total energy available for battery charging."""
    #Energy (in joules) = Power (in watts) * Time (in seconds)
    max_power = 280  # Maximum power limit in watts
    power_delivered = min(power_delivered, max_power)  # Limit power to max
    energy = power_delivered * time_elapsed
    return energy

#For additional functionality, we can add a function to calculate total energy over multiple intervals [Check + Assignment]
def total_energy_profile(intervals):
    total_energy = 0.0

    for voltage, current, duration in intervals:
        # Use the existing functions
        power = available_power(voltage, current)
        energy = battery_charging(power, duration)
        total_energy += energy

    return total_energy
# Example usage test case 
check_plus_test1 = [(22, 7, 300), (40, 7, 60), (25, 10, 200), (10, 4, 600)]
check_plus_test2 = [(0, 7, 300), (30, 10, 60), (28, 10, 200), (10, 10, 10)]
print("Total energy for Check + 1:", total_energy_profile(check_plus_test1), "Joules")
print("Total energy for Check + 2:", total_energy_profile(check_plus_test2), "Joules")

def main():
    """
    Main function to test the EPS functions.
    """
    # Example test cases from the project description
    test_cases = [
        (25, 10, 3600),
        (30, 8, 1800),
        (15, 12, 7200)
    ]

    for i, (v, i_current, t) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        power = available_power(v, i_current)
        print(f"Available Power: {power:.2f} W")
        energy = battery_charging(power, t)
        print(f"Energy for charging: {energy:.2f} J")
        print("-" * 20)

if __name__ == "__main__":
    main()
