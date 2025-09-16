import cv2
import argparse
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw
from skimage import data


def read_data(path):
    '''
    Чтение данных из фото
    :param path:
    :return:
    '''
    try:
        image = cv2.imread(path)
        gimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image, gimage
    except:
        raise Exception("Incorrect path to file")

def find_corners(gimage):
    '''
    Находит углы в gimage
    :param gimage:
    :return:
    '''
    corners = cv2.goodFeaturesToTrack(gimage, maxCorners=1000, qualityLevel=0.08, minDistance=10, useHarrisDetector=False)
    return corners

def display_data(file, corners, mode='m', path_to_save=None):
    if mode == 'm': # in graph
        plt.plot()
        ax = plt.gca()
        ax.imshow(file)
        # Добавляем круги вокруг найденных углов
        for corner in corners:
            x, y = map(int, corner[0])
            ax.add_patch(patches.Circle((x, y), 10, linewidth=2, edgecolor="red", fill=None))

        # Визуализация
        plt.show()
    elif mode == 'f': # in file
        cv2.imwrite(path_to_save, file)
        im = Image.open(path_to_save)
        draw = ImageDraw.Draw(im)
        # Добавляем круги вокруг найденных углов
        for corner in corners:
            x, y = map(int, corner[0])
            draw.ellipse((x - 10, y - 10, x + 10, y + 10), outline="red")
        # Сохраняем изображение
        im.save(path_to_save, quality=120)
        im.close()

def main(flags:list) -> None:
    if flags.p is None:
        gimage = data.coins()  # Загружаем изображение
        image = gimage
    else:
        image, gimage = read_data(flags.p)
    corners = find_corners(gimage)
    if flags.f is None:
        display_data(image, corners, 'm')
    else:
        display_data(image, corners, 'f', flags.f)





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',type=str)
    parser.add_argument('-f')
    args=parser.parse_args()
    main(args)
