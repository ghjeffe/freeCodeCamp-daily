def tire_status(tire_pressures, range_bar):

    psi_in_bar = 14.5038
    tire_status = ["Low", "Good", "High"]
    range_psi = [range_bar[0] * psi_in_bar, range_bar[1] * psi_in_bar] #[29.0076, 36.2595]
    tire_readings = []

    for tire_pressure in tire_pressures:
        if tire_pressure < range_psi[0]:
            tire_readings.append("Low")
        elif tire_pressure > range_psi[1]:
            tire_readings.append("High")
        else:
            tire_readings.append("Good")

    return tire_readings

print(tire_status([30, 35, 40, 45], [2.0, 2.5]))