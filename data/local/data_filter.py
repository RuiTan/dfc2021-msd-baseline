import pandas as pd
import numpy as np
import os

training_set = pd.read_csv('training_set_naip_nlcd_both_old.csv', sep=',')
drop_rows = []
invalid_samples = np.loadtxt('invalid_samples.txt', dtype=np.int)
for index, row in training_set.iterrows():
    # print(index, row['image_fn'], row['label_fn'])
    if int(os.path.splitext(os.path.split(row['image_fn'])[1])[0].split('_')[0]) in invalid_samples:
        drop_rows.append(index)
print(drop_rows)
training_set_new = training_set.drop(drop_rows)
training_set_new.to_csv('./training_set_naip_nlcd_both.csv', sep=',', index=0)