import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to simulate IoT sensor data
def simulate_sensor_data(samples=1000):
    data = {
        'Temperature': np.random.normal(75, 5, samples),  # Mean 75°C, SD 5
        'Vibration': np.random.normal(0.5, 0.1, samples), # Mean 0.5 Hz, SD 0.1
        'Pressure': np.random.normal(30, 2, samples)      # Mean 30 PSI, SD 2
    }
    return pd.DataFrame(data)

# Generate and save simulated sensor data
print("Generating simulated IoT sensor data...")
sensor_data = simulate_sensor_data(1000)  # Generate 1000 samples
sensor_data.to_csv("simulated_sensor_data.csv", index=False)
print("Sensor data saved to 'simulated_sensor_data.csv'.")

# Visualize the simulated data
print("Displaying simulated sensor data...")
sensor_data.plot(title="Simulated IoT Sensor Data")
plt.xlabel("Sample Index")
plt.ylabel("Sensor Readings")
plt.legend()
plt.show()

