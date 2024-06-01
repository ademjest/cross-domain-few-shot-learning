import os
import shutil
import random


def split_dataset(base_dir, output_dir, train_ratio=0.7, val_ratio=0.15):
    categories = os.listdir(base_dir)
    for category in categories:
        category_path = os.path.join(base_dir, category)
        if not os.path.isdir(category_path):
            continue

        images = os.listdir(category_path)
        random.shuffle(images)

        train_count = int(len(images) * train_ratio)
        val_count = int(len(images) * val_ratio)

        train_images = images[:train_count]
        val_images = images[train_count:train_count + val_count]
        test_images = images[train_count + val_count:]

        save_split_images(output_dir, 'train', category, category_path, train_images)
        save_split_images(output_dir, 'val', category, category_path, val_images)
        save_split_images(output_dir, 'test', category, category_path, test_images)


def save_split_images(output_dir, split, category, category_path, images):
    split_dir = os.path.join(output_dir, split, category)
    os.makedirs(split_dir, exist_ok=True)

    for image in images:
        src_image_path = os.path.join(category_path, image)
        dest_image_path = os.path.join(split_dir, image)
        shutil.copyfile(src_image_path, dest_image_path)


if __name__ == "__main__":
    art_dir = r"G:\模式识别\课设\数据集\OfficeHome\OfficeHomeDataset_10072016\Art"
    clipart_dir = r"G:\模式识别\课设\数据集\OfficeHome\OfficeHomeDataset_10072016\Clipart"
    output_dir = r"G:\Python\python_work\conda_test\metric_learning_few_shots\prototypical-networks-few-shot-learning" \
                 r"-main\datasets\officehome"

    split_dataset(art_dir, output_dir)
    split_dataset(clipart_dir, output_dir)
