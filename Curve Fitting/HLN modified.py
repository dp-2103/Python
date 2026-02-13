import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import digamma
import tkinter as tk
from tkinter import ttk, messagebox

# =========================
# Physical constants
# =========================
e = 1.602e-19
hbar = 1.055e-34

# =========================
# Load data
# =========================
try:
    data = np.loadtxt("BST_2K.csv", delimiter=",", skiprows=1)
    B = data[:, 0]
    Y = data[:, 1]
except Exception as e:
    print("Error loading CSV file:", e)
    exit()

noise_sigma = np.std(Y - np.mean(Y))

# =========================
# Models
# =========================
def linear_model(B, k):
    return k * np.abs(B)

def parabolic_model(B, a):
    return a * B**2

def linear_parabolic_model(B, k, a):
    return k * np.abs(B) + a * B**2

def HLN_model_norm(B, A, lphi):
    B = np.abs(B) + 1e-12   # avoid division by zero
    Bphi = hbar / (4 * e * lphi**2)
    return -A * (
        digamma(0.5 + Bphi / B) - np.log(Bphi / B)
    )


def mHLN_linear_quad_norm(B, A, lphi, k, a):
    B = np.abs(B)
    Bphi = hbar / (4 * e * lphi**2)
    hln = -A * (
        digamma(0.5 + Bphi / B) - np.log(Bphi / B)
    )
    return hln + k * B + a * B**2

# =========================
# Model registry
# =========================
MODELS = {
    "Linear": (linear_model, [0.1], ["k"]),
    "Parabolic": (parabolic_model, [0.1], ["a"]),
    "Linear + Parabolic": (linear_parabolic_model, [0.1, 0.1], ["k", "a"]),
    "HLN (normalized ΔG)": (HLN_model_norm, [-0.5, 60e-9], ["A", "lphi"]),
    "Modified HLN + Lin + Quad": (
        mHLN_linear_quad_norm,
        [-0.5, 60e-9, 0.0, 0.0],
        ["A", "lphi", "k", "a"]
    )
}

# =========================
# Fit quality metrics
# =========================
def r_squared(y, yfit):
    ss_res = np.sum((y - yfit)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    return 1 - ss_res / ss_tot

def reduced_chi_square(y, yfit, sigma, n_params):
    chi2 = np.sum(((y - yfit) / sigma)**2)
    dof = len(y) - n_params
    return chi2 / dof

def AIC(y, yfit, n_params):
    rss = np.sum((y - yfit)**2)
    n = len(y)
    return n * np.log(rss / n) + 2 * n_params

# =========================
# Fit function
# =========================
def run_fit():
    model_name = model_var.get()
    func, p0, param_names = MODELS[model_name]

    lower_bounds = []
    upper_bounds = []

    for name in param_names:

        if name == "A":
            lower_bounds.append(-0.5)
            upper_bounds.append(0.5)

        elif name == "lphi":
            lower_bounds.append(10e-9)      # 10 nm
            upper_bounds.append(200e-9)     # 200 nm

        elif name == "ls":
            lower_bounds.append(1e-9)       # positive only
            upper_bounds.append(500e-9)

        else:
            lower_bounds.append(-np.inf)
            upper_bounds.append(np.inf)

    try:
        popt, pcov = curve_fit(
            func,
            B,
            Y,
            p0=p0,
            bounds=(lower_bounds, upper_bounds),
            maxfev=50000
        )
    except Exception as e:
        messagebox.showerror("Fit Error", str(e))
        return

    Y_fit = func(B, *popt)

    R2 = r_squared(Y, Y_fit)
    chi2_red = reduced_chi_square(Y, Y_fit, noise_sigma, len(popt))
    aic = AIC(Y, Y_fit, len(popt))

    result = f"Model: {model_name}\n\n"

    for name, val in zip(param_names, popt):
        if name == "lphi":
            result += f"lφ = {val*1e9:.2f} nm\n"
        elif name == "ls":
            result += f"lₛ = {val*1e9:.2f} nm\n"
        elif name == "A":
            result += f"A = {val:.6g} (effective prefactor)\n"
        else:
            result += f"{name} = {val:.6g}\n"

    result += f"\nR² = {R2:.4f}"
    result += f"\nReduced χ² = {chi2_red:.3f}"
    result += f"\nAIC = {aic:.2f}"

    messagebox.showinfo("Fit Result", result)

    print("========== FIT RESULT ==========")
    print(result)
    print("================================")

    plt.figure()
    plt.scatter(B, Y, s=15, label="Data")
    plt.plot(B, Y_fit, 'r', label="Fit")
    plt.xlabel("B (T)")
    plt.ylabel("ΔG (normalized)")
    plt.title(model_name)
    plt.legend()
    plt.show()

# =========================
# GUI
# =========================
root = tk.Tk()
root.title("HLN Fitting (Constrained & Stable)")

model_var = tk.StringVar(value="HLN (normalized ΔG)")

ttk.Label(root, text="Select Model:").grid(row=0, column=0, padx=10, pady=10)

ttk.Combobox(
    root,
    textvariable=model_var,
    values=list(MODELS.keys()),
    state="readonly",
    width=30
).grid(row=0, column=1, padx=10, pady=10)

ttk.Button(root, text="Fit", command=run_fit)\
    .grid(row=1, column=0, columnspan=2, pady=15)

root.mainloop()