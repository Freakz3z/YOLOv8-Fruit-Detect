# YOLOv8 Fruit Detection

这是一个使用YOLOv8模型进行水果检测的实时应用程序。

## 安装

请按照以下步骤安装所需的依赖项：

1. 克隆此仓库：
    ```sh
    git clone <repository_url>
    cd YOLOv8_FruitDetect
    ```

2. 安装依赖项：
    ```sh
    pip install -r requirements.txt
    ```

## 使用

1. 确保摄像头已连接并可用。
2. 运行应用程序：
    ```sh
    python GUI.py
    ```
3. 应用程序启动后，将显示实时视频流，并在检测到的水果上绘制标注。

## 文件说明

- `GUI.py`: 主应用程序文件，包含GUI和YOLO模型的加载与推理逻辑。
- `requirements.txt`: 列出了项目所需的所有Python依赖项。
- `fruit_nano.pt`: 预训练的YOLOv8模型文件。

## 数据集

数据集来源：https://drive.google.com/drive/folders/1UR6dCBjY1Bhf_NSMpGnobbCT_zoaTAxz

## 许可证

此项目遵循MIT许可证 - 有关更多详细信息，请参阅LICENSE文件。
