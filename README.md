# ImgToVG5000
A program to turn a PNG file to a BASIC listing running on VG5000µ

(french below)

## Requirements

You need python3 with Pillow installed. You can use pip and the requirements.txt file to install the correct verison.

## Usage

    > python3 img_to_vg5000.py 
    usage: img_to_vg5000.py [-h] [--output-dithered] [--output-deduplicated]
                            [--output-block-palette] [--output-basic]
                            [--auto-crop] [--auto-reduce]
                            file

* The *output* options will send to the disk the different stages of the conversion.
* --auto-crop will crop the image to the bounding box according to Pillow.
* --auto-reduce will reduce the input image until the number of needed character doesn't exceed 96.

## Tips

The more black & white your image initially is, the more simple and accurate the conversion will be.

Also, prefer images with moderate size. 320x250 is the maximum theorical resolution, everything bigger is useless.

# Version française

## Pré-requis

Vous avez besoin de python3 avec Pillow d'installé. Vous pouvez utiliser pip avec le fichier requirements.txt pour installer la bonne version.

## Usage

    > python3 img_to_vg5000.py 
    usage: img_to_vg5000.py [-h] [--output-dithered] [--output-deduplicated]
                            [--output-block-palette] [--output-basic]
                            [--auto-crop] [--auto-reduce]
                            file

* Les options *output* écriront sur le disque les différentes étapes de la conversion.
* --auto-crop découpera l'image selon la boite englobante calculée par Pillow.
* --auto-reduce réduira progressivement l'image jusqu'à ce qu'elle nécessite un nombre de caractères inférieur ou égal 96.

## Astuces

Plus l'image initiale est en noir et blanc, plus la conversion sera simple et précise.

Préférez aussi des images de taille modérée. La résolution théorique maximale est de 320x250. Il est inutile d'avoir une image plus grande.
