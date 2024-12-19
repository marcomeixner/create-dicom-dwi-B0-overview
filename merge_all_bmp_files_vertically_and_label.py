import os
from PIL import Image, ImageDraw, ImageFont

def merge_bmp_images_vertically(input_folder, output_file):
    """
    Merges all BMP files in the input folder into a single vertically stacked image.
    Each image will have a running number and its filename (without extension) written in the upper-left corner.

    Parameters:
    - input_folder: Path to the folder containing BMP files.
    - output_file: Path to save the output image.
    """
    # List all BMP files in the input directory
    bmp_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.bmp')]
    
    if not bmp_files:
        print("No BMP files found in the specified directory.")
        return

    # Sort the BMP files for consistent order
    bmp_files.sort()

    # Open all BMP images and add text to each
    images = []
    for i, bmp_file in enumerate(bmp_files, start=1):  # Start numbering from 1
        image_path = os.path.join(input_folder, bmp_file)
        img = Image.open(image_path)

        # Remove the file extension from the filename
        file_label = os.path.splitext(os.path.basename(bmp_file))[0]

        # Create a label with the running number
        label = f"{i}: {file_label}"

        # Draw the label onto the image
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()  # Default font; customize if needed
        draw.text((10, 10), label, font=font, fill="white")  # Draw text at (10, 10)

        images.append(img)

    # Calculate the total height and the maximum width for the combined image
    total_height = sum(img.height for img in images)
    max_width = max(img.width for img in images)

    # Create a blank canvas for the merged image
    result = Image.new("RGB", (max_width, total_height))

    # Paste each image into the canvas
    y_offset = 0
    for img in images:
        result.paste(img, (0, y_offset))
        y_offset += img.height

    # Save the final image
    result.save(output_file)
    print(f"Merged image saved to {output_file}")

# Main script
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python merge_bmp_vertically.py <input_folder> <output_file>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_file = sys.argv[2]
    merge_bmp_images_vertically(input_folder, output_file)
