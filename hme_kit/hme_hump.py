"""
HME with a competing location force (own exercise, built on the lecture's footloose-capital model).

Region A is the larger market (demand share theta). Capital is mobile; returns to capital are proportional to a
firm's sales (constant markup, zero profit). A location cost shifter kappa (land rents, congestion, wage premium,
weaker institutions) lowers the net return in A by a factor 1/(1+kappa). kappa = 0 is the lecture model.
  sales_A ∝ theta/(phi + (1-phi)λ) + phi(1-theta)/(1 - (1-phi)λ)
  sales_B ∝ phi*theta/(phi + (1-phi)λ) + (1-theta)/(1 - (1-phi)λ)
Equilibrium λ*: net returns equal, with corner solutions λ in {0,1}.
"""
import numpy as np
from scipy.optimize import brentq

def sales(lam, theta, phi):
    DA = phi + (1 - phi) * lam
    DB = 1 - (1 - phi) * lam
    return theta / DA + phi * (1 - theta) / DB, phi * theta / DA + (1 - theta) / DB

def gap(lam, theta, phi, kappa):
    sA, sB = sales(lam, theta, phi)
    return sA / (1 + kappa) - sB          # net return differential, A minus B

def lam_star(theta, phi, kappa):
    eps = 1e-9                              # avoid 0/0 at the corners
    if gap(1 - eps, theta, phi, kappa) >= 0: return 1.0
    if gap(eps, theta, phi, kappa) <= 0: return 0.0
    return brentq(gap, eps, 1 - eps, args=(theta, phi, kappa))

if __name__ == "__main__":
    theta = 0.6
    phis = [0, 0.2, 0.4, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]
    print("lambda* (share of firms in the larger region), theta = 0.6")
    print("phi    " + "".join(f"kappa={k:<6}" for k in (0, 0.01, 0.03, 0.05)))
    for p in phis:
        print(f"{p:<7}" + "".join(f"{lam_star(theta, p, k):<12.3f}" for k in (0, 0.01, 0.03, 0.05)))
    print("\nPull toward the larger market at lambda = theta (gross return differential, kappa = 0):")
    for p in phis:
        print(f"phi={p:<5} differential={gap(theta, theta, p, 0):.4f}   (differential/(1-phi) = {gap(theta, theta, p, 0)/(1-p):.4f})")
