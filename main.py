import streamlit as st
import matplotlib.pyplot as plt

# Set the title of the Streamlit app
st.title("Charging Station with Two Batteries")

# Description
st.write(
    """
    This visualization represents a charging station connected to two batteries:
    - One battery is at **100%** state of charge.
    - The other battery is at **80%** state of charge.
    """
)

# Create the diagram using matplotlib
fig, ax = plt.subplots(figsize=(6, 4))

# Draw the charging station (rectangle)
charging_station = plt.Rectangle((0.4, 0.4), 0.2, 0.3, color="purple", alpha=0.7)
ax.add_patch(charging_station)
ax.text(0.5, 0.55, "Charging\nStation", ha="center", va="center", color="white", fontsize=10)

# Draw lines to the batteries
ax.plot([0.5, 0.3], [0.4, 0.2], color="black", linewidth=2)  # To Battery 1
ax.plot([0.5, 0.7], [0.4, 0.2], color="black", linewidth=2)  # To Battery 2

# Draw Battery 1 (100%)
battery1 = plt.Rectangle((0.25, 0.1), 0.1, 0.1, color="blue", alpha=0.8)
ax.add_patch(battery1)
ax.text(0.3, 0.17, "100%", ha="center", va="center", color="white", fontsize=10)

# Draw Battery 2 (80%)
battery2 = plt.Rectangle((0.65, 0.1), 0.1, 0.1, color="green", alpha=0.8)
ax.add_patch(battery2)
ax.text(0.7, 0.17, "80%", ha="center", va="center", color="white", fontsize=10)

# Set limits and turn off axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Display the diagram
st.pyplot(fig)

# Run the Streamlit app using:
# streamlit run app.py
