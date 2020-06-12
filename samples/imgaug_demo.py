import imageio
import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np

image = imageio.imread("D:/vedai/VEDAI_COCO/train2017/00000049.png")

seq = iaa.Sequential([
    iaa.Affine(rotate=(-25, 25)),
    iaa.AdditiveGaussianNoise(scale=(30, 90)),
    iaa.Crop(percent=(0, 0.4)),
    iaa.Fliplr(0.5),
    iaa.Flipud(0.5),
    iaa.GaussianBlur(sigma=(0.0, 5.0))
], random_order=True)

images_aug = [seq.augment_image(image) for _ in range(20)]

print("Augmented:")
ia.imshow(ia.draw_grid(images_aug, cols=5, rows=4))
