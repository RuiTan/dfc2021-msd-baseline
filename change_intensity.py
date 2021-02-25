import pandas as pd
import rasterio
import numpy as np
import cv2.cv2
import os

from tqdm import tqdm


def to_uint8(img: np.ndarray):
    max = np.nanmax(img)
    min = np.nanmin(img)
    # max = 1.0
    # min = -1.0
    img = 255 * (img-min)/(max-min)
    return img.astype(np.uint8)


def print_change_intensity_map(output_path):
    input_dataframe = pd.read_csv('data/local/val_inference_both.csv')
    image_fns = input_dataframe["image_fn"].values
    count = len(image_fns)
    for i in range(int(count/2)):
        filename = os.path.split(image_fns[i*2])[1].split('-')[0]
        with rasterio.open(image_fns[i*2]) as f_2013:
            R_2013 = f_2013.read(1)
            G_2013 = f_2013.read(2)
            B_2013 = f_2013.read(3)
            NIR_2013 = f_2013.read(4)
        with rasterio.open(image_fns[i*2+1]) as f_2017:
            R_2017 = f_2017.read(1)
            G_2017 = f_2017.read(2)
            B_2017 = f_2017.read(3)
            NIR_2017 = f_2017.read(4)
        change_intensity_map = to_uint8(np.sqrt(np.square(R_2013-R_2017) +
                                       np.square(G_2013-G_2017) +
                                       np.square(B_2013-B_2017) +
                                       np.square(NIR_2013-NIR_2017)))
        cv2.imwrite(output_path + filename + '-change-intensity.png', change_intensity_map)


def separate_change(change_map, change_intensity_map, threshold=0.9):
    threshold = int(255*threshold)
    change_intensity_map[change_intensity_map <= threshold] = 0
    change_intensity_map[change_intensity_map > threshold] = 1
    change_map[change_intensity_map == 0] = 0
    return change_map

def NDVI(output_path):
    if not os.path.exists(output_path): os.makedirs(output_path)
    input_dataframe = pd.read_csv('data/local/val_inference_both.csv')
    image_fns = input_dataframe["image_fn"].values
    count = len(image_fns)
    for i in tqdm(range(count)):
        filename = os.path.split(image_fns[i])[1].split('.')[0]
        with rasterio.open(image_fns[i]) as f:
            R = f.read(1).astype(np.float64)
            G = f.read(2).astype(np.float64)
            B = f.read(3).astype(np.float64)
            NIR = f.read(4).astype(np.float64)
        NDVI_map = to_uint8((NIR-R)/(NIR+R))
        cv2.imwrite(output_path + filename + '-ndvi.png', NDVI_map)

def NDWI(output_path):
    if not os.path.exists(output_path): os.makedirs(output_path)
    input_dataframe = pd.read_csv('data/local/val_inference_both.csv')
    image_fns = input_dataframe["image_fn"].values
    count = len(image_fns)
    for i in tqdm(range(count)):
        filename = os.path.split(image_fns[i])[1].split('.')[0]
        with rasterio.open(image_fns[i]) as f:
            R = f.read(1).astype(np.float64)
            G = f.read(2).astype(np.float64)
            B = f.read(3).astype(np.float64)
            NIR = f.read(4).astype(np.float64)
        NDVI_map = to_uint8((G - NIR) / (NIR + G))
        cv2.imwrite(output_path + filename + '-ndwi.png', NDVI_map)

# print_change_intensity_map('data/change_intensity/')

if __name__ == '__main__':
    NDVI('data/NDVI/')
    # NDWI('data/NDWI/')
