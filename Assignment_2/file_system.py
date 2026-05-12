import os
import sys
import stat

def list_files_info(directory_path):
    """
    Iterates through a given directory and retrieves the size
    and permissions of all files inside it.
    """
    # Verify if the provided path exists and is indeed a directory
    if not os.path.exists(directory_path):
        print(f"Error: The path '{directory_path}' does not exist.")
        return
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        return

    print(f"Scanning directory: {directory_path}\n")
    print(f"{'File Name':<30} | {'Size (bytes)':<15} | {'Permissions'}")
    print("-" * 65)

    try:
        # os.listdir() returns a list containing the names of the entries in the directory.
        for item in os.listdir(directory_path):
            # We need the absolute path to use os.stat()
            full_path = os.path.join(directory_path, item)
            
            # The assignment specifies to list all *files* inside it
            if os.path.isfile(full_path):
                # os.stat() performs a stat system call on the given path to get metadata
                file_stats = os.stat(full_path)
                
                # st_size gives the size of the file in bytes
                file_size = file_stats.st_size
                
                # st_mode contains the file type and permissions.
                # stat.filemode() converts this into a readable 'rwxrwxrwx' string format.
                file_permissions = stat.filemode(file_stats.st_mode)
                
                print(f"{item:<30} | {file_size:<15} | {file_permissions}")
                
    except PermissionError:
        print(f"Error: Permission denied. You don't have the rights to read '{directory_path}'.")

if __name__ == "__main__":
    # Accept directory path as a command-line argument, or ask for input
    if len(sys.argv) > 1:
        target_directory = sys.argv[1]
    else:
        target_directory = input("Enter a directory path (or press Enter for current directory '.'): ")
        if not target_directory.strip():
            target_directory = "."
            
    list_files_info(target_directory)
