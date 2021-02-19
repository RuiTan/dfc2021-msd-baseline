import os

from ConfigParser import *

'''
naip: 高分图像，包含2013、2017
nlcd: 粗糙标签，包含2013、2016
landsat: 低分图像，包含2013-2017
'''


def getAllImageData(path_key: str):
    data_path = getKey(path_key)
    images_name = os.listdir(data_path)
    naip_2013_name = [naip for naip in images_name if naip.__contains__('naip-2013')]
    naip_2017_name = [naip for naip in images_name if naip.__contains__('naip-2017')]
    nlcd_2013_name = [nlcd for nlcd in images_name if nlcd.__contains__('nlcd-2013')]
    nlcd_2016_name = [nlcd for nlcd in images_name if nlcd.__contains__('nlcd-2016')]
    landsat_2013_name = [landsat for landsat in images_name if landsat.__contains__('landsat-2013')]
    landsat_2014_name = [landsat for landsat in images_name if landsat.__contains__('landsat-2014')]
    landsat_2015_name = [landsat for landsat in images_name if landsat.__contains__('landsat-2015')]
    landsat_2016_name = [landsat for landsat in images_name if landsat.__contains__('landsat-2016')]
    landsat_2017_name = [landsat for landsat in images_name if landsat.__contains__('landsat-2017')]
    images_path = {'naip_2013': naip_2013_name, 'naip_2017': naip_2017_name, 'nlcd_2013': nlcd_2013_name,
                   'nlcd_2016': nlcd_2016_name, 'landsat_2013': landsat_2013_name, 'landsat_2014': landsat_2014_name,
                   'landsat_2015': landsat_2015_name, 'landsat_2016': landsat_2016_name,
                   'landsat_2017': landsat_2017_name}
    return images_path
