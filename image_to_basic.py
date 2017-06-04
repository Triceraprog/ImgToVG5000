SCREEN_BLOCK_WIDTH = 40
SCREEN_BLOCK_HEIGHT = 25


class ImageToBasic:
    def __init__(self, block_image):
        self.block_image = block_image
        block_width, block_height = self.block_image.block_size

        prologue = PROLOGUE_TEMPLATE.strip().split("\n")

        self.lines = []

        mapping = {"for_x": 1,
                   "for_y": 2,
                   "center_x": int((SCREEN_BLOCK_WIDTH - block_width) / 2),
                   "center_y": int((SCREEN_BLOCK_HEIGHT - block_height) / 2),
                   "line": 10}
        line_count = 10
        for line in prologue:
            mapping["line"] = line_count
            self.lines.append(line.format_map(mapping))
            line_count += 10

    def get_line_count(self):
        return len(self.lines)

    def __iter__(self):
        for line in self.lines:
            yield line


PROLOGUE_TEMPLATE = """
{line} INIT 6:EG0,6
{line} FOR Y=0 TO {for_y}
{line} FOR X=0 TO {for_x}
{line} READ I
{line} CURSORX X+{center_x}:CURSORY Y+{center_y}
{line} PRINT CHR$(I);
{line} NEXT X
{line} NEXT Y
"""
