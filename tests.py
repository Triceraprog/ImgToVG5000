import unittest
from PIL import Image
from block_image import BLOCK_HEIGHT, BLOCK_WIDTH, BlockImage, box_generator


def construct_test_image():
    test_image = Image.new("1", (16, 30))
    test_image.putpixel((0, 0), 1)
    test_image.putpixel((15, 0), 1)
    test_image.putpixel((1, 10), 1)
    test_image.putpixel((14, 10), 1)
    test_image.putpixel((2, 20), 1)
    test_image.putpixel((13, 20), 1)

    return test_image


def construct_redundant_image():
    test_image = Image.new("1", (16, 30))
    test_image.putpixel((0, 0), 1)
    test_image.putpixel((8, 0), 1)
    test_image.putpixel((1, 10), 1)
    test_image.putpixel((9, 10), 1)
    test_image.putpixel((3, 21), 1)
    test_image.putpixel((11, 21), 1)

    return test_image


class TestBlockImage(unittest.TestCase):
    def test_block_image_asks_for_input_image(self):
        input_image = Image.new("1", (16, 30))
        im = BlockImage(input_image)
        self.assertEqual(im.size, (16, 30))
        self.assertEqual(im.block_size, (2, 3))
        self.assertEqual(im.block_count, 6)

    def test_blocks_are_cut_from_input_image(self):
        input_image = construct_test_image()
        im = BlockImage(input_image)

        list_of_ones = [(0, 0), (7, 0), (1, 0), (6, 0), (2, 0), (5, 0)]

        for block_index in range(im.block_count):
            block_to_test = im.blocks[block_index]

            self.assertEqual(block_to_test.size, (BLOCK_WIDTH, BLOCK_HEIGHT), "Block %i" % (block_index, ))
            self.assertEqual(block_to_test.mode, "1", "Block %i" % (block_index,))

            for y in range(BLOCK_HEIGHT):
                for x in range(BLOCK_WIDTH):
                    pixel = block_to_test.getpixel((x, y))
                    if (x, y) == list_of_ones[block_index]:
                        self.assertEqual(pixel, 1, "Coordinates %i (%i, %i)" % (block_index, x, y))
                    else:
                        self.assertEqual(pixel, 0, "Coordinates %i (%i, %i)" % (block_index, x, y))

    def test_reduce_blocks_removes_duplicates(self):
        input_image = construct_redundant_image()
        im = BlockImage(input_image)

        self.assertEqual(im.block_count, 6)
        self.assertEqual(im.get_unique_block_count(), 6)

        im.deduplicate_blocks()

        self.assertEqual(im.blocks[0], im.blocks[1])
        self.assertNotEqual(im.blocks[1], im.blocks[2])
        self.assertEqual(im.blocks[2], im.blocks[3])
        self.assertNotEqual(im.blocks[3], im.blocks[4])
        self.assertEqual(im.blocks[4], im.blocks[5])
        self.assertEqual(im.get_unique_block_count(), 3)


class TestBoxGenerator(unittest.TestCase):
    def test_box_generator(self):
        target = [(0, 0, 8, 10), (8, 0, 16, 10), (0, 10, 8, 20), (8, 10, 16, 20)]
        test = []
        for box in box_generator(16, 20, 8, 10):
            test.append(box)

        self.assertEqual(target, test)

