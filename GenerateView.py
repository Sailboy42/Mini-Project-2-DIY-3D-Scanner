##Pre-Process data
import PreProcessing as PreProc

## importing visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

ax = plt.axes(projection="3d")
ax.scatter3D(PreProc.df("xs"), PreProc.df("ys"), PreProc.df("zs"), c=PreProc.df("zs"), cmap="Greens")
