from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

def extract_colors(image_path, num_colors):
    image = Image.open(image_path)
    image = image.resize((600, 400))
    image_np = np.array(image)

    image_np = image_np.reshape((image_np.shape[0] * image_np.shape[1], 3))
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(image_np)

    colors = kmeans.cluster_centers_

    return colors

def plot_colors(colors):
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 1, 1)

    for i, color in enumerate(colors):
        plt.fill_betweenx([0, 1], i, i + 1, color=color / 255)

    plt.xlim(0, len(colors))
    plt.axis('off')
    plt.show()

def main():
    image_path = input("Enter the path of the image: ")
    num_colors = int(input("Enter the number of colors to extract: "))

    colors = extract_colors(image_path, num_colors)
    plot_colors(colors)

if __name__ == "__main__":
    main()
