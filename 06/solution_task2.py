import numpy as np

time = 40709879
distance = 215105121471005

xs = np.arange(0, time)
ys = xs * (time - xs)

filtered = ys[ys > distance]

print(len(filtered))