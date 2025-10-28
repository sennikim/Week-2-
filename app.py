
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random, math

st.title("Generative Poster Project")
st.write("This is Kim Seyeon's Week 2 generative art project.")

plt.figure(figsize=(6,8))
plt.axis('off')
plt.gca().set_facecolor((0.98,0.97,0.95))
def blob(n_points=100):
    angles=np.linspace(0,2*np.pi,n_points)
    radii=1+np.random.uniform(-0.2,0.2,n_points)
    x=radii*np.cos(angles); y=radii*np.sin(angles)
    plt.fill(x,y,color=(0.8,0.6,0.9),alpha=0.5)
blob()

st.pyplot(plt.gcf())
