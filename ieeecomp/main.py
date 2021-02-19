from DataUtil import *

if __name__ == '__main__':
    image_paths = getAllImageData('data_path')
    ilist = []
    for i in image_paths['naip_2013']:
        ilist.append(int(i.split('_')[0]))
    ilist.sort()

    image_paths = getAllImageData('full_data_path')
    ilist1 = []
    for i in image_paths['naip_2013']:
        ilist1.append(int(i.split('_')[0]))
    ilist1.sort()
    print(len(ilist))
    print(len(ilist1))
    print(set(ilist) <= set(ilist1))

    # print(len(image_paths['naip_2013']))
    # print(len(image_paths['naip_2017']))
    # print(len(image_paths['nlcd_2013']))
    # print(len(image_paths['nlcd_2016']))
    # print(len(image_paths['landsat_2013']))
    # print(len(image_paths['landsat_2014']))
    # print(len(image_paths['landsat_2015']))
    # print(len(image_paths['landsat_2016']))
    # print(len(image_paths['landsat_2017']))

