# Assignment 2: File System Interaction

- **Objective:** Understand how the OS manages files, directories, and metadata.
- **Status:** Completed
- **File:** `file_system.py`

## Report & Justification
To interact with the Linux file system, I wrote a Python script utilizing standard OS libraries:
1.  **`os.listdir(path)`**: I chose this function because it efficiently retrieves a list of all entries (files and directories) contained within the specified path. 
2.  **`os.path.isfile(path)`**: Used to filter the entries so that we only process standard files, as requested by the assignment.
3.  **`os.stat(path)`**: This is the core system call used to extract file metadata. It returns a `stat_result` object.
    * I accessed the `st_size` attribute to get the exact file size in bytes.
    * I accessed the `st_mode` attribute to retrieve the raw permission bits.
4.  **`stat.filemode(mode)`**: I used this utility function to convert the raw `st_mode` integer into a human-readable POSIX permission string (e.g., `-rw-r--r--`), which clearly shows the read/write/execute permissions.

## Proof of Execution (Console Output)
<img width="1287" height="519" alt="image" src="https://github.com/user-attachments/assets/8e9019f9-0254-4e85-83d2-0518e40530fb" />