"""    
This project extracts the dominant colors from any image and creates a color palette.
It uses OpenCV to load the image and scikit-learn’s KMeans clustering to find the main colors.
This project will teach you about clustering algorithms and image processing while producing visually engaging results!

The program reads an image.jpg file.
After running the program, it should generate and display the color palette for the input image using matplotlib.

Required Libraries: opencv, numpy, scikit-learn, matplotlib
pip install opencv-python numpy scikit-learn matplotlib
"""
import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
    
def extract_colors(image_path, n_colors=5) -> np.ndarray:
    """Extracts dominant colors from an image using KMeans clustering."""

    # Load the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

    # Reshape the image to a 2D array of pixels
    pixels = image.reshape(-1, 3)

    # Apply KMeans clustering to find dominant colors
    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(pixels)

    # Get the cluster centers (dominant colors)
    colors = kmeans.cluster_centers_.astype(int)

    return colors

def plot_color_palette(colors):
    """Plots the color palette from the extracted colors."""
    palette = np.zeros((100, 500, 3), dtype=int)

    for i, color in enumerate(colors):
        palette[:, i * 100:(i + 1) * 100] = color

    plt.imshow(palette)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    """Main entry point for the color palette extractor."""
    image_path = './image.jpg'  # Path to the input image
    n_colors = 5  # Number of dominant colors to extract

    colors = extract_colors(image_path, n_colors)
    print("Extracted Colors (RGB):", colors)

    plot_color_palette(colors)