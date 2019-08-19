import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.ndimage.filters import gaussian_filter

# plt.figure(figsize=(10,25))

# axes = plt.gca()
# axes.set_xlim([0,608])
# axes.set_ylim([0,608])

fig = plt.figure(frameon=False)
# fig.set_size_inches(8,8)

ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)

def myplot(x, y, s, bins=1000):
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins,range=[[0, 608], [0, 608]])
    heatmap = gaussian_filter(heatmap, sigma=s)

    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    return heatmap.T, extent


a = np.load("points.npz")["data"]


x = a[:,0]
y = a[:,1]


img, extent = myplot(x, y, 64)

ax.imshow(img, extent=extent, cmap=cm.jet, aspect='auto')

fig.savefig("out.png", dpi=80)

# plt.imshow(img, extent=extent, origin='lower', cmap=cm.jet)
# plt.savefig('out.png', bbox_inches='tight', pad_inches=0)


# plt.show()

# fig, axs = plt.subplots(2, 2)


# sigmas = [0, 16, 32, 64]

# for ax, s in zip(axs.flatten(), sigmas):
#     if s == 0:
#         ax.plot(x, y, 'k.', markersize=5)
#         ax.set_title("Scatter plot")
#     else:
#         img, extent = myplot(x, y, s)
#         ax.imshow(img, extent=extent, origin='lower', cmap=cm.jet)
#         ax.set_title("Smoothing with  $\sigma$ = %d" % s)

# plt.show()