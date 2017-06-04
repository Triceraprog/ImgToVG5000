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


def chunks(sequence, chunk_size):
    for index in range(0, len(sequence), chunk_size):
        yield sequence[index:index + chunk_size]


def fix_size_to_block_multiple(size):
    new_width = BLOCK_WIDTH * int((size[0] + BLOCK_WIDTH - 1) / BLOCK_WIDTH)
    new_height = BLOCK_HEIGHT * int((size[1] + BLOCK_HEIGHT - 1) / BLOCK_HEIGHT)
    new_size = new_width, new_height
    return new_size
