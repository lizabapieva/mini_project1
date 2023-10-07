from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 20

fig = plt.figure()
ax = plt.axes(xlim=(0, 30), ylim=(15, 45))
max_points = 30
line, = ax.plot(np.arange(max_points), np.ones(max_points, dtype=np.float)*np.nan, lw=1, c='blue', marker='d', ms=2)