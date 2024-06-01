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


print("数据重组中------")
# 清理并重新创建文件夹
rmdir(DATA_PATH + '/officehome/images_background')
rmdir(DATA_PATH + '/officehome/images_evaluation')
mkdir(DATA_PATH + '/officehome/images_background')
mkdir(DATA_PATH + '/officehome/images_evaluation')

# 收集类别
classes = []
source_path = 'G:/模式识别/课设/数据集/OfficeHome/OfficeHomeDataset_10072016'
for domain in ['Art', 'Clipart']:
    domain_path = os.path.join(source_path, domain)
    for class_name in os.listdir(domain_path):
        class_dir = os.path.join(domain_path, class_name)
        if os.path.isdir(class_dir):
            classes.append(class_name)
print(f"已读取{source_path}所有类别")
# 去重类别并打乱划分训练和测试集
classes = list(set(classes))
np.random.seed(0)
np.random.shuffle(classes)
background_classes, evaluation_classes = classes[:len(classes) // 2], classes[len(classes) // 2:]

# 创建训练和测试集文件夹
for c in background_classes:
    mkdir(DATA_PATH + f'/officehome/images_background/{c}/')
for c in evaluation_classes:
    mkdir(DATA_PATH + f'/officehome/images_evaluation/{c}/')
print("已创建新的训练和测试文件夹")

# 移动图像到对应文件夹
for domain in ['art', 'clipart']:
    domain_path = os.path.join(source_path, domain)
    for class_name in os.listdir(domain_path):
        class_dir = os.path.join(domain_path, class_name)
        if os.path.isdir(class_dir):
            subset_folder = 'images_evaluation' if class_name in evaluation_classes else 'images_background'
            for image_name in os.listdir(class_dir):
                if image_name.endswith('.jpg'):
                    src = os.path.join(class_dir, image_name)
                    dst = DATA_PATH + f'/officehome/{subset_folder}/{class_name}/{image_name}'
                    shutil.copy(src, dst)

print("数据集重组完成")
