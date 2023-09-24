## importing visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Scatter plot with day against tip
plt.scatter(data["day"], data["tip"])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel("Day")
plt.ylabel("Tip")

plt.show()
