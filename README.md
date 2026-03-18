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

Architecture

<img width="1704" height="636" alt="image" src="https://github.com/user-attachments/assets/7d0bf18a-8c8f-4768-acf3-aaff4edda88d" />


Output

<img width="1138" height="728" alt="image" src="https://github.com/user-attachments/assets/e311c5d5-317f-4f2f-a0a8-b57c49d91f8a" />   <img width="955" height="601" alt="image" src="https://github.com/user-attachments/assets/76cbe5ae-4d34-45dc-808a-424cfc554855" />




Use Case

This system can be used in pharmaceutical and healthcare industries to automate inventory counting, reduce manual effort, and improve operational efficiency.


