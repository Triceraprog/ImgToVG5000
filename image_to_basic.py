from image_to_text import ImageToText
from tools import chunks

SCREEN_BLOCK_WIDTH = 40
SCREEN_BLOCK_HEIGHT = 25

CHARACTER_ENCODING_FIRST_LINE = 200
DATA_FIRST_LINE = 2000


class ImageToBasic:
    def __init__(self, block_image):
        self.block_image = block_image
        self.lines = []
        self.char_database = {}

        prologue_lines = self.__construct_prologue()
        self.lines.extend(prologue_lines)

        characters_lines = self.__construct_characters()
        self.lines.extend(characters_lines)

        data_lines = self.__construct_data()
        self.lines.extend(data_lines)

    def __construct_prologue(self):
        block_width, block_height = self.block_image.block_size

        prologue_lines = []
        prologue = PROLOGUE_TEMPLATE.strip().split("\n")
        mapping = {"for_x": int(block_width - 1),
                   "for_y": int(block_height - 1),
                   "center_x": int((SCREEN_BLOCK_WIDTH - block_width) / 2),
                   "center_y": int((SCREEN_BLOCK_HEIGHT - block_height) / 2),
                   "char_encoding": CHARACTER_ENCODING_FIRST_LINE,
                   "line": 10}
        line_count = 10
        for line in prologue:
            mapping["line"] = line_count
            prologue_lines.append(line.format_map(mapping))
            line_count += 10
        return prologue_lines

    def __construct_characters(self):
        line_count = CHARACTER_ENCODING_FIRST_LINE
        block_list = self.block_image.get_block_palette()

        character_lines = []
        for index, block in enumerate(block_list):
            char_index = 32 + index
            if char_index > 128:
                break
            itt = ImageToText(block)

            self.char_database[str(itt)] = char_index

            line = CHARACTER_TEMPLATE.format(line=line_count, char_index=char_index, encoded_char=itt)
            character_lines.append(line)
            line_count += 10

        character_lines.append("{line} RETURN".format(line=line_count))

        return character_lines

    def __construct_data(self):
        indexed_content = []
        for block in self.block_image.blocks:
            itt = ImageToText(block)
            char_index = self.char_database.get(str(itt), 32)
            indexed_content.append(str(char_index))

        line_count = DATA_FIRST_LINE
        data_lines = []
        for data in chunks(indexed_content, 16):
            line = DATA_TEMPLATE.format(line=line_count, content=",".join(data))
            data_lines.append(line)
            line_count += 10

        return data_lines

    def get_line_count(self):
        return len(self.lines)

    def __iter__(self):
        for line in self.lines:
            yield line


PROLOGUE_TEMPLATE = """
{line} INIT 0,0:EG6,0
{line} FOR Y=0 TO {for_y}
{line} FOR X=0 TO {for_x}
{line} READ I
{line} CURSORX X+{center_x}:CURSORY Y+{center_y}
{line} PRINT CHR$(I);
{line} NEXT X
{line} NEXT Y
{line} GOSUB {char_encoding}
{line} GOTO {line}
"""

CHARACTER_TEMPLATE = '{line} SETEG {char_index},"{encoded_char}"'

DATA_TEMPLATE = "{line} DATA {content}"
