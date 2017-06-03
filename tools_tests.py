import unittest

from tools import box_generator


class TestBoxGenerator(unittest.TestCase):
    def test_box_generator(self):
        target = [(0, 0, 8, 10), (8, 0, 16, 10), (0, 10, 8, 20), (8, 10, 16, 20)]
        test = []
        for box in box_generator(16, 20, 8, 10):
            test.append(box)

        self.assertEqual(target, test)