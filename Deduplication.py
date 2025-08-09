import uuid
import queue
import time
import random

# In-memory message queue
message_queue = queue.Queue()
processed_messages = set()

# Producer: sends messages, sometimes duplicates
def producer():
    for i in range(5):
        msg_id = str(uuid.uuid4())
        message = {"id": msg_id, "content": f"Message {i}"}
        message_queue.put(message)
        
        # Simulate accidental duplicate send
        if random.random() < 0.3:
            print(f"[Producer] Sending duplicate: {msg_id}")
            message_queue.put(message)
        
        time.sleep(0.5)

# Consumer: processes messages only once
def consumer():
    while True:
        try:
            message = message_queue.get(timeout=3)
        except queue.Empty:
            break
        
        if message["id"] in processed_messages:
            print(f"[Consumer] Duplicate detected: {message['id']}")
            continue
        
        # Non-idempotent operation: Append to file (can’t safely repeat)
        with open("processed.txt", "a") as f:
            f.write(message["content"] + "\n")
        
        processed_messages.add(message["id"])
        print(f"[Consumer] Processed: {message}")
        time.sleep(0.2)

if __name__ == "__main__":
    producer()
    consumer()
