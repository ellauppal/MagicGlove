import cv2
import numpy as np
from camera_detect import *

def colour_detect_on_image(path):

    print("Colour Recognition Python")

    # get image input
    img = cv2.imread(path)
    new_img = cv2.resize(img, (50, 50))
    height, width, _ = new_img.shape
    hsv_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV) # convert image from rgb to hsv

    array_store = []

    colour_dict = {'BLACK': [[180, 255, 30], [0, 0, 0]],
                'WHITE': [[180, 18, 255], [0, 0, 231]],
                'RED': [[180, 255, 255], [159, 50, 70]],
                'RED': [[9, 255, 255], [0, 50, 70]],
                'GREEN': [[89, 255, 255], [36, 50, 70]],
                'BLUE': [[128, 255, 255], [90, 50, 70]],
                'YELLOW': [[35, 255, 255], [25, 50, 70]],
                'PURPLE': [[158, 255, 255], [129, 50, 70]],
                'ORANGE': [[24, 255, 255], [10, 50, 70]],
                'GRAY': [[180, 18, 230], [0, 0, 40]]}

    for x in range(width):
        for y in range (height):
            hue = hsv_img[x,y][0]
            sat = hsv_img[x,y][1]
            value = hsv_img [x,y][2]

            for colour in colour_dict:
                if ((colour_dict[colour][1][0] < hue < colour_dict[colour][0][0]) and (colour_dict[colour][1][1] < sat < colour_dict[colour][0][1]) and (colour_dict[colour][1][2] < value < colour_dict[colour][0][2])):
                    array_store.append(colour)
                    break

    count_colour_freq_dict = {}

    for i in array_store:
        if i in count_colour_freq_dict:
            count_colour_freq_dict[i] += 1
        else:
            count_colour_freq_dict[i] = 1

    final_colour = max(count_colour_freq_dict, key=count_colour_freq_dict.get)
    print("Maximum value: ", final_colour)

    return final_colour


if __name__ == "__main__":
    colour_detect_on_image("/home/magicglove/MagicGlove/test/image.jpg")
