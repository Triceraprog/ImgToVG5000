import unittest

from PIL import Image

from tools import BLOCK_WIDTH, BLOCK_HEIGHT, ParameterException
from block_list import BlockList, ParameterException


class TestBlockListToImage(unittest.TestCase):
    def test_block_list_gets_an_image_list(self):
        block1 = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))
        block2 = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))
        block2.putpixel((0, 0), 1)

        bl = BlockList([block1, block2])
        self.assertEqual(len(bl), 2)

    def test_every_image_must_be_the_same_size(self):
        block1 = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))
        block2 = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT + 1))

        with self.assertRaises(ParameterException):
            BlockList([block1, block2])

    def test_maximum_size_must_be_big_enough(self):
        block = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))

        bl = BlockList([block])
        with self.assertRaises(ParameterException):
            bl.get_image(BLOCK_WIDTH - 1)

    def test_block_list_can_give_an_image_horizontal(self):
        block1 = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))
        block2 = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))
        block2.putpixel((0, 0), 1)

        bl = BlockList([block1, block2])
        im = bl.get_image(BLOCK_WIDTH * 2)
        self.assertEqual(im.size, (BLOCK_WIDTH * 2, BLOCK_HEIGHT))
        self.assertEqual(im.getpixel((8, 0)), 1)
        self.assertEqual(im.getpixel((0, 0)), 0)

    def test_block_list_is_iterable(self):
        block1 = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))
        block2 = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))
        block2.putpixel((0, 0), 1)

        bl = BlockList([block1, block2])

        count = 0
        for block in bl:
            count += 1
        self.assertEqual(2, count)
