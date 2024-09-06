# Import the necessary modules to access operating system
import os

# Define a function to group files by their extensions
def group_files_by_extension(directory):
    # Create a dictionary to store files by their extensions
    files_by_extension = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]

        # If the extension is not already in the dictionary, add it
        if file_extension not in files_by_extension:
            files_by_extension[file_extension] = []

        # Add the file to the list of files with the same extension
        files_by_extension[file_extension].append(filename)

    # Print the files grouped by their extensions
    for extension, files in files_by_extension.items():
        print(f"Files with extension {extension}:")
        for file in files:
            print(f"- {file}")

# Ask the user for the directory to group files in
directory = input("Enter the directory path: ")

# Check if the directory exists
if not os.path.exists(directory):
    print("Invalid directory. Please try again.")
else:
    # Call the function to group files by their extensions
    group_files_by_extension(directory)