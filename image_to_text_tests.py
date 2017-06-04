import unittest

from PIL import Image

from image_to_text import ImageToText
from tools import BLOCK_WIDTH, BLOCK_HEIGHT, ParameterException


class TestImageToText(unittest.TestCase):
    def test_image_to_text_takes_a_block(self):
        block = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))
        itt = ImageToText(block)

        self.assertEqual(str(itt), "00000000000000000000")

    def test_refuses_image_if_not_of_block_size(self):
        block = Image.new("1", (BLOCK_WIDTH + 1, BLOCK_HEIGHT))
        with self.assertRaises(ParameterException):
            ImageToText(block)

    def test_refuses_image_if_not_of_one_bit_format(self):
        block = Image.new("RGB", (BLOCK_WIDTH, BLOCK_HEIGHT))
        with self.assertRaises(ParameterException):
            ImageToText(block)

    def test_image_to_text_encodes_a_block(self):
        block = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))
        block.putpixel((0, 0), 1)
        block.putpixel((BLOCK_WIDTH - 1, BLOCK_HEIGHT - 1), 1)
        itt = ImageToText(block)

        self.assertEqual(str(itt), "80000000000000000001")
