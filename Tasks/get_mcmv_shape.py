## Noted M&M1 datasets issue during extraction, to examine the shape of the image file first
## Not sure why some files cannot be opened by ITK software
## Not sure why some mid sliced mask has no segmentation information
## Usage: python generate_mcmv_shape.py <data_directory> <excel_name>

import os
import nibabel as nib
import pandas as pd

def generate_data_shape(data_dir, author_name):
    # Initialize lists to store information
    ids = []
    image_sizes = []
    smallest = []
    smallest_indices = []
    largest = []
    largest_indices = []
    has_similar_index = []
    data_type = []  # New list to store whether data is from image or label

    # Iterate through each subfolder in the data directory
    for subfolder in os.listdir(data_dir):
        subfolder_path = os.path.join(data_dir, subfolder)
        if not os.path.isdir(subfolder_path):
            continue
        
        # Extract ID from subfolder name
        current_id = subfolder

        # Iterate through each file in the subfolder
        for file in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, file)
            if file.endswith("_sa.nii.gz") or file.endswith("_sa_gt.nii.gz"):
                # Load NIfTI file
                img = nib.load(file_path)
                data = img.get_fdata()

                 # Append the ID with a suffix for images
                if file.endswith("_sa_gt.nii.gz"):
                  ids.append(f"{current_id}_label")
                  data_type.append("label")
                else: 
                  ids.append(f"{current_id}_image")
                  data_type.append("image")
                
                # Get image size
                size = list(data.shape)
                image_sizes.append(size)

                # Get the smallest and largest sizes
                small = min(size)
                small_index = size.index(min(size))
                large = max(size)
                large_index = size.index(max(size))

                # Append the smallest and largest indices to the lists
                smallest.append(small)
                largest.append(large)
                smallest_indices.append(small_index)
                largest_indices.append(large_index)
                
                # Check if index 0 and index 1 of image size are the same
                if size[0] == size[1]:
                    has_similar_index.append(True)
                else:
                    has_similar_index.append(False)
    
    # Create a DataFrame from the lists
    df = pd.DataFrame({
        'ID': ids,
        'Image Size': image_sizes,
        'Small': smallest,
        'Smallest Index': smallest_indices,
        'Largest': largest,
        'Largest Index': largest_indices,
        'Has Similar Index': has_similar_index,
        'Data Type': data_type
    })

    # Save the DataFrame to an Excel file
    output_file = f"image_info_{excel_name}.xlsx"
    df.to_excel(output_file, index=False)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python generate_data_shape.py <data_directory> <excel_name>")
        sys.exit(1)
    data_dir = sys.argv[1]
    excel_name = sys.argv[2]
    generate_data_shape(data_dir, excel_name)
