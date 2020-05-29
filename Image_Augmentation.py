# import the library and helpers
import imageio
import imgaug as ia
from imgaug import augmenters as iaa
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import matplotlib
import numpy as np

# use imageio library to read the image (alternatively you can use OpenCV cv2.imread() function)
image = imageio.imread('C:\\Users\\salma\\OneDrive\\Documents\\Python Codes\\Railway_Track_Image_Dataset\\30.jfif')

# initialize the augmenters for demo
rotate = iaa.Affine(rotate=(-25, 25)) # rotate image
gaussian_noise = iaa.AdditiveGaussianNoise(scale=(10, 60)) # add gaussian noise
crop = iaa.Crop(percent=(0, 0.4)) # crop image
hue = iaa.AddToHueAndSaturation((-60, 60))  # change their color
elastic_trans = iaa.ElasticTransformation(alpha=90, sigma=9) # water-like effect
coarse_drop = iaa.CoarseDropout((0.01, 0.1), size_percent=0.01)# set large image areas to zero
# get augmented images
image_rotated = rotate.augment_images([image])
image_noise = gaussian_noise.augment_images([image])
image_crop = crop.augment_images([image])
image_hue = hue.augment_images([image])
image_trans = elastic_trans.augment_images([image])
image_coarse = coarse_drop.augment_images([image])

# create an array of augmented images for the demo
images_aug = [image_rotated[0], image_noise[0], image_crop[0], image_hue[0], image_trans[0], image_coarse[0]]

# plot augmentation examples
plt.figure(figsize=(15,5))
plt.axis('off')
plt.imshow(np.hstack(images_aug))
plt.title('Sample augmentations')