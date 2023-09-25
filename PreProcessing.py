import math
import pandas as pd
import numpy as np

## read spherical scan data from file (data can also be read in real-time over a serial connection)
df = pd.read_csv(
    "serial_output_Z_scan_2D.txt",
    header=0,
    names=["ir_read", "orig_tilt_deg", "orig_pan_deg"],
)

"""***************************************************************************************
*    Title: 3D Scanner 3D data projection and visualization
*    Author: Gati Aher
*    Date: Sep 28, 2021
*    Code version: 1
*    Availability: https://gatiaher.github.io/projects/building-a-pan-tilt-3d-scanner/#cad-design-of-pan-tilt-mount
*
***************************************************************************************"""

## delete last row with end signal 0,0,0
df = df[:-1]


## convert sensor measurement (x) to distance (d)
## y = Cx^-1 (Power Law)
df["distance"] = df.apply(lambda row: 10964 * (1 / row["ir_read"]), axis=1)

## account for servo motor offsets
TILT_DEG_OFFSET = 20
PAN_DEG_OFFSET = -60
df["tilt_deg"] = df.apply(lambda row: row["orig_tilt_deg"] + TILT_DEG_OFFSET, axis=1)
df["pan_deg"] = df.apply(lambda row: row["orig_pan_deg"] + PAN_DEG_OFFSET, axis=1)

## convert from degrees to radians
df["tilt_rad"] = df.apply(lambda row: math.radians(row["tilt_deg"]), axis=1)
df["pan_rad"] = df.apply(lambda row: math.radians(row["pan_deg"]), axis=1)

## convert spherical coordinates to Cartesian coordinates
df["xs"] = df.apply(
    lambda row: row["distance"] * math.sin(row["tilt_rad"]) * math.sin(row["pan_rad"]),
    axis=1,
)
df["ys"] = df.apply(
    lambda row: row["distance"] * math.sin(row["tilt_rad"]) * math.cos(row["pan_rad"]),
    axis=1,
)
df["zs"] = df.apply(lambda row: row["distance"] * math.cos(row["tilt_rad"]), axis=1)

## flip axis (because original read was from right-to-left)
df["xs"] = df.apply(lambda row: row["xs"] * -1, axis=1)


##Isolate object scan data from forfront and backdrop data
subject_data = df.loc[
    (df["distance"] >= 30) & (df["distance"] <= 35), df["xs"] & df["zs"]
]
