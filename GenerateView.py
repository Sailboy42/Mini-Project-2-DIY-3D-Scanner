## importing visualization libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

##Pre-Process data
import PreProcessing as PreProc

##3D Plot
scan_data = plt.axes(projection="3d")
scan_data.scatter3D(
    PreProc.df("xs"),
    PreProc.df("ys"),
    PreProc.df("zs"),
    c=PreProc.df("zs"),
    cmap="Greens",
)
##2D Plot/Subject Visuzlization
PreProc.subject_data.plot(kind="scatter")
plt.show()
