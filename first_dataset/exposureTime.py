import os
from PIL import Image
from PIL.ExifTags import TAGS

img_file = 'DSC_0160.jpg'
image = Image.open(img_file)

exif = {}

for tag, value in image._getexif().items():
    if tag in TAGS:
        exif[TAGS[tag]]=value
if 'ExposureTime' in exif:
    extime=exif['ExposureTime']
print(extime)
