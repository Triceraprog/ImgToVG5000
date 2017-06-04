from PIL import ImageChops


def box_generator(width, height, box_w, box_h):
    for y in range(int(height / box_h)):
        for x in range(int(width / box_w)):
            coord_x = x * box_w
            coord_y = y * box_h
            yield (coord_x, coord_y, coord_x + box_w, coord_y + box_h)


def are_images_equal(first_image, second_image):
    if first_image.mode != second_image.mode:
        return False

    if first_image.size != second_image.size:
        return False

    return ImageChops.difference(first_image, second_image).getbbox() is None


BLOCK_WIDTH = 8
BLOCK_HEIGHT = 10


class ParameterException(Exception):
    pass
