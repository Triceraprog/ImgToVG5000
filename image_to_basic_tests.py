import unittest

from block_image import BlockImage
from block_image_tests import construct_redundant_image
from image_to_basic import ImageToBasic


class TestImageToBasic(unittest.TestCase):
    def test_image_to_basic_takes_a_block_image(self):
        im = BlockImage(construct_redundant_image())
        basic = ImageToBasic(im)
        self.assertGreater(basic.get_line_count(), 0)

    def test_basic_contains_loops_for_blocks(self):
        im = BlockImage(construct_redundant_image())
        basic = ImageToBasic(im)

        found_x_loop = False
        found_y_loop = False

        x_loop = "FOR X=0 TO 1"
        y_loop = "FOR Y=0 TO 2"

        for line in basic:
            if x_loop in line:
                found_x_loop = True
            if y_loop in line:
                found_y_loop = True

        self.assertTrue(found_x_loop, "for loop for X not found")
        self.assertTrue(found_y_loop, "for loop for Y not found")

    def test_basic_first_line_is_10(self):
        im = BlockImage(construct_redundant_image())
        basic = ImageToBasic(im)

        all_lines = "\n".join(basic)
        self.assertEqual("10 ", all_lines[:3])

    def test_basic_centers_the_image(self):
        im = BlockImage(construct_redundant_image())
        basic = ImageToBasic(im)

        found_x_cursor_shift = False
        found_y_cursor_shift = False

        x_cursor_shift = "CURSORX X+19"
        y_cursor_shift = "CURSORY Y+11"

        for line in basic:
            if x_cursor_shift in line:
                found_x_cursor_shift = True
            if y_cursor_shift in line:
                found_y_cursor_shift = True

        self.assertTrue(found_x_cursor_shift, "cursor shift for X not found")
        self.assertTrue(found_y_cursor_shift, "cursor shift for Y not found")
