import os
import shutil
import numpy as np
from tqdm import tqdm
import os
import sys

# 将项目根目录添加到 PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
from config import DATA_PATH


def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def rmdir(path):
    if os.path.exists(path):
        shutil.rmtree(path)


# 清理并重新创建文件夹
rmdir(DATA_PATH + '/miniImageNet/images_background')
rmdir(DATA_PATH + '/miniImageNet/images_evaluation')
mkdir(DATA_PATH + '/miniImageNet/images_background')
mkdir(DATA_PATH + '/miniImageNet/images_evaluation')

# 收集类别
classes = []
new_path = os.path.join(DATA_PATH, 'mini_imagenet')
for split in ['train', 'val', 'test']:
    split_path = os.path.join(new_path, split)
    for class_name in os.listdir(split_path):
        class_dir = os.path.join(split_path, class_name)
        if os.path.isdir(class_dir):
            classes.append(class_name)

# 打乱并划分训练和测试集
np.random.seed(0)
np.random.shuffle(classes)
background_classes, evaluation_classes = classes[:80], classes[80:]

# 创建训练和测试集文件夹
for c in background_classes:
    mkdir(DATA_PATH + f'/miniImageNet/images_background/{c}/')
for c in evaluation_classes:
    mkdir(DATA_PATH + f'/miniImageNet/images_evaluation/{c}/')

# 移动图像到对应文件夹
for split in ['train', 'val', 'test']:
    split_path = os.path.join(new_path, split)
    for class_name in os.listdir(split_path):
        class_dir = os.path.join(split_path, class_name)
        if os.path.isdir(class_dir):
            subset_folder = 'images_evaluation' if class_name in evaluation_classes else 'images_background'
            for image_name in os.listdir(class_dir):
                if image_name.endswith('.jpg'):
                    src = os.path.join(class_dir, image_name)
                    dst = DATA_PATH + f'/miniImageNet/{subset_folder}/{class_name}/{image_name}'
                    shutil.copy(src, dst)

print("数据集重组完成")
