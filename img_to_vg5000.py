import argparse
import logging
from PIL import Image


def main(options):
    input_filename = options.file
    logger = logging.getLogger("convert")
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)

    logger.info("Start processing: %s" % input_filename)

    input_image = Image.open(input_filename)

    logger.debug("Input image has size: %s" % str(input_image.size))

    dithered_image = input_image.convert(mode="1", dither=Image.FLOYDSTEINBERG)

    if options.output_dithered:
        dithered_image.save("dithered.png")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert a picture file to a VG5000µ picture.")
    parser.add_argument('--output-dithered', action="store_true", dest="output_dithered")
    parser.add_argument('file', type=str, help="Filename of the input picture file")

    args = parser.parse_args()
    main(args)
