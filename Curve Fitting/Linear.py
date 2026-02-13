import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import tkinter as tk
from tkinter import ttk, messagebox

try:
    data = np.loadtxt("BST_5K_1.csv", delimiter=',', skiprows=1)
    X = data[:,0]
    Y = data[:,1]
except:
    print("Error loading CSV file.")
    exit()

def linear_model(x, m, b):
    return m * x + b

def run_fit():
    try:
        popt, pcov = curve_fit(linear_model, X, Y)
        m, b = popt
        Y_fit = linear_model(X, m, b)

        plt.scatter(X, Y, label='Data', color='blue')
        plt.plot(X, Y_fit, label='Fit: y = {:.2f}x + {:.2f}'.format(m, b), color='red')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Fitting failed: {e}")