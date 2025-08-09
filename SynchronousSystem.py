# Ping-Pong Game Server
import time

def synchronous_round(player1, player2):
    print("[Round Start]")
    time.sleep(1)  # Simulate known fixed delay
    move1 = player1()
    move2 = player2()
    print(f"Player1: {move1}, Player2: {move2}")
    print("[Round End]")

if __name__ == "__main__":
    synchronous_round(lambda: "Ping", lambda: "Pong")
    synchronous_round(lambda: "Ping", lambda: "Ping")

# Key Point: The round only finishes when both players’ actions are received.
