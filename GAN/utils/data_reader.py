from torch.utils.data import Dataset
from torchvision.transforms import transforms
from PIL import Image
import os

imgsz = 512  # 缩放图像的大小


# 定义数据读取器
class LoadData(Dataset):
    def __init__(self, dir_path, number_of_channels, category, label_map):
        self.category = category
        self.label_map = label_map
        print(os.listdir(dir_path))
        self.imgs_info = [(os.path.join(dir_path, img), int(img.split('.')[0])) for img in os.listdir(dir_path)]
        self.tf = transforms.Compose([
            # 将图片尺寸resize到512*512
            transforms.Resize((imgsz, imgsz)),
            # 将图片转化为Tensor格式
            transforms.ToTensor(),
            # 将图片通道数转化为模型输入通道数
            transforms.Grayscale(number_of_channels),
            # 标准化(当模型出现过拟合的情况时，用来降低模型的复杂度)
            transforms.Normalize([0.5] * number_of_channels, [0.5] * number_of_channels)  # 图像标准化
        ])

    def __getitem__(self, index):
        img_path, none = self.imgs_info[index]
        label_str = self.category
        print(img_path)
        print(label_str)
        img = Image.open(img_path)
        img = img.convert('RGB')
        img = self.tf(img)
        label = self.label_map[label_str]
        return img, float(label)

    def __len__(self):
        return len(self.imgs_info)