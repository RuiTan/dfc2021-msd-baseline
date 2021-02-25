import rasterio
import numpy as np
import os
from cv2 import cv2

def tif_to_rgb(image_path, input_path, output_path):
    with rasterio.open(os.path.join(input_path, image_path)) as f:
        R = np.expand_dims(f.read(1), axis=2)
        G = np.expand_dims(f.read(2), axis=2)
        B = np.expand_dims(f.read(3), axis=2)
        image = np.concatenate((R,G,B), axis=-1)
        cv2.imwrite(os.path.join(output_path, image_path), image)

def visualize_tif(image_id):
    input_path = '/archive/cold0/tanrui/IEEEData'
    image_id = str(image_id)
    image_naip_2013 = image_id + '_naip-2013.tif'
    image_naip_2017 = image_id + '_naip-2017.tif'
    out_path = '/home/tanrui@corp.sse.tongji.edu.cn/tanrui/ieeecomp/methods/dfc2021-msd-baseline/results/naip_rgb'
    tif_to_rgb(image_naip_2013, input_path, out_path)
    tif_to_rgb(image_naip_2017, input_path, out_path)
