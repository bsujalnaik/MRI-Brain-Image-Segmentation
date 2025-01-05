import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from skimage import io, color
# Load the MRI image
image = io.imread('MRI_Brain_GE_Healthcare.jpg')
# Convert the image to grayscale
gray_image = color.rgb2gray(image)
# Reshape the image to 1D array
reshaped_image = gray_image.reshape(-1, 1)
# Define the number of clusters (brain tissues)
# Cluster 1: Gray Matter (responsible for information processing)
# Cluster 2: White Matter (connects different brain regions)
# Cluster 3: Cerebrospinal Fluid (protects the brain)
num_clusters = 3
# Fit Gaussian MixtMiMixtMi Rdxtureure Model
gmm = GaussianMixture(n_components=num_clusters, random_state=42)
gmm.fit(reshaped_image)
# Predict the labels (cluster assignments)
predicted_labels = gmm.predict(reshaped_image)# Reshape the predicted labels to original image shape
segmented_image = predicted_labels.reshape(gray_image.shape)
# Display original and segmented images
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(segmented_image, cmap='viridis')
plt.title('Segmented Image')
plt.axis('off')

plt.show()