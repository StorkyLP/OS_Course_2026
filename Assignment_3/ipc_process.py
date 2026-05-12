import os
import multiprocessing

def child_process_task(conn):
    """
    This function runs in the child process.
    It receives data, transforms it, and sends it back.
    """
    # os.getpid() gets the Process ID of the current process (the child)
    child_pid = os.getpid()
    
    print(f"Child  [PID {child_pid}] waiting for data from parent...")
    
    # 1. Receive data from the pipe
    data_received = conn.recv()
    print(f"Child  [PID {child_pid}] received data: '{data_received}'")
    
    # 2. Transform the data (convert to UPPERCASE)
    print(f"Child  [PID {child_pid}] processing (converting to uppercase)...")
    transformed_data = data_received.upper()
    
    # 3. Send the transformed data back to the parent
    print(f"Child  [PID {child_pid}] sending transformed data back...")
    conn.send(transformed_data)
    
    # Close the child's end of the pipe
    conn.close()

def main():
    # os.getpid() gets the Process ID of the main program (the parent)
    parent_pid = os.getpid()
    print(f"Parent [PID {parent_pid}] starting execution.")

    # Create a Pipe for two-way communication.
    # It returns two connection objects: one for each end of the pipe.
    parent_conn, child_conn = multiprocessing.Pipe()

    # Create the child process. We target our function and pass the child's connection.
    child_process = multiprocessing.Process(target=child_process_task, args=(child_conn,))
    
    # Start the child process
    child_process.start()
    
    # The data we want to send
    original_string = "hello operating systems class!"
    
    # 1. Parent sends data to the child via its end of the pipe
    print(f"Parent [PID {parent_pid}] sending data: '{original_string}'")
    parent_conn.send(original_string)
    
    # 2. Parent waits to receive the response from the child
    print(f"Parent [PID {parent_pid}] waiting for response...")
    final_result = parent_conn.recv()
    print(f"Parent [PID {parent_pid}] received final result: '{final_result}'")
    
    # Wait for the child process to completely finish before exiting
    child_process.join()
    print(f"Parent [PID {parent_pid}] execution finished.")

if __name__ == "__main__":
    main()