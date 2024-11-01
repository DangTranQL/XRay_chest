import os
import glob
import pandas as pd
import panel as pn
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import random

pn.extension()

# Define paths
base_path = "C:/Users/ADMIN/Desktop/chest_xray"
train_path = os.path.join(base_path, "train")
test_path = os.path.join(base_path, "test")

# Load data
def load_data():
    data = []
    for dataset in ['train', 'test']:
        for label in ['NORMAL', 'PNEUMONIA']:
            folder_path = os.path.join(base_path, dataset, label)
            image_files = glob.glob(os.path.join(folder_path, '*.jpeg'))
            data.extend([(file, label) for file in image_files])
    return pd.DataFrame(data, columns=['file', 'label'])

source_data = load_data()

# Function to get filtered DataFrame
def get_filtered_df(label_select, dataset_select, index):
    data =  source_data[(source_data['label'] == label_select) & (source_data['file'].str.contains(dataset_select))]
    img_path = data["file"].iloc[index]
    img = Image.open(img_path)
    pn.pane.Image(img, width=300)
    return data

# Widgets for selection
dataset_select = pn.widgets.Select(name="Dataset", options=['train', 'test'], value='train')
label_select = pn.widgets.Select(name="Class", options=['NORMAL', 'PNEUMONIA'], value='NORMAL')
image_index = pn.widgets.IntSlider(name="Image Index", start=0, end=len(source_data)-1, value=0)

df = pn.rx(get_filtered_df)(label_select=label_select, dataset_select=dataset_select, index=image_index)
count = df.rx.len()
    
widths = []
heights = []
for img_path in random.sample(os.listdir(os.path.join(base_path, dataset_select.value, label_select.value)), 100):
    print(random.sample(os.listdir(os.path.join(base_path, dataset_select.value, label_select.value)), 100))
    img = Image.open(img_path)
    widths.append(img.width)
    heights.append(img.height)

# Create histograms
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].hist(widths, bins=20, color='blue', alpha=0.7)
axs[0].set_title('Width Distribution')
axs[0].set_xlabel('Width (pixels)')
axs[0].set_ylabel('Frequency')

axs[1].hist(heights, bins=20, color='green', alpha=0.7)
axs[1].set_title('Height Distribution')
axs[1].set_xlabel('Height (pixels)')
axs[1].set_ylabel('Frequency')

plt.tight_layout()
histogram_pane = pn.pane.Matplotlib(fig, tight=True)

# Statistics
stats = df.groupby('label').size()

# Display indicators
indicators = pn.Column(
    pn.indicators.Number(value=stats, name='Number of X-rays', format="{value:,.0f}"),
)

# Layout the dashboard
dashboard = pn.Column(
    pn.Row(dataset_select, label_select, image_index),
    indicators
)

dashboard.servable()
