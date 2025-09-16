import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
from skimage import data

def find_corners(gimage):
    '''
    Находит углы в gimage
    :param gimage:
    :return:
    '''
    corners = cv2.goodFeaturesToTrack(gimage, maxCorners=25, qualityLevel=0.01, minDistance=10)
    return corners

def main():
    gimage = data.coins() #Загружаем изображение
    corners = find_corners(gimage)
    plt.plot()
    ax = plt.gca()
    ax.imshow(gimage)
    # Добавляем круги вокруг найденных углов
    for corner in corners:
        x,y = map(int, corner[0])
        ax.add_patch(patches.Circle((x, y), 10, linewidth=2, edgecolor="red", fill=None))

    # Визуализация
    plt.show()

if __name__=='__main__':
    main()