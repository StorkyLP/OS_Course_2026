# Assignment 3: Process Creation & IPC

- **Objective:** Learn how to create processes and establish Inter-Process Communication (IPC).
- **Status:** Completed
- **File:** `ipc_process.py`

## Report & IPC Justification

For this task, I implemented the inter-process communication using a **Pipe** (`multiprocessing.Pipe`). 

**Why a Pipe?**
A Pipe is the most appropriate IPC mechanism for this specific scenario because:
1. **1-to-1 Communication:** The architecture consists of exactly two processes (one Parent, one Child). Pipes are perfectly optimized for direct, point-to-point communication.
2. **Bi-directional Capability:** In Python, `multiprocessing.Pipe()` provides a duplex (two-way) connection by default. This perfectly matches the requirement where the parent sends data, and the child sends a response back over the same channel.
3. **Overhead efficiency:** While OS Shared Memory (as seen in Lab 03) is excellent for massive data structures like 500MB matrices to avoid the "Pickle penalty", using a simple Pipe is much more memory-efficient and straightforward for transferring small strings. A Queue would also be unnecessarily complex here, as Queues are designed for multi-producer/multi-consumer thread/process safety, which is not needed for a strict 1-to-1 parent-child exchange.

## Proof of Execution
<img width="1036" height="313" alt="image" src="https://github.com/user-attachments/assets/68ffe3ea-5908-4358-93e0-e9204a4fcae6" />