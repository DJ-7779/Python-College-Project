
import numpy as np

n = int(input("Enter the number of sensor readings: "))

sensor_data = []

for i in range(n):
    value = float(input(f"Enter sensor reading {i + 1}: "))
    sensor_data.append(value)

sensor_data = np.array(sensor_data)

print("\nSensor Data:", sensor_data)
print("Mean:", round(np.mean(sensor_data), 2))
print("Median:", round(np.median(sensor_data), 2))
print("Minimum:", np.min(sensor_data))
print("Maximum:", np.max(sensor_data))
print("Std. Dev.:", round(np.std(sensor_data), 2))

threshold = float(input("\nEnter threshold value: "))

high_values = sensor_data[sensor_data > threshold]

print("Values above", threshold, ":", high_values)
