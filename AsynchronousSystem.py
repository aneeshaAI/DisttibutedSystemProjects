import threading, time, random

messages = []

def send_message(user, content):
    delay = random.uniform(0.1, 2.0)
    time.sleep(delay)
    messages.append((time.time(), user, content))

def chat_simulator():
    users = ["Alice", "Bob"]
    threads = []
    for i in range(5):
        user = random.choice(users)
        content = f"Message {i} from {user}"
        t = threading.Thread(target=send_message, args=(user, content))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Messages received (unordered):")
    for msg in messages:
        print(msg)

if __name__ == "__main__":
    chat_simulator()
