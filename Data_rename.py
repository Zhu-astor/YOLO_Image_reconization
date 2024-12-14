import shutil
import os
from shutil import copy
from glob import glob


# file_path = "C:/Users/bubbl/Downloads/SIR2/Postcard Dataset/Postcard Dataset/Focus"
# num = 0
# for i in folder_name:
#     for j in range(1,32):
#         file_exist = False
#         f1 = file_path + "/" + i + "/" + (str)(j)  + "/" + i +"-5-"+"m-"+str(j)+".png"
#         if os.path.isfile(f1):
#             print("檔案存在")
#             file_exist = True
#             num = num + 1
#         else:
#             print("檔案不存在")
#         if file_exist == True:
#             f2 = "C:/Users/bubbl/Desktop/Contest/AI GO/GAN_Test/Dataset/reflection/image_" + (str)(num+300) + ".jpg"
#             shutil.copyfile(f1,f2)
file_path = glob('C:/Users/bubbl/Desktop/Contest/AI GO/Classification/datasets/datasets/process/*')
n = 0
for img_path in file_path:
    img_original_name = 'C:/Users/bubbl/Desktop/Contest/AI GO/Classification/datasets/datasets/process/'
    path_len = len(img_original_name)
    img_number = img_path[path_len+5 : len(img_path)-4]
    # print(img_path)
    class_name = ""
    # print(int(img_number))
    if int(img_number)<=62:
        class_name = "obj_1_" + str(n)
    elif int(img_number)<=111:
        class_name = "obj_2_" + str(n)
    elif int(img_number)<=166:
        class_name = "obj_3_" + str(n)
    elif int(img_number)<=194:
        class_name = "obj_4_" + str(n)
    elif int(img_number)<=258:
        class_name = "obj_5_" + str(n)
    elif int(img_number)<=277:
        class_name = "obj_6_" + str(n)
    elif int(img_number)<=347:
        class_name = "obj_7_" + str(n)
    print(class_name)
    img_path2 = img_original_name+class_name+'.jpg'
    shutil.copyfile(img_path,img_path2)
    n = n + 1
        
    
    
