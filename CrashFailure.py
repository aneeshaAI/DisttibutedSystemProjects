import time
import threading
import queue

# Task queue between master and worker
task_queue = queue.Queue()
result_queue = queue.Queue()

# Worker state
worker_alive = True

def worker():
    """Worker that processes tasks until it crashes."""
    global worker_alive
    while worker_alive:
        try:
            task = task_queue.get(timeout=1)
        except queue.Empty:
            continue
        time.sleep(1)  # Simulate work
        result_queue.put(f"Task {task} processed")
    # After crash, worker stops processing entirely
    while True:
        time.sleep(1)  # Silent halt

def master():
    """Master sends tasks and detects worker crash."""
    consecutive_timeouts = 0
    for i in range(1, 8):
        task_queue.put(i)
        print(f"[Master] Sent task {i}")
        
        try:
            # Wait for worker response (timeout = 2s)
            result = result_queue.get(timeout=2)
            print(f"[Master] Received: {result}")
            consecutive_timeouts = 0  # Reset timeout counter
        except queue.Empty:
            consecutive_timeouts += 1
            print(f"[Master] No response for task {i} (timeout {consecutive_timeouts})")
        
        if consecutive_timeouts >= 3:
            print("[Master] Worker has crashed! Ta
