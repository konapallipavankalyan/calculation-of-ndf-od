import streamlit as st

def npp(l, p, pf):
    """
    Calculate the number of photons per pulse.
    Parameters:
        l (float): Wavelength in meters.
        p (float): Power in watts.
        pf (float): Pulsing frequency in Hz.
    Returns:
        float: Number of photons per pulse.
    """
    h = 6.626 * 1e-34  # Planck's constant in J·s
    c = 3 * 10**8      # Speed of light in m/s
    e_p = p / pf       # Energy per pulse
    E = (h * c) / l    # Energy of a single photon
    n = e_p / E        # Number of photons per pulse
    return n

def main():
    st.title("Photon Calculation and Neutral Density Filter Order")

    # User input for wavelength, power, and pulsing frequency
    wavelength = st.number_input("Enter the wavelength (nm):", min_value=200.0, max_value=2000.0, value=808.0) * 1e-9
    power = st.number_input("Enter the power (mW):", min_value=0.1, max_value=1000.0, value=1.0) * 1e-3
    pulse_frequency = st.number_input("Enter the pulsing frequency (Hz):", min_value=1.0, max_value=1e6, value=1e5)

    # Neutral density filter order (transmission probability)
    d = st.number_input("Enter the neutral density filter order (d):", min_value=0.0, max_value=20.0, value=10.9)
    t_p = 10**(-d)  # Transmission probability

    # Calculate photons per pulse and output photons
    photons_per_pulse = npp(wavelength, power, pulse_frequency)
    output_photons = t_p * photons_per_pulse

    # Display results
    st.subheader("Results")
    st.write(f"Photon energy: {((6.626 * 1e-34) * (3 * 10**8)) / wavelength:.2e} J")
    st.write(f"Number of photons per pulse: {photons_per_pulse:.2e}")
    st.write(f"Output photons after transmission: {output_photons:.2e}")

if __name__ == "__main__":
    main()
