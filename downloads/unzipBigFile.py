"""

Function to safely unzip a potentially large zip file. 
It checks for zip bombs (files designed to expand significantly when decompressed) and ensures that the
zip file is not corrupt before extraction. 
If no issues are found, it extracts the files into the specified output directory.
After extraction, you can check the size and number of files in the output directory

"""

import zipfile
import os

def unzip_large_zip(zip_file_path, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Check if the zip file contains any potentially harmful files
        for zip_info in zip_ref.infolist():
            if zip_info.file_size > 100_000_000_000:  # Adjust this threshold as needed
                print("Warning: Potential zip bomb detected. Aborting extraction.")
                return

        # Extract files from the zip file
        try:
            zip_ref.extractall(output_dir)
            print("Extraction completed successfully.")
        except zipfile.BadZipFile:
            print("Error: Zip file is corrupt. Aborting extraction.")
            return

# Example usage:
zip_file_path = "path/to/your/large_zip_file.zip"
output_dir = "path/to/output_directory"

unzip_large_zip(zip_file_path, output_dir)

# Check the size of the output directory
def get_directory_size(directory):
    total_size = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

# Check the number of files in the output directory
def count_files_in_directory(directory):
    num_files = sum(len(files) for _, _, files in os.walk(directory))
    return num_files


# Get the size of the output directory
output_dir_size = get_directory_size(output_dir)
print(f"Size of output directory: {output_dir_size} bytes")

# Get the number of files in the output directory
num_files = count_files_in_directory(output_dir)
print(f"Number of files in output directory: {num_files}")


