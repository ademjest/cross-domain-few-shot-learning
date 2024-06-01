import os
import shutil
from sklearn.model_selection import train_test_split

# 设置数据集路径
dataset_dir = 'C:/Users/cxl/Desktop/模式识别课程设计/data/Office_Home/Real_World'  # 替换为原始文件夹的实际路径
output_dir = 'C:/Users/cxl/Desktop/模式识别课程设计/data/Office_Home/Real_World_Split'  # 替换为输出文件夹的实际路径

# 创建输出目录结构
os.makedirs(os.path.join(output_dir, 'train'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'val'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'test'), exist_ok=True)

# 获取所有类别文件夹
category_folders = [d for d in os.listdir(dataset_dir)
                    if os.path.isdir(os.path.join(dataset_dir, d))]

# 对每个类别执行操作
for category in category_folders:
    category_path = os.path.join(dataset_dir, category)
    images = os.listdir(category_path)

    # 划分数据集
    train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)
    train_images, val_images = train_test_split(train_images, test_size=0.25, random_state=42)  # 0.25 * 0.8 = 0.2

    # 创建类别的输出目录
    train_category_dir = os.path.join(output_dir, 'train', category)
    val_category_dir = os.path.join(output_dir, 'val', category)
    test_category_dir = os.path.join(output_dir, 'test', category)

    # 创建类别目录
    os.makedirs(train_category_dir, exist_ok=True)
    os.makedirs(val_category_dir, exist_ok=True)
    os.makedirs(test_category_dir, exist_ok=True)

    # 划分图片到相应的集合目录
    for image in train_images:
        shutil.move(os.path.join(category_path, image), os.path.join(train_category_dir, image))
    for image in val_images:
        shutil.move(os.path.join(category_path, image), os.path.join(val_category_dir, image))
    for image in test_images:
        shutil.move(os.path.join(category_path, image), os.path.join(test_category_dir, image))

print("Dataset split completed.")