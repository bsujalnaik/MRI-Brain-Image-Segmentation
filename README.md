# 🧠 MRI Brain Image Segmentation

This project demonstrates an image segmentation technique applied to MRI brain images using a **Gaussian Mixture Model (GMM)**. The segmentation divides the brain image into three distinct regions: Gray Matter, White Matter, and Cerebrospinal Fluid. The segmentation is useful for medical image analysis, assisting in diagnosing neurological conditions and understanding brain structures.

---
## 📝 Project Explanation

### 🎯 Objective
The goal is to segment an MRI brain image into three regions:
1. **Gray Matter**: Responsible for information processing.
2. **White Matter**: Connects different regions of the brain.
3. **Cerebrospinal Fluid**: Protects and cushions the brain.

By clustering the pixel intensities of the grayscale image, we can group similar tissues based on their statistical properties.

---

### 📂 Workflow
1. **Image Loading**:
   The MRI image is loaded using the `skimage` library.

2. **Preprocessing**:
   - The image is converted to grayscale to simplify processing.
   - The grayscale image is reshaped into a 1D array for clustering.

3. **Clustering with Gaussian Mixture Model (GMM)**:
   - The GMM is used to identify three distinct clusters in the image, corresponding to the Gray Matter, White Matter, and Cerebrospinal Fluid.
   - The GMM assumes that pixel intensities follow a Gaussian distribution and segments the image by fitting a mixture of Gaussians.

4. **Segmentation**:
   - After clustering, the predicted labels are reshaped to the original image dimensions, creating the segmented image.

5. **Visualization**:
   - The original grayscale image and the segmented image are displayed side by side for comparison.

---

## 🚀 How to Run the Code

1. Install the necessary libraries:
   ```bash
   pip install numpy matplotlib scikit-learn scikit-image

## 🔧 What I Have Used in This Code

### Libraries:
- **numpy**: For numerical operations and array manipulation.
- **matplotlib**: For plotting and visualizing the images.
- **scikit-learn**: For implementing the Gaussian Mixture Model (GMM).
- **skimage**: For image loading and preprocessing.

### Techniques:
- **Gaussian Mixture Model (GMM)**: A statistical clustering technique that assumes data points are drawn from a mixture of multiple Gaussian distributions.
- **Image Processing**: Grayscale conversion and pixel intensity clustering.

---

## 🧬 Gaussian Mixture Model (GMM)

The **Gaussian Mixture Model (GMM)** captures the statistical properties of each tissue type (cluster) in the MRI image. It fits the data as a combination of multiple Gaussian distributions, each representing a specific tissue type.

### GMM Formula:
\[ 
p(x | \theta) = \sum_{k=1}^{K} \pi_k \cdot \phi(x | \mu_k, \Sigma_k) 
\]
Where:
- \( p(x | \theta) \): Probability of data point \( x \) given the model parameters \( \theta \).
- \( K \): Number of clusters (in this case, 3: Gray Matter, White Matter, and Cerebrospinal Fluid).
- \( \pi_k \): Weight of the \( k \)-th Gaussian (mixing coefficient).
- \( \phi(x | \mu_k, \Sigma_k) \): Gaussian distribution with mean \( \mu_k \) and covariance \( \Sigma_k \).

This formula models the intensity distribution of pixel values in the MRI image, allowing the segmentation of distinct brain tissues.

---

## ⚡ Applications

- **Medical Diagnosis**: Assisting in detecting abnormalities in brain structures.
- **Research**: Analyzing brain composition and function.
- **Image Processing**: Exploring segmentation techniques for various medical imaging tasks.

---
## 📊 Results

- **Original Image**: A grayscale representation of the MRI brain scan.
- **Segmented Image**: The brain tissues are clustered into three regions using distinct colors (Gray Matter, White Matter, Cerebrospinal Fluid).
-
![MRI Brain Scan](MRI_Brain_GE_Healthcare.jpg "MRI Brain Image")

