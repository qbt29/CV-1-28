import cv2
import argparse
from PIL import Image, ImageDraw

def read_data(path):
    image = cv2.imread('test_photo_1.jpg')
    gimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image, gimage

def main(path):
    image, gimage = read_data(path)
    corners = cv2.goodFeaturesToTrack(gimage, maxCorners=1000, qualityLevel=0.08, minDistance=10, useHarrisDetector=False)

    cv2.imwrite('found.jpg', image)
    im = Image.open('found.jpg')
    draw = ImageDraw.Draw(im)
    for corner in corners:
        x,y = map(int, corner[0])
        draw.ellipse((x-10,y-10, x+10, y+10), outline="red")
    im.save("found.jpg", quality=120)
    im.close()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path',type=str)
    args=parser.parse_args()
    path = args.path
    main(path)






