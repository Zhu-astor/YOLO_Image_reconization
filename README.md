
# 📸 **YOLO 影像辨識專案**  
本專案利用 **YOLOv8** 模型進行影像物件辨識，提供一套完整的影像處理與辨識流程。專案包含資料預處理、模型訓練、測試及轉換至 TensorFlow Lite 模型的工具程式。

---

## 🚀 **專案目錄**

```bash
.
├── AutoLabel.py           # 自動標註工具
├── Background_remove.py   # 背景去除腳本
├── calibration_image_sample_data_20x12.npy # 樣本校正數據
├── config.yaml            # 訓練設定檔
├── Data_preprocess.py     # 資料預處理腳本
├── Data_rename.py         # 資料重新命名工具
├── Data_setlabels.py      # 標籤設定工具
├── test.py                # 測試腳本
├── Totflite.py            # 模型轉換至 TFLite 工具
├── train.py               # 訓練腳本
└── yolov8n.pt             # YOLOv8 模型權重檔
```

---

## 📝 **專案介紹**
本專案使用 **YOLOv8**（You Only Look Once）進行高效能影像物件偵測，並整合多項影像處理工具與功能：

- **🔧 資料預處理**：包含標註、背景去除及資料重命名。
- **🛠️ 訓練工具**：使用 YOLOv8 模型進行訓練與調校。
- **🧪 模型測試**：對輸入影像進行辨識測試並輸出結果。
- **💡 模型轉換**：將 YOLO 模型轉換至 TensorFlow Lite 格式，以便部署於行動裝置。

---

## ⚙️ **安裝步驟**

### **1. 環境需求**
請確保安裝以下套件：

- Python 3.8 以上
- PyTorch
- OpenCV
- NumPy
- Ultralytics（YOLOv8 依賴套件）

### **2. 安裝套件**
使用 `pip` 安裝所需套件：

```bash
pip install torch torchvision opencv-python numpy ultralytics
```

---

## 🚀 **使用方法**

### **1. 資料預處理**
使用提供的腳本進行資料預處理：

- **去除背景**  
   ```bash
   python Background_remove.py
   ```

- **標註與標籤設定**  
   ```bash
   python Data_setlabels.py
   ```

- **重新命名資料**  
   ```bash
   python Data_rename.py
   ```

---

### **2. 訓練 YOLO 模型**
執行 `train.py` 訓練 YOLO 模型：

```bash
python train.py --data config.yaml --weights yolov8n.pt --epochs 50
```

**參數說明：**
- `--data`：資料集設定檔。
- `--weights`：預訓練權重（`yolov8n.pt`）。
- `--epochs`：訓練回合數。

---

### **3. 模型測試**
使用 `test.py` 測試 YOLO 模型：

```bash
python test.py --source images/test_image.jpg --weights runs/train/weights/best.pt
```

---

### **4. 模型轉換**
將 YOLO 模型轉換為 TensorFlow Lite 格式，方便行動裝置部署：

```bash
python Totflite.py --weights runs/train/weights/best.pt
```

---

## 📊 **結果展示**
以下為 YOLOv8 模型的影像辨識範例：

| 輸入影像                    | 輸出影像                       |
|-----------------------------|--------------------------------|
|![IMG_20240516_153723_jpg rf 6d9b870075cd4f92dc99e03b042ef21d](https://github.com/user-attachments/assets/27eda09e-dce7-4b90-be29-ea1a5917f6da)| ![IMG_20240516_153723_jpg rf 6d9b870075cd4f92dc99e03b042ef21d](https://github.com/user-attachments/assets/a6a631c1-8d2b-4e5e-929f-bd5cd872464b)|

---

## 📂 **資料集**
請將資料集放置於專案根目錄的 `images` 資料夾中，並確保標註格式符合 YOLO 標準。

**資料集結構：**
```bash
images/
├── train/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── val/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── labels/
    ├── image1.txt
    ├── image2.txt
    └── ...
```

---

## 🎯 **未來規劃**
- 優化 YOLO 模型參數以提升辨識精度。
- 增加多目標追蹤功能（如 ReID 技術）。
- 支援更多影像處理功能（如邊緣偵測、特徵增強）。

---

## 🧑‍💻 **貢獻者**
- **Your Name**：專案開發者與維護者
- **其他貢獻者（如有）**

---

## 📜 **授權**
本專案依據 [MIT License](https://opensource.org/licenses/MIT) 授權開源，歡迎自由使用與改進。

---

## 📬 **聯絡方式**
若有任何問題或建議，請聯絡：  
📧 **Email**: your-email@example.com  
🌐 **GitHub**: [你的 GitHub 連結](https://github.com/你的帳號)

---

### 🎉 **感謝您的使用！如果覺得有幫助，歡迎按下 ⭐️ Star 支持此專案！**
