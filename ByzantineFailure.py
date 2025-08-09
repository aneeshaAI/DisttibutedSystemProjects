import random

def normal_node():
    return "Hello from normal node"

def byzantine_node():
    behaviors = [
        "Corrupt message",
        "Wrong timestamp: 2099-12-31",
        "False claim: Node2 failed",
        "Random junk: " + str(random.randint(1000, 9999))
    ]
    return random.choice(behaviors)

for _ in range(5):
    print("[Normal]", normal_node())
    print("[Byzantine]", byzantine_node())
