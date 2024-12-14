from ultralytics import YOLO


model = YOLO("C:/Users/bubbl/Desktop/Contest/AI GO/GAN_Test/no_reflex2000_saved_model/no_reflex2000_float32.tflite")
# C:/Users/bubbl/Desktop/Contest/AI GO/GAN_Test/no_reflex2000.pt




source="C:/Users/bubbl/Downloads/image3/image.png"



result = model(source)

#include<bits/stdc++.h>

#print(type(result))

#print(result)

#TRY THIS IN TERMINAL: yolo detect predict model=museumV3  source=datasets/test/images save=true



