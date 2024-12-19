import os
import numpy as np
import pydicom
from PIL import Image
import argparse

def extract_and_save_sagittal_view(dicom_dir, volume_indices, sagittal_slice_idx, output_file):
    """
    Extracts sagittal views from specified volumes in a DICOM dataset and saves them in a row as a BMP file.

    Parameters:
    - dicom_dir (str): Path to the directory containing DICOM files.
    - volume_indices (list): Indices of the volumes to extract sagittal views from.
    - sagittal_slice_idx (int): The index of the sagittal slice to extract.
    - output_file (str): The name of the output BMP file.
    """
    # Load all DICOM files from the directory
    dicom_files = [os.path.join(dicom_dir, f) for f in os.listdir(dicom_dir)]
    dicom_files.sort()  # Ensure consistent ordering

    # Read the dataset (assuming all volumes are stored as separate files in the directory)
    volumes = [pydicom.dcmread(f).pixel_array for f in dicom_files]
    print(f"Loaded {len(volumes)} volumes.")

    # Extract specified volumes
    selected_slices = []
    for idx in volume_indices:
        if idx >= len(volumes):
            raise ValueError(f"Volume index {idx} is out of range. Dataset has {len(volumes)} volumes.")
        volume = volumes[idx]
        sagittal_slice = volume[:, :, sagittal_slice_idx]  # Extract the sagittal slice
        selected_slices.append(sagittal_slice)

    # Normalize and flip each slice by 180 degrees
    normalized_slices = [
        np.rot90(((s - np.min(s)) / (np.max(s) - np.min(s)) * 255).astype(np.uint8), k=2)
        for s in selected_slices
    ]
    combined_image = np.hstack(normalized_slices)

    # Save the result as a BMP file
    img = Image.fromarray(combined_image)
    img.save(output_file)
    print(f"Sagittal views saved to {output_file}")

# Main script using argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract and save sagittal views from a DICOM dataset.")
    parser.add_argument("dicom_dir", type=str, help="Path to the directory containing DICOM files.")
    parser.add_argument("output_file", type=str, help="Path and name of the output BMP file.")
    parser.add_argument("--sagittal_slice_idx", type=int, default=64, help="Sagittal slice index (default: 64).")
    parser.add_argument("--volume_indices", type=str, help="Space-separated list of volume indices (e.g., '0 17 34 51 68').")

    args = parser.parse_args()

    # Convert the space-separated string into a list of integers
    if args.volume_indices:
        volume_indices = [int(x) for x in args.volume_indices.split()]
    else:
        volume_indices = []

    # Pass command-line arguments and the parsed volume indices to the function
    extract_and_save_sagittal_view(
        dicom_dir=args.dicom_dir,
        volume_indices=volume_indices,
        sagittal_slice_idx=args.sagittal_slice_idx,
        output_file=args.output_file,
    )
