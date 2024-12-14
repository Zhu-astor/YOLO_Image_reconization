import os
from glob import glob

file_path = glob('C:/Users/bubbl/Desktop/Contest/AI GO/Classification/datasets/datasets/valid/images/*')

for img_path in file_path:
    
    path = "C:/Users/bubbl/Desktop/Contest/AI GO/Classification/datasets/datasets/valid/images/"
    path2 = "C:/Users/bubbl/Desktop/Contest/AI GO/Classification/datasets/datasets/valid/images/obj"
    len_path = len(path)
    len_path2 = len(path2)
    output_label_file = 'C:/Users/bubbl/Desktop/Contest/AI GO/Classification/datasets/datasets/valid/labels/' + img_path[len_path:len(img_path)-4] + ".txt"

    # 打開標註文件
    with open(output_label_file, 'w') as f:

                
        class_id = img_path[len_path2:len_path2+1]
                
        label = str(class_id)+" 0.5 0.5 1.0 1.0\n"
        
                
        f.write(label)


