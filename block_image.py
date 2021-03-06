from block_list import BlockList
from tools import box_generator, BLOCK_WIDTH, BLOCK_HEIGHT
from unique_block_set import UniqueBlockSet


class BlockImage:
    def __init__(self, input_image):
        self.size = input_image.size

        width, height = self.size

        self.block_size = (width / BLOCK_WIDTH, height / BLOCK_HEIGHT)
        self.block_count = int(self.block_size[0] * self.block_size[1])
        self.unique_block_count = self.block_count

        self.blocks = []

        for box in box_generator(width, height, BLOCK_WIDTH, BLOCK_HEIGHT):
            block = input_image.crop(box)
            self.blocks.append(block)

    def deduplicate_blocks(self):
        block_set = UniqueBlockSet()
        for block in self.blocks:
            block_set.add(block)

        new_blocks = [block_set.get(block) for block in self.blocks]

        self.blocks = new_blocks
        self.unique_block_count = len(block_set)

    def get_unique_block_count(self):
        return self.unique_block_count

    def save(self, filename):
        output_image = self.get_image()
        output_image.save(filename)

    def get_image(self):
        bl = BlockList(self.blocks)
        im = bl.get_image(self.size[0])

        return im

    def get_block_palette(self):
        block_set = UniqueBlockSet()
        for block in self.blocks:
            block_set.add(block)

        return BlockList(block_set.blocks)
