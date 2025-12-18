import os

def list_files_and_dirs(directory):
    try:
        # Get a list of all files and directories in the given directory
        files_and_dirs = os.listdir(directory)
        
        # Initialize two empty lists to store files and directories
        files = []
        dirs = []
        
        # Iterate over the list of files and directories
        for item in files_and_dirs:
            # Construct the full path of the item
            item_path = os.path.join(directory, item)
            
            # Check if the item is a file or a directory
            if os.path.isfile(item_path):
                # If it's a file, add it to the files list
                files.append(item)
            elif os.path.isdir(item_path):
                # If it's a directory, add it to the dirs list
                dirs.append(item)
        
        # Return the lists of files and directories
        return files, dirs
    
    except FileNotFoundError: #Raised if the given directory does not exist.
        print(f"The directory '{directory}' does not exist.")
        return None, None
    except PermissionError: #Raised if you do not have permission to access the given directory.
        print(f"You do not have permission to access the directory '{directory}'.")
        return None, None

def main():
    directory = input("Enter the directory path: ")
    files, dirs = list_files_and_dirs(directory)
    
    if files is not None and dirs is not None:
        print(f"Files in '{directory}':")
        for file in files:
            print(file)
        
        print(f"\nDirectories in '{directory}':")
        for dir in dirs:
            print(dir)

if __name__ == "__main__":
    main()

