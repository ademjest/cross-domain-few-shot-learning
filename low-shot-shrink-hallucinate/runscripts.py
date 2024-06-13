import os

# 确保检查点目录存在
os.makedirs("checkpoints/ResNet10_sgm", exist_ok=True)

# 构建命令
command = """
python ./main.py --model ResNet10 traincfg base_classes_train_template.yaml  --valcfg base_classes_val_template.yaml  --print_freq 10 --save_freq 10  --aux_loss_wt 0.02 --aux_loss_type sgm --checkpoint_dir D:\low_shot\checkpoints\ResNet10_sgm
"""

# 运行命令
os.system(command)

