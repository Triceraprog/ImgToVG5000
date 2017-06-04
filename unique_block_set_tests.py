import unittest

from PIL import Image

from tools import BLOCK_WIDTH, BLOCK_HEIGHT, are_images_equal
from unique_block_set import UniqueBlockSet


class TestUniqueBlockSet(unittest.TestCase):
    def test_starts_with_no_block(self):
        block_set = UniqueBlockSet()
        self.assertEqual(len(block_set), 0)

    def test_can_add_a_block(self):
        block = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))

        block_set = UniqueBlockSet()
        block_set.add(block)

        self.assertEqual(len(block_set), 1)

    def test_can_get_a_unique_block_with_identical_content(self):
        block = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))

        block_set = UniqueBlockSet()
        block_set.add(block)

        new_block = block_set.get(block)
        self.assertTrue(are_images_equal(block, new_block))

    def test_identical_blocks_only_give_one_unique_block(self):
        block1 = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))
        block2 = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))
        block3 = Image.new("1", (BLOCK_WIDTH, BLOCK_HEIGHT))
        block3.putpixel((0, 0), 1)

        block_set = UniqueBlockSet()
        block_set.add(block1)
        block_set.add(block2)
        block_set.add(block3)

        self.assertEqual(len(block_set), 2)
        new_block1 = block_set.get(block1)
        new_block2 = block_set.get(block2)
        new_block3 = block_set.get(block3)
        self.assertEqual(new_block1, new_block2)
        self.assertNotEqual(new_block2, new_block3)
