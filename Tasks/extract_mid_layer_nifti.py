# For extracting mid layer.
# How to use: python3 extract_mid_layer_nifti.py /path/to/data name_of_dataset
# Example: python3 extract_mid_layer_nifti.py /home/username/Downloads/brats2020/TrainingData/ name_of_dataset
# Please beware that patient data should be in the following format:
# /path/to/data/patient_id/patient_id_frame01.nii.gz <-  Can recode based on requirements


# Import dependencies
import os
import numpy as np
import torch
import nibabel as nib

from monai.transforms import Compose

from monai.transforms import (
    LoadImaged,
    Spacingd,
    Orientationd,
    CropForegroundd,
    ToTensord,
)

from monai.data import ImageDataset
import matplotlib.pyplot as plt
import sys

### Define data directory
# Define paths
data_dir = sys.argv[1]  # Replace with your path
dataset_name = sys.argv[2] # Replace with your dataset name
output_dir = "extracted_{dataset_name}"

# Check if the directory exists, and create it if it doesn't
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Now you can use `output_dir` for further operations
print(f"Directory '{output_dir}' is ready!")
# output_dir = "extracted_images"

# Define MONAI transforms to load both image and label
transforms = Compose([
    LoadImaged(keys=["image", "label"]),  # Load both image and label
    Spacingd(keys=["image", "label"], pixdim=(1.5, 1.5, 2.0), mode=("bilinear","nearest")),
    Orientationd(keys=["image", "label"], axcodes="RAI"),
    CropForegroundd(keys=["image", "label"], source_key="image"),
    ToTensord(keys=["image", "label"])
])

# Read and process each patient's data
for patient_folder in os.listdir(data_dir):
    patient_id = patient_folder.split("_")[-1]  # Extract patient ID from folder name
    patient_data_dir = os.path.join(data_dir, patient_folder)
    image_file = os.path.join(patient_data_dir, f"{patient_folder}_frame01.nii.gz")
    label_file = os.path.join(patient_data_dir, f"{patient_folder}_frame01_gt.nii.gz")

    # Load image and label using MONAI transforms
    data = transforms({"image": image_file, "label": label_file})

    # Get the mid slice of Z-axis for image
    z_mid = data["image"].shape[2] // 2
    mid_slice_image_transverse_np = data["image"][:,:,z_mid].numpy()
    mid_slice_image_transverse_np = mid_slice_image_transverse_np.astype(np.float32)

    # Get the mid slice of Z-axis for label
    mid_slice_image_transverse_np = data["label"][:,:,z_mid].numpy()
    mid_slice_image_transverse_np = mid_slice_label_transverse_np.astype(np.float32)
    

    # This section for nifti file, alternative method will be to save the image straight without nifti being generated
    # Save extracted images
    os.makedirs(output_dir, exist_ok=True)
    nib.save(nib.Nifti1Image(mid_slice_image_transverse_np, affine=np.eye(4)),
             os.path.join(output_dir, f"patient_{patient_id}_mid_slice_image_transverse.nii.gz"))
    nib.save(nib.Nifti1Image(mid_slice_label_transverse_np, affine=np.eye(4)),
             os.path.join(output_dir, f"patient_{patient_id}_mid_slice_label_transverse.nii.gz"))

  #  print(f"Processed and saved data for patient {patient_id}")

print("All data processed and saved!")
