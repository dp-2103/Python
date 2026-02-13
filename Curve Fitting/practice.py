import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import tkinter as tk
from tkinter import ttk, messagebox

# =========================
# Load data from CSV
# =========================
try:
    data = np.loadtxt("BST_5K_1.csv", delimiter=",", skiprows=1)
    B = data[:, 0]
    Y = data[:, 1]
except Exception as e:
    print("Error loading CSV file:", e)
    exit()

# Estimate noise for chi-square
noise_sigma = np.std(Y - np.mean(Y))

# =========================
# Define models
# =========================
def linear_model(B, k):
    return k * np.abs(B)

def parabolic_model(B, a):
    return a * B**2

def linear_parabolic_model(B, k, a):
    return k * np.abs(B) + a * B**2

MODELS = {
    "Linear": (linear_model, [0.1], ["k"]),
    "Parabolic": (parabolic_model, [0.1], ["a"]),
    "Linear + Parabolic": (linear_parabolic_model, [0.1, 0.1], ["k", "a"])
}

# =========================
# Goodness of fit
# =========================
def r_squared(y, yfit):
    ss_res = np.sum((y - yfit)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    return 1 - ss_res/ss_tot

def reduced_chi_square(y, yfit, sigma, n_params):
    chi2 = np.sum(((y - yfit)/sigma)**2)
    dof = len(y) - n_params
    return chi2 / dof

def AIC(y, yfit, n_params):
    rss = np.sum((y - yfit)**2)
    n = len(y)
    return n*np.log(rss/n) + 2*n_params

# =========================
# Fit function
# =========================
def run_fit():
    model_name = model_var.get()
    func, p0, param_names = MODELS[model_name]

    try:
        popt, pcov = curve_fit(func, B, Y, p0=p0)
    except Exception as e:
        messagebox.showerror("Fit Error", str(e))
        return

    Y_fit = func(B, *popt)

    R2 = r_squared(Y, Y_fit)
    chi2_red = reduced_chi_square(Y, Y_fit, noise_sigma, len(popt))
    aic = AIC(Y, Y_fit, len(popt))

    result = f"Model: {model_name}\n\n"
    for name, val in zip(param_names, popt):
        result += f"{name} = {val:.6g}\n"

    result += f"\nR² = {R2:.4f}"
    result += f"\nReduced χ² = {chi2_red:.3f}"
    result += f"\nAIC = {aic:.2f}"

    messagebox.showinfo("Fit Result", result)

    plt.figure()
    plt.scatter(B, Y, label="Data")
    plt.plot(B, Y_fit, 'r', label="Fit")
    plt.xlabel("B")
    plt.ylabel("Y")
    plt.title(model_name)
    plt.legend()
    plt.show()

# =========================
# GUI
# =========================
root = tk.Tk()
root.title("Origin-like Nonlinear Fitting (CSV Data)")

model_var = tk.StringVar(value="Linear")

ttk.Label(root, text="Select Model:").grid(row=0, column=0, padx=10, pady=10)

model_menu = ttk.Combobox(
    root,
    textvariable=model_var,
    values=list(MODELS.keys()),
    state="readonly",
    width=22
)
model_menu.grid(row=0, column=1, padx=10, pady=10)

fit_button = ttk.Button(root, text="Fit", command=run_fit)
fit_button.grid(row=1, column=0, columnspan=2, pady=15)

root.mainloop()
