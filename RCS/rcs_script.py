def malfunction_detection(thrust_values):
    """
    Checks input thrust values for each thruster against set limits.
    Prints a message if a thruster exceeds thrust, flow rate, or exhaust velocity limits.
    """

    MAX_THRUST = 100          # Newtons
    MAX_FLOW_RATE = 0.05      # kg/s
    MAX_EXHAUST_VELOCITY = 2000  # m/s

    for thruster, params in thrust_values.items():
        thrust = params.get("thrust", 0)
        m_dot = params.get("flow_rate", 0)
        v_e = params.get("exhaust_velocity", 0)

        if thrust > MAX_THRUST:
            diff = thrust - MAX_THRUST
            print(f"{thruster} exceeds thrust limit by {diff:.2f} N")
        if m_dot > MAX_FLOW_RATE:
            diff = m_dot - MAX_FLOW_RATE
            print(f"{thruster} exceeds flow rate limit by {diff:.4f} kg/s")
        if v_e > MAX_EXHAUST_VELOCITY:
            diff = v_e - MAX_EXHAUST_VELOCITY
            print(f"{thruster} exceeds exhaust velocity limit by {diff:.2f} m/s")


def velocity_change_calculation(m_dot, v_e, time_elapsed, spacecraft_mass=500):
    """
    Calculates delta-v from mass flow rate, exhaust velocity, and time elapsed.
    """
    thrust = m_dot * v_e
    delta_v = (thrust * time_elapsed) / spacecraft_mass
    return delta_v


def main():
    """
    Main function to test the RCS functions.
    """

    test_cases = [
        {"Thruster 1": {"flow_rate": 0.02, "exhaust_velocity": 1000, "thrust": 0.02*1000}, "time": 5},
        {"Thruster 2": {"flow_rate": 0.06, "exhaust_velocity": 1000, "thrust": 0.06*1000}, "time": 3},
        {"Thruster 3": {"flow_rate": 0.05, "exhaust_velocity": 2000, "thrust": 0.05*2000}, "time": 10},
    ]

    for i, case in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")

        # Extract time and thruster data
        time_elapsed = case["time"]
        thruster_data = {k: v for k, v in case.items() if k != "time"}

        # Run malfunction detection
        malfunction_detection(thruster_data)

        # Calculate delta-v for each thruster
        for thruster, params in thruster_data.items():
            delta_v = velocity_change_calculation(params["flow_rate"], params["exhaust_velocity"], time_elapsed)
            print(f"{thruster} calculated delta_v: {delta_v:.2f} m/s")

        print("-" * 30)


if __name__ == "__main__":
    main()
