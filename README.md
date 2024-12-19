# create-dicom-dwi-B0-overview
This script creates a bitmap overview of all the B0 volumes of man DWI MRI datasets



# this script:
#################
# - runs through a parent folder that contains subfolders with DWI Dicom data
# - uses dcmdump to identify the B0 volumes (install dcmdump: sudo apt install dcmtk)
# - takes a sagittal slice of each B0  volume of a specified position (sagIdx)
# - creates a bmp overview of all sagittal slices next to each other
# - labels all overviews and puts them together vertically to a big bmp overview 

# python scripts used: 
#   extract_slice_from_dcm_to_bmp_arg.py 
#   (python libraries required: os, numpy, PIL, argparse)
#   merge_bmp_files_line_and_label.py
#   (libraries required: os, PIL)
#
# input: 
#   - rootPath: is the parent folder, which contains  subfolders,  of which each contains (only) the DWI dicom files (numVols = numFiles)
#   - destPath: where the data is written (needs to have a '/' in the end)
#   - scriptPath: where the script is (needs to have a '/' in the end)
#   - sagittal slice index: sagIdx
#
# output: 
#   - individual bmp overviews (filenames are input folder names) and labelled big bmp overview oview.bmp in destPath
#
# how to run the script: bash ./extract_slice_from_dcm (needs to run explcitly with 'bash')
#
# When looking at the bmp overviews, be aware that many image viewer automatically smoowth the images
