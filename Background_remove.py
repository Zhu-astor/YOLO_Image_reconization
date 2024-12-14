# import the image process module
import cv2
import matplotlib
import rembg
from PIL import Image
matplotlib.use("Agg")
from glob import glob

# define the input image
# 若影像跟程式不在同一個資料夾底下，file_path需要輸入影像的完整路徑
file_path = glob('C:/Users/bubbl/Desktop/Contest/AI GO/Classification/datasets/datasets/total/*')
n = 0
for image in file_path:
    print(image)
    input = Image.open(image)
    # read the input image
    # 去除背景
    removed_bg_image = rembg.remove(input)
    # 保存去除背景后的图片
    removed_bg_image.save('C:/Users/bubbl/Desktop/Contest/AI GO/Classification/datasets/datasets/process/image'+str(n)+'.png')
    n = n + 1