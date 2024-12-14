import torchvision.transforms as transforms
from PIL import Image
from glob import glob
# 定義數據增強變換
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),  # 隨機水平翻轉
    transforms.RandomRotation(degrees=30),   # 隨機旋轉
    transforms.RandomResizedCrop(size=640, scale=(0.4, 1.3)),  # 隨機裁剪並調整大小
    transforms.ColorJitter(brightness=(0.1,1.2)),  # 只調整亮度
    transforms.ToTensor(),                   # 轉換為 Tensor
])
n = 0
num = 10
file_path = glob('C:/Users/bubbl/Desktop/Contest/AI GO/Classification/datasets/datasets/valid/images/*')
for img_path in file_path:
    # 加載圖片
    image = Image.open(img_path)
    img_name = img_path[len(img_path)-10:len(img_path)-4]
    # 應用數據增強
    for i in range(num):
        augmented_image = transform(image)
        augmented_image_pil = transforms.ToPILImage()(augmented_image)
        augmented_image_pil.save('C:/Users/bubbl/Desktop/Contest/AI GO/Classification/datasets/datasets/valid/images/'+img_name+'_preprocess_'+str(n)+'.png')
        n = n + 1
