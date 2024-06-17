import numpy as np
import scipy.ndimage as ndimage

grid = np.zeros((100, 100), dtype=bool)

for row, line in enumerate(open('trial')):
    grid[row][[i for i, x in enumerate(line) if x == '#']] = 1

for i in range(100):
    grid = ndimage.generic_filter(grid, lambda x: sum(x) - 1 in [2, 3] if x[4] else sum(x) == 3,
                                  size=(3, 3), mode='constant')

print (grid.sum())
