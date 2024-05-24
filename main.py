import filterpy.stats as stats
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

class KalmanFilter:
    def __init__(self, initial_state, initial_covariance, process_noise, measurement_noise):
        self.x = initial_state
        self.P = initial_covariance
        self.Q = process_noise
        self.R = measurement_noise

    def predict(self):
        self.P = self.P + self.Q  # This is the predictive step, takes initial and adds noise

    def update(self, measurement):
        K = self.P / (self.P + self.R)  # Kalman Gain
        self.x = self.x + K * (measurement - self.x)  # Update estimate
        self.P = (1 - K) * self.P  # Update error covariance

    def get_state(self):
        return self.x


# an example
initial_state = 0.0
initial_covariance = 1.0
process_noise = 1e-5
measurement_noise = 0.1

kf = KalmanFilter(initial_state, initial_covariance, process_noise, measurement_noise)

# Generate some noisy measurements
np.random.seed(50)
true_value = 2.0
measurements = true_value + np.random.normal(0, np.sqrt(measurement_noise), 100)

# Apply the Kalman Filter to the measurements
filtered_estimates = []
for measurement in measurements:
    kf.predict()
    kf.update(measurement)
    filtered_estimates.append(kf.get_state())

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(measurements, label='Noisy Measurements', linestyle='--', marker='o', color='r')
plt.plot(filtered_estimates, label='Kalman Filter Estimate', color='b')
plt.axhline(true_value, color='g', linestyle='-', label='True Value')
plt.title('Kalman Filter Estimate vs Noisy Measurements')
plt.xlabel('Time Step')
plt.ylabel('Value')
plt.legend()
plt.show()
