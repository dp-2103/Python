# Simple Linear fitting example

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Read data files from csv or txt
data = np.loadtxt("data1.csv", delimiter=",", skiprows=1)
X = data[:, 0]
Y = data[:, 1]

#Define linear model for fitting
def linear_model(x, m, b):
    return m*x + b

# Perform curve fitting
popt, pcov = curve_fit(linear_model, X, Y)
m, b = popt                                           # Extract fitted parameters
print(f"Model: Linear\n Fitted parameters:\n m = {m}\n b = {b}")

# Generate fitted data
X_fit = np.linspace(np.min(X), np.max(X), 200)
Y_fit = linear_model(X_fit, m, b)
#Plot orignal data and fitted curve
plt.scatter(X, Y, label='Data', color='blue')
plt.plot(X_fit, Y_fit, label='Fit', color="red")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()




"""
Step1: Import necessary libraries
Step2: load data from CSV file
Step3: Define model for fitting
Step4: Perform curve fitting using curve_fit module
Step5: Extract fitted parameters
Step6: Generate Fitted data for plotting
Step7: Plot orignal data as well as fitted data
"""