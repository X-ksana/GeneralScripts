### This is to facilitate checking dependencies of ML/DL tasks running for HPC

### Version 1: Using manual key-in
### python checkDepend.py package1 package2 package3

### Version 2: Using requirements.txt
### python checkDepend.py requirements /path/to/requirements.txt

# --------------------------------------------------------------------------------
# Import 
import os
import sys


# Function to read requirements.txt and extract package names
def read_requirements(requirements_file):
  packages = []
  with open(requirements_file, "r") as f:
    for line in f:
      # Remove whitespace and split  on "=="
      package_name = line.strip().split("==")[0]
      packages.append(package_name)
  return packages

# Function to check for missing dependencies
def check_dependencies(packages):
  missing_dependencies = []
  for package in packages:
    try:
      __import__(package)
    except ImportError:
      missing_dependencies.append(package)
  return missing_dependencies

# Main 
def main():
  if len(sys.argv) >1 and sys.argv[1] == 'requirements':
    # Use requirements.txt
    if len(sys.argv) != 3:
      print("Error: Please specify the path to requirements.txt.")
      return
    if not os.path.exists(requirements_file):
      print("Error: requirements.txt file not found!")
      return
  else:
    # Manually enter package names
    packages = syst.argv[1:]

  missing_dependencies = check_dependencies(packages)

  if missing_dependencies:
    print("The following dependencies are missing and need to be installed:")
    for dep in missing_dependencies:
      print(dep)
  else:
    print("All specified dependencies are available.")

if __name__== "__main__":
  main()


    
