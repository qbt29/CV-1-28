import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
from skimage import data

gimage = data.coins()
corners = cv2.goodFeaturesToTrack(gimage, maxCorners=25, qualityLevel=0.01, minDistance=10)

plt.plot()
ax = plt.gca()
ax.imshow(gimage)

for corner in corners:
    x,y = map(int, corner[0])
    ax.add_patch(patches.Circle((x, y), 10, linewidth=2, edgecolor="red", fill=None))

plt.show()

