# OS_Course_2026

**Name:** [Ezequiel-junior VARELA MONTEIRO]
**Student ID:** ST64049

## Practical Assignments
This repository contains the practical assignments for the Operating Systems module 2026.

### Assignment 1: Environment Setup & Basic System Info
- **Objective:** Get comfortable with the development environment and extract basic OS-level information.
- **Status:** Completed
- **File:** `sys_info.py`

### Assignment 2: File System Interaction
- **Objective:** Understand how the OS manages files, directories, and metadata.
- **Status:** Completed
- **File:** `file_system.py`

**Report & Justification:**
To interact with the Linux file system, I wrote a Python script utilizing standard OS libraries:
1.  **`os.listdir(path)`**: I chose this function because it efficiently retrieves a list of all entries (files and directories) contained within the specified path. 
2.  **`os.path.isfile(path)`**: Used to filter the entries so that we only process standard files, as requested by the assignment.
3.  **`os.stat(path)`**: This is the core system call used to extract file metadata. It returns a `stat_result` object.
    *   I accessed the `st_size` attribute to get the exact file size in bytes.
    *   I accessed the `st_mode` attribute to retrieve the raw permission bits.
4.  **`stat.filemode(mode)`**: I used this utility function to convert the raw `st_mode` integer into a human-readable POSIX permission string (e.g., `-rw-r--r--`), which clearly shows the read/write/execute permissions.

**Proof of Execution (Console Output):**
<img width="1287" height="519" alt="image" src="https://github.com/user-attachments/assets/8e9019f9-0254-4e85-83d2-0518e40530fb" />


# Assignment 3: Process Creation & IPC

**Objective:** Learn how to create processes and establish Inter-Process Communication (IPC).
**File:** `ipc_process.py`

## Report & IPC Justification

For this task, I implemented the inter-process communication using a **Pipe** (`multiprocessing.Pipe`). 

**Why a Pipe?**
A Pipe is the most appropriate IPC mechanism for this specific scenario because:
1. **1-to-1 Communication:** The architecture consists of exactly two processes (one Parent, one Child). Pipes are perfectly optimized for direct, point-to-point communication.

2. **Bi-directional Capability:** In Python, `multiprocessing.Pipe()` provides a duplex (two-way) connection by default. This perfectly matches the requirement where the parent sends data, and the child sends a response back over the same channel.

3. **Overhead efficiency:** While OS Shared Memory (as seen in Lab 03) is excellent for massive data structures like 500MB matrices to avoid the "Pickle penalty", using a simple Pipe is much more memory-efficient and straightforward for transferring small strings. A Queue would also be unnecessarily complex here, as Queues are designed for multi-producer/multi-consumer thread/process safety, which is not needed for a strict 1-to-1 parent-child exchange.

## Proof of Execution

<img width="1036" height="313" alt="image" src="https://github.com/user-attachments/assets/68ffe3ea-5908-4358-93e0-e9204a4fcae6" />

# Assignment 4: Threads & Synchronization

**Objective:** Understand concurrency, race conditions, and synchronization primitives.
**Status:** Completed
**File:** `threads_sync.py`

## Report: Concurrency Reflection

**1. What is a Race Condition? (Based on Part 1)**
From observing the output of my code in Part 1, a race condition occurs when multiple threads try to access and modify the same shared data (`counter_race`) at the exact same time without any coordination. 
Even though `counter += 1` looks like a single instruction, the CPU processes it in three separate steps: 
1. Read the current value.
2. Add 1.
3. Write the new value back.
When threads run concurrently, these steps overlap. Thread A might read the value, but before it can write the update, Thread B reads the *old* value. They both end up writing the exact same updated number, causing one increment to be completely lost. This is why the final counter was much lower than the expected 4,000,000.

**2. How the Mutex Solved the Problem (Based on Part 2)**
A Mutex (Mutual Exclusion) acts like a key to a locked room. By putting the `with mutex:` statement around the increment operation, I created a "critical section". 
Now, when Thread A wants to increment the counter, it takes the lock. If Thread B arrives at the same time, it sees the lock is taken and is forced to wait until Thread A finishes the entire read-add-write process and releases the lock. This ensures the shared variable is modified by only one thread at a time, resulting in zero data loss and achieving the perfect 4,000,000 result.

## Proof of Execution
<img width="957" height="290" alt="image" src="https://github.com/user-attachments/assets/34a71bb7-1ccb-4285-99a4-f50dddf733fb" />
