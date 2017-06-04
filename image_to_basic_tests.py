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

    def test_basic_outputs_encoded_blocks(self):
        im = BlockImage(construct_redundant_image())
        basic = ImageToBasic(im)

        character_count = 0
        found_char_1 = False
        found_char_2 = False
        found_char_3 = False

        for line in basic:
            if "SETEG " in line:
                character_count += 1
            if "80000000000000000000" in line:
                found_char_1 = True
            if "40000000000000000000" in line:
                found_char_2 = True
            if "00100000000000000000" in line:
                found_char_3 = True

        self.assertEqual(3, character_count)
        self.assertTrue(found_char_1, "Did not found Encoded Character 1")
        self.assertTrue(found_char_2, "Did not found Encoded Character 2")
        self.assertTrue(found_char_3, "Did not found Encoded Character 3")

    def test_basic_outputs_index_data(self):
        im = BlockImage(construct_redundant_image())
        basic = ImageToBasic(im)

        found_data = False
        for line in basic:
            if "DATA 32,32,33,33,34,34" in line:
                found_data = True

        self.assertTrue(found_data, "DATA section was not found")
