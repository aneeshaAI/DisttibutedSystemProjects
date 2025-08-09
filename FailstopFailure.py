import time, threading

alive_nodes = {"node1": True, "node2": True}

def heartbeat(node):
    while alive_nodes[node]:
        print(f"[Heartbeat] {node} is alive")
        time.sleep(1)

def coordinator():
    while True:
        for node, alive in alive_nodes.items():
            if not alive:
                print(f"[Coordinator] {node} has fail-stopped")
        time.sleep(2)

if __name__ == "__main__":
    threading.Thread(target=heartbeat, args=("node1",), daemon=True).start()
    threading.Thread(target=heartbeat, args=("node2",), daemon=True).start()
    threading.Thread(target=coordinator, daemon=True).start()

    time.sleep(4)
    alive_nodes["node2"] = False  # Simulate fail-stop
    time.sleep(10)
