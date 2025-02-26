import os
import matplotlib.pyplot as plt
from os.path import join
from util.img_util import readImageFile, saveImageFile
from util.inpaint_util import removeHair


def process_images(input_folder, output_folder=None, display=False):
    """Process images in a folder, applying hair removal and optionally displaying results."""
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff")):
            image_path = join(input_folder, filename)
            
            # Read image
            img_rgb, img_gray = readImageFile(image_path)
            if img_rgb is None or img_gray is None:
                print(f"Error loading: {filename}")
                continue
            
            #Save Image

            # Apply hair removal
            blackhat, thresh, img_out = removeHair(img_rgb, img_gray)

            # Display images with matplotlib
            if display:
                plt.figure(figsize=(15, 10))

                plt.subplot(2, 2, 1)
                plt.imshow(img_rgb)
                plt.title("Original Image")
                plt.axis("off")

                plt.subplot(2, 2, 2)
                plt.imshow(blackhat, cmap="gray")
                plt.title("BlackHat Image")
                plt.axis("off")

                plt.subplot(2, 2, 3)
                plt.imshow(thresh, cmap="gray")
                plt.title("Thresholded Mask")
                plt.axis("off")

                plt.subplot(2, 2, 4)
                plt.imshow(img_out)
                plt.title("Inpainted Image")
                plt.axis("off")

                plt.tight_layout()
                plt.show()

if __name__ == "__main__":
    input_folder = "data"
    output_folder = "processed_data"  # Set to None if saving is not needed
    process_images(input_folder, output_folder, display=True)  # Set display=False to disable visualization
