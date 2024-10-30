import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import random
import panel as pn
from matplotlib.figure import Figure

# Define the data directory
data_dir = 'C:/Users/ADMIN/Desktop/chest_xray'
categories = ['NORMAL', 'PNEUMONIA']

# Initialize an empty DataFrame to hold the counts
data_counts = []

# Loop through each subfolder
for phase in ['train', 'val', 'test']:
    for category in categories:
        folder_path = os.path.join(data_dir, phase, category)
        count = len(os.listdir(folder_path))
        data_counts.append({'Phase': phase, 'Category': category, 'Count': count})

# Convert to DataFrame
df_counts = pd.DataFrame(data_counts)

ACCENT = "teal"
LOGO = "https://assets.holoviz.org/panel/tutorials/matplotlib-logo.png"

pn.extension(sizing_mode="stretch_width")

normal_images = os.listdir(os.path.join(data_dir, "train", 'NORMAL'))
sizes = []

for img in random.sample(normal_images, 100):  # Sample 100 images
    img_path = os.path.join(data_dir, "train", 'NORMAL', img)
    with Image.open(img_path) as im:
        sizes.append(im.size)

widths, heights = zip(*sizes)

fig = Figure(figsize=(8, 4))
ax = fig.subplots()
ax.hist(widths, bins=20, color=ACCENT)

component = pn.pane.Matplotlib(fig, format='svg', sizing_mode='scale_both')

pn.template.FastListTemplate(
    title="Interactive-Width", sidebar=[LOGO], main=[component], accent=ACCENT
).servable()