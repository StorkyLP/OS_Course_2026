import platform
import os
import getpass

def display_system_info():
    """
    Retrieves and prints basic system information including the OS name,
    kernel version, current user, and current working directory.
    """
    print("--- Basic System Information ---")
    
    # 1. Operating System name and kernel version
    # platform.system() returns the OS name (e.g., Linux, Windows)
    # platform.release() returns the system's release/kernel version
    os_name = platform.system()
    kernel_version = platform.release()
    print(f"OS Name: {os_name}")
    print(f"Kernel Version: {kernel_version}")
    
    # 2. Current logged-in user
    # getpass.getuser() is used here as it is more robust in cloud 
    # environments (like Colab or Killercoda) compared to os.getlogin()
    current_user = getpass.getuser()
    print(f"Current User: {current_user}")
    
    # 3. Current working directory
    # os.getcwd() retrieves the directory from which the script is executed
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}")
    print("-" * 32)

if __name__ == "__main__":
    display_system_info()
