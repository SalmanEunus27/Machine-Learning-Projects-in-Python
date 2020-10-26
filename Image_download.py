# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 21:42:59 2020

@author: salman
"""

import requests
import cv2
import os
from imutils import paths
url_path = open('C:\\Users\\salma\\Downloads\\download').read().strip().split('\n')
total = 0
if not os.path.exists('images'):
    os.mkdir('images')
image_path = 'images'
for url in url_path:
    try:
        req = requests.get(url, timeout=60)
        file_path = os.path.sep.join([image_path, '{}.jpg'.format(
            str(total).zfill(6))]
        )
        file = open(file_path, 'wb')
        file.write(req.content)
        file.close()
        print('Downloaded {}'.format(file_path))
        total += 1
    except:
        print('Could not download {}. Downloading next file'.format(file_path))
        
for imagePath in paths.list_images('images'):
    delete_image = False
    try:
        image = cv2.imread(imagePath)
        if image is None:
            delete_image = True
    # if OpenCV cannot load the image
    except:
        delete_image = True
    if delete_image:
        print('Deleting {}'.format(imagePath))
        os.remove(imagePath)