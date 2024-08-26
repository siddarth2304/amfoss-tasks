import os
import cv2
import numpy as np
from PIL import Image, ImageDraw

def load_and_sort_images(folder_path):
    images = []
    filenames = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')],
                       key=lambda x: int(x.split(' ')[1].split('.')[0]))
    
    for filename in filenames:
        img_path = os.path.join(folder_path, filename)
        image = cv2.imread(img_path)
        images.append((filename, image))
    
    return images

def is_white_image(image):
    # Check if the image is completely white
    return np.all(image == [255, 255, 255])

def detect_dot(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        contour = max(contours, key=cv2.contourArea)
        moments = cv2.moments(contour)
        if moments['m00'] != 0:
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])
            color = image[cy, cx]
            return (cx, cy), tuple(color)
    return None, None

def draw_lines(images, output_path):
    width = 512 * len(images)
    base_image = Image.new('RGB', (width, 512), color='white')
    draw = ImageDraw.Draw(base_image)
    
    prev_dot = None
    for filename, img in images:
        if is_white_image(img):
            prev_dot = None  # Reset previous dot on line break
            continue
        
        dot, color = detect_dot(img)
        if dot:
            if prev_dot:
                if color:
                    draw.line([prev_dot, dot], fill=color, width=2)
            prev_dot = dot
        else:
            prev_dot = None
    
    base_image.save(output_path)

if __name__ == "__main__":
    folder_path = '/home/sahith-siddarth/Operation_Pixel_Merge/assets'  # Absolute path to the assets folder
    output_path = '/home/sahith-siddarth/Operation_Pixel_Merge/stitched_output.png'  # Absolute path for output file
    
    images = load_and_sort_images(folder_path)
    draw_lines(images, output_path)

