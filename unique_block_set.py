from tools import are_images_equal


class UniqueBlockSet:
    def __init__(self):
        self.blocks = []

    def add(self, block):
        if block not in self:
            self.blocks.append(block)

    def get(self, asked_block):
        for block in self.blocks:
            if are_images_equal(block, asked_block):
                return block
        return None

    def __len__(self):
        return len(self.blocks)

    def __contains__(self, asked_block):
        for block in self.blocks:
            if are_images_equal(block, asked_block):
                return True
        return False
