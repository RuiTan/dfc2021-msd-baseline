from sklearn.cluster import KMeans
import os
import rasterio
import numpy as np


def read_imgs(input_path):
    x = []
    imgs = os.listdir(input_path)
    k = 0
    for i in imgs:
        k += 1
        if k >= 3:
            break
        with rasterio.open(input_path + i) as f:
            label = f.read(1)
            x = np.concatenate((x, np.reshape(label, -1)), axis=0)
    return x


def kmeans(clusters):
    print()
    clf = KMeans(n_clusters=clusters)
    x = read_imgs('/home/tanrui@corp.sse.tongji.edu.cn/tanrui/ieeecomp/methods/dfc2021-msd-baseline/data/NDVI/')
    x = x.reshape(-1, 1)
    clf.fit(x)
    centers = clf.cluster_centers_
    print(centers)


kmeans(3)

