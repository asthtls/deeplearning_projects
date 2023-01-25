# 데이터 분할을 위한 폴더 생성

import os
import shutil

original_dataset_dir = './dataset'
classes_list = os.listdir(original_dataset_dir)

base_dir = './splitted' # 데이터 분할 폴더 
train_dir = os.path.join(base_dir, 'train')
test_dir = os.path.join(base_dir, 'test')
val_dir = os.path.join(base_dir, 'val')

try:
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    if not os.path.exists(train_dir):
        os.mkdir(train_dir)
    if not os.path.exists(test_dir):
        os.mkdir(test_dir)
    if not os.path.exists(val_dir):
        os.mkdir(val_dir)

    for cls in classes_list:
        os.mkdir(os.path.join(train_dir, cls))
        os.mkdir(os.path.join(test_dir, cls))
        os.mkdir(os.path.join(val_dir, cls))
except:
    print("Error : Failed to create the directory.")


