import os

# Specify the directory path
directory_path = "/users"  # Replace with your desired path

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of", directory_path)
for item in contents:
    print(item)
