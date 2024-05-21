import filterpy.stats as stats
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt


stats.plot_gaussian_pdf(mean=10., variance=1.,
                        xlim=(4, 16), ylim=(0, .5))

xs = range(500)
ys = randn(500)*1. + 10.
plt.plot(xs, ys)
print(f'Mean of readings is {np.mean(ys):.3f}')