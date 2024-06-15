import os
import re
import shutil

def clean_name(name):
    """Remove numbers and dashes from the name and replace with spaces"""
    name_without_numbers = re.sub(r'\d', '', name)
    name_with_spaces = re.sub(r'[-]', ' ', name_without_numbers)
    return name_with_spaces.strip()

def organize_files(directory):
    """Organize files into folders based on cleaned names"""
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    for filename in os.listdir(directory):
        # Skip directories
        if os.path.isdir(os.path.join(directory, filename)):
            continue
        
        # Extract the base name without extension
        basename, ext = os.path.splitext(filename)
        
        # Clean the name to remove numbers and dashes
        folder_name = clean_name(basename)
        
        # Create the folder path
        folder_path = os.path.join(directory, folder_name)
        
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Move the file into the folder
        shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))
        print(f"Moved {filename} to {folder_path}")

def remove_files(directory):
    """Remove files from folders and place them back into the main directory"""
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            # Move the file back to the main directory
            shutil.move(file_path, os.path.join(directory, filename))
            print(f"Moved {filename} back to {directory}")
        
    # After moving all files, remove empty directories
    remove_empty_folders(directory)

def remove_empty_folders(directory):
    """Remove empty folders from the directory"""
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    for foldername in os.listdir(directory):
        folder_path = os.path.join(directory, foldername)
        if os.path.isdir(folder_path) and not os.listdir(folder_path):
            os.rmdir(folder_path)
            print(f"Removed empty folder {folder_path}")
    return
  

def mainPrompt(directory):
    """Prompt the user to choose an option"""
    while True:
        print("What would you like to do?")
        print("1. Add files to directories")
        print("2. Remove files from directories")
        print("3. Remove empty directories")
        print("4. Enter a new directory path")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            organize_files(directory)
        elif choice == "2":
            remove_files(directory)
        elif choice == "3":
            remove_empty_folders(directory)
        elif choice == "4":
            startPrompt()
        elif choice == "5":
            break
        else:
            print("Invalid choice")
    
def startPrompt():
    """Prompt the user to enter the directory path"""
    directory = input("Please enter the path to the directory you want to organize: ")
    print(f"Organizing files in {directory}")
    mainPrompt(directory)

if __name__ == "__main__":
    # Prompt the user to enter the directory path
    startPrompt()
