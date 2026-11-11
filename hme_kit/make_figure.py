"""Produces figures/hme_hump.png from hme_hump.py. Run: python make_figure.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from hme_hump import lam_star, gap

theta = 0.6
phis = np.linspace(0, 0.995, 400)
fig, ax = plt.subplots(1, 2, figsize=(11, 4.2), dpi=200)

for k, c in zip((0, 0.01, 0.03, 0.05), ("#222222", "#1f77b4", "#d95f02", "#7570b3")):
    ax[0].plot(phis, [lam_star(theta, p, k) for p in phis], label=f"κ = {k}", color=c, lw=2)
ax[0].axhline(theta, ls=":", color="grey", lw=1)
ax[0].text(0.01, theta - 0.07, "θ = 0.6 (large region's demand share)", color="grey", fontsize=8)
ax[0].set_xlabel("Freeness of trade φ  (0 = prohibitive, 1 = free)")
ax[0].set_ylabel("Share of firms in the larger region, λ*")
ax[0].set_title("(a) Where firms end up: a hump once κ > 0")
ax[0].set_ylim(-0.03, 1.05); ax[0].legend(frameon=False)

pull = [gap(theta, theta, p, 0) for p in phis]
ax[1].plot(phis, pull, color="#222222", lw=2)
ax[1].set_xlabel("Freeness of trade φ")
ax[1].set_ylabel("Return advantage of the large market at λ = θ")
ax[1].set_title("(b) How strong the pull is: it fades as trade becomes free")

for a in ax:
    a.spines[["top", "right"]].set_visible(False)
fig.text(0.01, 0.005, "Footloose-capital model, θ = 0.6. κ = proportional location cost in the larger region. Own simulation.", fontsize=7, color="grey")
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig("figures/hme_hump.png")
print("saved")
