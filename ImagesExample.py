import PIL
from PIL import Image


def main():
    image = Image.open('Flowers.jpg')
    flower = darker(image)
    width = image.width
    height = image.height
    print("width is", width, "height is", height)
    flower.show()


"""This function is going to reduce the brightness of the flower"""


def darker(flower):
    for x in range(flower.width):
        for y in range(flower.height):
            r, g, b = flower.getpixel((x, y))
            # print("Red: {0}, Green: {1}, Blue: {2}".format(r, g, b))
            r = flower.getpixel((x, y))[0] // 2
            g = flower.getpixel((x, y))[1] // 2
            b = flower.getpixel((x, y))[2] // 2
            # create a tuple
            new_color = (r, g, b)
            flower.putpixel((x, y), new_color)
    return flower


if __name__ == "__main__":
    main()
