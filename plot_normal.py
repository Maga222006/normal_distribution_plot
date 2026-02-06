# plot_normal.py
"""
Generate and save a plot of the standard normal distribution.

Usage:
    python plot_normal.py

The script creates a PNG file named 'normal_distribution.png' in the same directory.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def main():
    # Parameters for the standard normal distribution
    mu = 0.0
    sigma = 1.0

    # X values: cover a range that captures most of the distribution
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
    # Probability density function values
    y = norm.pdf(x, loc=mu, scale=sigma)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"$\mu={mu}, \sigma={sigma}$", color="steelblue")
    plt.title("Standard Normal Distribution")
    plt.xlabel("x")
    plt.ylabel("Probability Density")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    # Save the figure
    output_path = "normal_distribution.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to {output_path}")

if __name__ == "__main__":
    main()
