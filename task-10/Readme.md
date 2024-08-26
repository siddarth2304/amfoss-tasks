
## Operation Pixel Merge

### Overview

In this task, we stitch together fragmented images to reveal a secret message. Each image contains a single colored dot on a white background. The goal is to connect these dots in the correct sequence to form a coherent image, using Python with OpenCV and Pillow libraries.

### Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd Operation_Pixel_Merge
   ```

2. **Set Up the Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install opencv-python numpy Pillow
   ```

### Running the Script

1. **Prepare Images:**

   Place your images in the `assets` folder. Ensure that images are named sequentially (e.g., `Layer 1.png`, `Layer 2.png`, ...).

2. **Execute the Script:**

   ```bash
   python scripts/pixel_merge.py
   ```

3. **Check the Output:**

   The stitched image will be saved as `stitched_output.png` in the `Operation_Pixel_Merge` directory.

### Troubleshooting

- **File Not Found:** Ensure that the paths in the script are correct and the images are located in the `assets` folder.
- **White Image Issues:** Verify that white images are correctly recognized as line breaks.

---
