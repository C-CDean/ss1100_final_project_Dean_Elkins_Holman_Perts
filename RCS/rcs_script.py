import numpy as np

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

def velocity_change_calculation(m_dot_list, v_e_list, time_list, directions=None, spacecraft_mass=500):
    """
    Calculate delta-v vector OR scalar depending on inputs.

    If directions is None:
        Treat inputs as scalars and return a single delta-v value.
    If directions is provided:
        Treat inputs as lists and compute a 3D delta-v vector.
    """

    # === Case 1: Scalar mode (used by the unit test) ===
    if directions is None:
        thrust = m_dot_list * v_e_list           # T = m_dot * v_e
        delta_v = (thrust * time_list) / spacecraft_mass
        return delta_v

    # === Case 2: Vector mode (original behavior) ===
    delta_v_vector = np.zeros(3)

    for m_dot, v_e, t, dir_vec in zip(m_dot_list, v_e_list, time_list, directions):
        dv_mag = (m_dot * v_e * t) / spacecraft_mass
        delta_v_vector += dv_mag * np.array(dir_vec)

    return delta_v_vector

def main():
    """
    Main function to test thruster malfunctions and vector delta-v.
    """
    spacecraft_mass = 500  # kg

    # Thruster test data
    test_cases = [
        {
            "name": "Thruster 1",
            "flow_rate": 0.04,
            "exhaust_velocity": 2000,
            "time": 15,
            "direction": [1, 0, 0]  # X-axis
        },
        {
            "name": "Thruster 2",
            "flow_rate": 0.03,
            "exhaust_velocity": 2000,
            "time": 4,
            "direction": [0, 1, 0]  # Y-axis
        },
        {
            "name": "Thruster 3",
            "flow_rate": 0.01,
            "exhaust_velocity": 2000,
            "time": 3,
            "direction": [0, 0, 1]  # Z-axis
        }
    ]

    # Prepare data for vector calculation
    m_dot_list = []
    v_e_list = []
    time_list = []
    directions = []
    thrust_values = {}

    for thruster in test_cases:
        m_dot = thruster["flow_rate"]
        v_e = thruster["exhaust_velocity"]
        t = thruster["time"]
        dir_vec = thruster["direction"]
        name = thruster["name"]

        # Add to lists for vector calculation
        m_dot_list.append(m_dot)
        v_e_list.append(v_e)
        time_list.append(t)
        directions.append(dir_vec)

        # Compute thrust for malfunction detection
        thrust_values[name] = {
            "thrust": m_dot * v_e,
            "flow_rate": m_dot,
            "exhaust_velocity": v_e
        }

    # Run malfunction detection
    print("=== Malfunction Detection ===")
    malfunction_detection(thrust_values)

    # Calculate delta-v vector
    delta_v = velocity_change_calculation(m_dot_list, v_e_list, time_list, directions, spacecraft_mass)
    
    print("\n=== Vector Delta-V ===")
    print(f"Delta-V vector (m/s): X={delta_v[0]:.2f}, Y={delta_v[1]:.2f}, Z={delta_v[2]:.2f}")
    print(f"Total Delta-V magnitude: {np.linalg.norm(delta_v):.2f} m/s")

if __name__ == "__main__":
    main()