import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

st.title("🎨 Week 2 - Generative Poster Project")
st.write("Kim Seyeon | Arts & Advanced Big Data")

# Blob function
def blob(n_points=200, radius=1.0, wobble=0.3):
    angles = np.linspace(0, 2*np.pi, n_points)
    radii = radius + np.random.uniform(-wobble, wobble, size=n_points)
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    return x, y

# Random pastel color
def random_pastel():
    base = np.array([random.random() for _ in range(3)])
    return tuple(0.7 + 0.3 * base)

# Poster
plt.figure(figsize=(6, 8))
plt.axis("off")
plt.gca().set_facecolor((0.98, 0.97, 0.95))

palette = [random_pastel() for _ in range(8)]
for i in range(8):
    wobble = random.uniform(0.1, 0.4)
    radius = 1.2 - i * 0.1
    x, y = blob(radius=radius, wobble=wobble)
    plt.fill(x, y, color=palette[i % len(palette)], alpha=0.4 + i * 0.05)

plt.text(-1.2, 1.3, "Generative Poster", fontsize=16, weight='bold')
st.pyplot(plt.gcf())
