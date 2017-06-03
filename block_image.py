BLOCK_WIDTH = 8
BLOCK_HEIGHT = 10


def box_generator(width, height, box_w, box_h):
    for y in range(int(height/box_h)):
        for x in range(int(width/box_w)):
            coord_x = x * box_w
            coord_y = y * box_h
            yield (coord_x, coord_y , coord_x + box_w, coord_y + box_h)


class BlockImage:
    def __init__(self, input_image):
        self.size = input_image.size

        width, height = self.size

        self.block_size = (width / BLOCK_WIDTH, height / BLOCK_HEIGHT)
        self.block_count = int(self.block_size[0] * self.block_size[1])
        self.blocks = []

        for box in box_generator(width, height, BLOCK_WIDTH, BLOCK_HEIGHT):
            block = input_image.crop(box)
            self.blocks.append(block)
