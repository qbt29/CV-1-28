import cv2
import argparse
from PIL import Image, ImageDraw

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
def main(path):
    image, gimage = read_data(path)
    corners = find_corners(gimage)

    cv2.imwrite('found.jpg', image)
    im = Image.open('found.jpg')
    draw = ImageDraw.Draw(im)
    # Добавляем круги вокруг найденных углов
    for corner in corners:
        x,y = map(int, corner[0])
        draw.ellipse((x-10,y-10, x+10, y+10), outline="red")
    # Сохраняем изображение в found.jpg
    im.save("found.jpg", quality=120)
    im.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path',type=str)
    args=parser.parse_args()
    path = args.path
    main(path)






