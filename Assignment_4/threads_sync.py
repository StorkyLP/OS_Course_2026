import threading
import time

# Variable globale partagée
counter = 0

# Le Mutex (cadenas)
mutex = threading.Lock()

# Configuration (100 000 est suffisant sur Mac pour voir l'erreur rapidement)
num_threads = 4
increments_per_thread = 100000 
expected_total = num_threads * increments_per_thread

# --- PART 1: The Problem (No Synchronization) ---
def worker_without_lock():
    global counter
    for _ in range(increments_per_thread):
        temp = counter
        # Sur macOS, ceci force le processeur à céder sa place à un autre thread
        time.sleep(0) 
        counter = temp + 1

# --- PART 2: The Solution (With Mutex/Lock) ---
def worker_with_lock():
    global counter
    for _ in range(increments_per_thread):
        # Le Mutex empêche les collisions, même avec le sleep !
        with mutex:
            temp = counter
            time.sleep(0) 
            counter = temp + 1

def run_experiment(target_function, use_lock=False):
    global counter
    counter = 0 # On remet le compteur à zéro
    
    threads = []
    
    for i in range(num_threads):
        t = threading.Thread(target=target_function)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
        
    return counter

if __name__ == '__main__':
    print("\n=== Assignment 4: Threads & Synchronization ===")
    
    print("\n[Part 1] Running 4 threads WITHOUT synchronization...")
    print("Expected result :", expected_total)
    actual_unlocked = run_experiment(worker_without_lock)
    print("Actual result   :", actual_unlocked)
    print("Notice the missing increments due to the Race Condition!")
    
    print("\n[Part 2] Running 4 threads WITH a Mutex (Lock)...")
    print("(Please wait a few seconds, locks make execution safer but slightly slower)")
    print("Expected result :", expected_total)
    actual_locked = run_experiment(worker_with_lock, use_lock=True)
    print("Actual result   :", actual_locked)
    print("Success! The Mutex protected the shared variable.")
    print("===============================================\n")