from tools import BLOCK_WIDTH, BLOCK_HEIGHT, ParameterException


def encode(block):
    encoded = ""
    for y in range(BLOCK_HEIGHT):
        acc = 0
        for x in range(BLOCK_WIDTH):
            p = block.getpixel((x, y))
            if p:
                acc += 2 ** (7 - x)

        encoded += "%02.X" % acc
    return encoded


class ImageToText:
    def __init__(self, block):
        if block.size != (BLOCK_WIDTH, BLOCK_HEIGHT):
            raise ParameterException()

        if block.mode != "1":
            raise ParameterException()

        self.representation = encode(block)

    def __str__(self):
        return self.representation
