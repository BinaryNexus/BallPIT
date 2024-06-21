from PIL import Image, ImageDraw
import numpy as np
from scipy.ndimage import label, find_objects
import cv2
import os

def count_and_circle(image_path, output_path):
    # Open image
    image = Image.open(image_path).convert('RGB')
    
    # Convert image to numpy array
    np_image = np.array(image)
    
    # Create a mask of pixels within the target range (looks for any pixel from 50% grey to pure white - originally looked for any non-black pixels, but this was prone to miscounts)
    target_mask = (
        (np_image[:, :, 0] >= 128) & (np_image[:, :, 0] <= 255) &
        (np_image[:, :, 1] >= 128) & (np_image[:, :, 1] <= 255) &
        (np_image[:, :, 2] >= 128) & (np_image[:, :, 2] <= 255)
    )
    
    # Label connected regions
    labeled_array, num_features = label(target_mask)
    
    # Find bounding boxes of labeled regions
    objects = find_objects(labeled_array)
    
    # Draw circles around the target areas
    for obj_slice in objects:
        # Find the center of the bounding box
        y_center = (obj_slice[0].start + obj_slice[0].stop) // 2
        x_center = (obj_slice[1].start + obj_slice[1].stop) // 2
        
        # Find the radius as half the diagonal of the bounding box
        height = obj_slice[0].stop - obj_slice[0].start
        width = obj_slice[1].stop - obj_slice[1].start
        radius = int(((height ** 2 + width ** 2) ** 0.5) // 2)
        
        # Draw a circle on the image
        cv2.circle(np_image, (x_center, y_center), radius, (255, 0, 0), 2)
    
    # Convert back to PIL Image and save the output
    output_image = Image.fromarray(np_image)
    output_image.save(output_path)
    
    return num_features

# Variables

# Get the input filename from the user
input_filename = input("Enter the image filename: ")
if not input_filename.lower().endswith('.png'):
    input_filename += '.png'

# Create the output filename by prepending "counted_" to the input filename
output_filename = os.path.join(os.path.dirname(input_filename), 'counted_' + os.path.basename(input_filename))

# Process the image and count the target areas
num_target_areas = count_and_circle(input_filename, output_filename)
print(f'Number of balls: {num_target_areas}')
print(f'Output saved to: {output_filename}')