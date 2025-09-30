import cv2
import numpy as np
import argparse, os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageDraw
from skimage import data

def read_data(path:str):
    if type(path) != str:
        print("Wrong type of path")
        exit(1)
    '''
    Чтение данных из фото
    :param path: str - путь к файлу
    :return: 
        (np.ndarrray, np.ndarray)
    '''
    if os.path.exists(path=path):
        image = cv2.imread(path)
    else:
        print("Incorrect path to file")
        exit(1)
    print(type(image))
    try:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image, gray_image
    except:
        print("Incorrect data")
        exit(1)

def find_corners(gray_image, maxCorners=100, qualityLevel=0.08, minDistance=10, HarrisDetector=False) -> np.ndarray:
    if not(type(gray_image) == np.ndarray and type(maxCorners) == int and type(qualityLevel) in [int, float] and 0<=qualityLevel<=1 and type(minDistance) in [int, float] and type(HarrisDetector) is bool):
        print("Wrong input data in find_corners, abort")
        exit(1)
    '''
    Находит углы в gray_image
    :params:
        gray_image - картинка (в сером формате) для поиска
        maxCorners - максимальное кол-во углов
        qualityLevel - [0..1] минимальное качество угла
        minDistance - минимальное Евклидово расстояние между углами
        HarrisDetector - испольовать ли детектор Гарриса (если False, то используется детектор Shi-Tomasi)
    :return:
        np.ndarray - массив коориднат найденных углов вида (x, y)
    '''
    corners = cv2.goodFeaturesToTrack(gray_image, maxCorners=maxCorners, qualityLevel=qualityLevel, minDistance=minDistance, useHarrisDetector=HarrisDetector)
    print(type(corners), 'corners')
    return corners

def display_data(file:np.ndarray, corners:np.ndarray, mode:str='m', path_to_save=None) -> None:
    '''
    Выводит данные в нужном формате
    :params:
        file:np.ndarray - исходный файл
        corners:np.ndarray - координаты найденных углов
        mode:str - в каком формате выводить (если m - то через matplotlin, f - в файл, указанный в path_to_save, картинкой)
    '''
    if not(type(file) == np.ndarray and type(corners) == np.ndarray and type(mode) == str and (path_to_save is None or type(path_to_save) == str)):
        print("Wrong input data in display_data, abort")
        exit(1)
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
    elif mode == 'f': # into file
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

def main(flags:dict) -> None:

    if flags.path is None:
        gray_image = data.coins()  # Загружаем изображение
        image = gray_image
    else:
        image, gray_image = read_data(flags.path)
    corners = find_corners(gray_image)
    if flags.file is None:
        display_data(image, corners, 'm')
    else:
        display_data(image, corners, 'f', flags.file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-path',type=str)
    parser.add_argument('-file')
    args=parser.parse_args()
    main(args)
