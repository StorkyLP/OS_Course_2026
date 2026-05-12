# Assignment 4: Threads & Synchronization

- **Objective:** Understand concurrency, race conditions, and synchronization primitives.
- **Status:** Completed
- **File:** `threads_sync.py`

## Report: Concurrency & Synchronization

**1. What is a Race Condition?**
A race condition occurs when multiple threads read and write to a shared variable concurrently without coordination. In Python, due to the Global Interpreter Lock (GIL), true parallel execution of bytecodes doesn't happen. To physically demonstrate the race condition, I had to force a context switch using `time.sleep(0)` right after reading the variable. This forces the thread to yield the CPU, allowing another thread to read the exact same old value. When both threads write their incremented values back, one increment is overwritten and lost forever. 

**2. How the Mutex Solved the Problem:**
A Mutex (Mutual Exclusion) acts as a lock. By wrapping the increment logic inside a `with mutex:` block, I created a "critical section". Even though I kept the `time.sleep(0)` inside Part 2 to force the thread to yield the CPU, the lock prevents any other thread from entering the critical section. The other threads are forced to wait until the first thread wakes up, finishes the addition, and releases the lock. This ensures absolute data integrity.

## Proof of Execution
<img width="1221" height="476" alt="image" src="https://github.com/user-attachments/assets/d94a86e2-4fd5-4a3f-91cf-1ae5649d3c97" />
