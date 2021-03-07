from math import sqrt, sin, cos, pi

import matplotlib.pyplot as plt
import json


def show_img(data):
    plt.imshow(data)
    plt.show()


def open_image_json(path):
    with open(path, 'r') as file:
        return json.load(file)


def calculate_p(hough_space, x, y):
    # x*cos(theta) + y*sin(theta) = p
    d = len(hough_space) >> 1
    radian = pi / 180
    for degree in range(0, 181):
        angle = radian * degree
        p = int(x * cos(angle) + y * sin(angle)) + d
        hough_space[degree][p] += 1


def hough_transform(data):
    d = int(sqrt(len(data) * len(data) + len(data[0]) + len(data[0])))
    hough_space = [[0 for j in range(-d, d + 1)] for i in range(0, 181)]

    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x]:
                calculate_p(hough_space, x, y)
    return hough_space


show_img(open_image_json("image_hough.json"))
image = hough_transform(open_image_json("image_hough.json"))
show_img(image)