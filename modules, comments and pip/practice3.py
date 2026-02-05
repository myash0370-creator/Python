#Write a python program to print the contents of a directory using the os module
import os

# Path of the directory
directory_path = "/"   # change this to your directory path

# Get list of files and folders
contents = os.listdir(directory_path)

# Print contents
print("Contents of the directory:")
for item in contents:
    print(item)
