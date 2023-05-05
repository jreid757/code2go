#!/usr/bin/env python3.7

# Import os module
import os

# Create an empty list
my_list = []

# Set variable to get the current working directory
my_cwd = os.getcwd()

# Loop through all files in the current working directory
for file in os.listdir(my_cwd):

# Join the file name with the current working directory path
    file_path = os.path.join(file)
# Get the file stats for the file using 'os.stat()'
    file_stats = os.stat(file_path)
    
#  Append a new dictionary to 'my_list' with file path and size  
    my_list.append({'my_cwd':my_cwd+'/'+file, 'size': file_stats.st_size})
        
# Print the list of file details with newline separator
print(*my_list, sep="\n")