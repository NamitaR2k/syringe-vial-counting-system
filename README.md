Smart Medical Supply Counter Using Computer Vision

Overview

This project is an AI-based system that detects and counts syringes and vials using computer vision techniques. It is designed to improve accuracy and efficiency in medical inventory management by reducing manual counting errors.

Features

* Automated detection of syringes and vials
* Real-time object counting
* High accuracy using deep learning models
* User-friendly interface built with Streamlit

Model Details

* Model: YOLOv8s (You Only Look Once - Version 8, Small)
* mAP (Mean Average Precision): 90.1%
* Epochs: 25
* Image Size: 650

YOLOv8s is a lightweight and efficient object detection model suitable for real-time applications with limited computational resources.

Tech Stack

* Python
* OpenCV
* YOLOv8
* Roboflow (for annotation & dataset management)
* Streamlit (for deployment)
* Google Colab (GPU training)

Project Workflow

1. Collected and prepared image dataset of syringes and vials
2. Annotated images using Roboflow
3. Applied data augmentation to improve dataset size
4. Trained YOLOv8 model using transfer learning
5. Evaluated model performance
6. Deployed using Streamlit interface

Output

<img width="1704" height="636" alt="image" src="https://github.com/user-attachments/assets/811fe94a-75c1-4ec3-87de-51007266a0aa" />


Use Case

This system can be used in pharmaceutical and healthcare industries to automate inventory counting, reduce manual effort, and improve operational efficiency.


