
### Pipe Detection 
#pip install pytorch
import PIL
import streamlit as st
from ultralytics import YOLO
import base64
#!pip install pandas ultralytics
from PIL import Image
#pip install SparseDtype
# Replace the relative path to your weight file
model_path = r"E:\project\best.pt"

# Setting page layout
st.set_page_config(
  page_title="Pipe Inventory Management System",
  page_icon="🤖",
  layout="wide",
  initial_sidebar_state="expanded"
)

# Creating sidebar with a background color
st.markdown(
    """
    <style>
    #MainMenu {
        background-color: blue; /* Change the color code to the one you prefer */
    }
    .sidebar .sidebar-content {
        color: brown; /* Text color in the sidebar */
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("Image/Video Config")
    source_img = st.file_uploader("Please Choose a File...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

# Adding Background to the page
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string});
            background-size: cover;
            opacity: 0.80; /* Set opacity to 80% (0.80) */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Example usage
image_path = r"E:\project\img.jpg"
#image_path = r"E:\project\img.jpg"
add_bg_from_local(image_path)

# Model Options
confidence = float(st.slider("Select Model Confidence", 25, 100, 40)) / 100

# Creating main page heading
st.title("Object Detection using YOLOv8")

# Creating two columns on the main page
col1, col2 = st.columns(2)

# Initialize boxes and res_plotted variables
boxes = []
res_plotted = None

# Adding image to the first column if an image is uploaded
with col1:
    if source_img:
        uploaded_image = PIL.Image.open(source_img)
        st.image(source_img, caption="Uploaded Image", use_column_width=True)

# Detecting objects in the image
if st.sidebar.button('Detect Objects'):
    try:
        model = YOLO(model_path)
    except Exception as ex:
        st.error(f"Unable to load the model. Check the specified path: {model_path}")
        st.error(ex)

    res = model.predict(uploaded_image, conf=confidence)
    boxes = res[0].boxes
    res_plotted = res[0].plot()[:, :, ::-1]

# Displaying the detection results
# Creating a table to display the labels and number of classes present
class_counts = {}
row_num = 1

for box in boxes:
    try:
        class_name = model.names[box.cls]
    except KeyError:
        class_id = box.cls.cpu().item()
        class_id = int(class_id)
        with open(r"E:\project\class_name.text", "r") as f:
            coco_names = f.read().splitlines()
            if class_id < len(coco_names):
                class_name = coco_names[class_id]
            else:
                class_name = "Unknown"

    if class_name not in class_counts:
        class_counts[class_name] = 0
    class_counts[class_name] += 1

# Create a list of rows for the table
table_data = [["Type of Object", "Object Count"]]
for class_name, class_count in class_counts.items():
    table_data.append([class_name, class_count])

# Display the table
st.table(table_data)

with col2:
    if res_plotted is not None:
        st.image(res_plotted, caption='Detected Image', use_column_width=True)
        with st.expander("Detection Results"):
            for box in boxes:
                class_name = model.names[box.cls] if box.cls in model.names else "Unknown"
                st.write(f"Row {row_num}:")
                st.write(f"Type of Object: {class_name}")
                st.write(f"Object Count: {class_counts[class_name]}")
                row_num += 1
    else:
        st.write("No image is uploaded yet!")