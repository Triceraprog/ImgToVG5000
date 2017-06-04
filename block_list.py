from PIL import Image

from tools import box_generator, BLOCK_WIDTH, BLOCK_HEIGHT, ParameterException


class BlockList:
    def __init__(self, block_list):
        sizes = {block.size for block in block_list}
        if len(sizes) != 1:
            raise ParameterException("All blocks must have the same size")

        self.block_list = block_list

    def __len__(self):
        return len(self.block_list)

    def __iter__(self):
        for block in self.block_list:
            yield block

    def __get_block_geometry(self, max_width):
        block_width, _ = self.block_list[0].size

        block_count = len(self.block_list)
        count_by_line = int(max_width / block_width)

        if count_by_line == 0:
            raise ParameterException("Maximum width is too small")

        entire_line_count = int(block_count / count_by_line)
        last_line_count = block_count - (entire_line_count * count_by_line)

        line_count = entire_line_count if last_line_count == 0 else entire_line_count + 1

        return count_by_line, line_count

    def get_image(self, max_width):
        block_width, block_height = self.block_list[0].size

        columns, lines = self.__get_block_geometry(max_width)
        image_width = columns * block_width
        image_height = lines * block_height

        im = Image.new("1", (image_width, image_height))

        paste_list = zip(box_generator(image_width, image_height, BLOCK_WIDTH, BLOCK_HEIGHT),
                         self.block_list)

        for box, block in paste_list:
            im.paste(block, box)

        return im
