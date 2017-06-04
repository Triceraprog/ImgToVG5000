import argparse
import logging

from PIL import Image

from block_image import BlockImage
from image_to_basic import ImageToBasic
from tools import fix_size_to_block_multiple


def main(options):
    input_filename = options.file
    logger = logging.getLogger("convert")
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)

    logger.info("Start processing: %s" % input_filename)

    input_image = Image.open(input_filename)

    logger.debug("Input image has size: %s" % str(input_image.size))

    dithered_image = input_image.convert(mode="1", dither=Image.FLOYDSTEINBERG)

    if options.auto_crop:
        bbox = dithered_image.getbbox()
        if bbox is not None:
            dithered_image = dithered_image.crop(bbox)
            size = dithered_image.size
            logger.debug("Cropped image has size: %s" % str(size))

            new_size = fix_size_to_block_multiple(size)
            if new_size != size:
                logger.info("Resizing picture to: %s" % str(new_size))
                new_image = Image.new("1", new_size)
                new_image.paste(dithered_image, box=(0, 0, dithered_image.size[0], dithered_image.size[1]))
                dithered_image = new_image

        else:
            logger.error("Cannot crop a blank image")

    if options.output_dithered:
        logger.debug("Output of dithered image")
        dithered_image.save("dithered.png")

    block_image = BlockImage(dithered_image)
    block_image.deduplicate_blocks()

    if len(block_image.get_block_palette()) > 96:
        logger.error("Picture generates more than 96 blocks. BASIC output will be truncated.")

    if options.output_deduplicated:
        logger.debug("Output of de-duplicated image")
        block_image.save("de-duplicated.png")

    if options.output_block_palette:
        logger.debug("Output of the block palette")
        block_palette = block_image.get_block_palette()
        im = block_palette.get_image(320)
        im.save("block_palette.png")

    if options.output_basic:
        logger.debug("Output of the BASIC listing")
        basic = ImageToBasic(block_image)
        with open("image.bas", "w") as f:
            content = "\n".join(basic)
            f.write(content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert a picture file to a VG5000µ picture.")
    parser.add_argument('--output-dithered', action="store_true", dest="output_dithered")
    parser.add_argument('--output-deduplicated', action="store_true", dest="output_deduplicated")
    parser.add_argument('--output-block-palette', action="store_true", dest="output_block_palette")
    parser.add_argument('--output-basic', action="store_true", dest="output_basic")
    parser.add_argument('--auto-crop', action="store_true", dest="auto_crop")
    parser.add_argument('file', type=str, help="Filename of the input picture file")

    args = parser.parse_args()
    main(args)
