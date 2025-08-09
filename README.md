# DisttibutedSystemProjects
Projects on various concepts of Distributed systems


# 1.Bank Transfer Service with Non-Idempotent Operations
A bank transfer is non-idempotent:
Transfer ₹100 twice = ₹200 gone (not safe if a retry happens accidentally).

We must design a system to track and prevent accidental replays.
Key Features:
- REST API that accepts a transaction_id, from_account, to_account, amount.
- Server stores processed transaction_ids in a deduplication cache (Redis or Python set).
- If a duplicate transaction_id arrives, the request is ignored.


 # 2. Message Queue with Deduplication
Simulate a distributed messaging system where:
- Messages might be redelivered due to network retries.
- Deduplication ensures the consumer processes each message only once.

Key Features:
- Producer sends messages with unique message_id.
- Consumer keeps a local store of processed IDs.
- Duplicate messages are discarded before processing.

- **Non-idempotent → The action changes state in a way that can’t be repeated safely (bank transfer, file append).**
- **Deduplication → Tracking transaction_id or message_id ensures we don’t accidentally apply the same change twice.**

# 3. Synchronous System Project – "Ping-Pong Game Server"
Concept:
- In a synchronous system, nodes operate in lockstep, and messages have known fixed delays.
- Both sides wait for the other before proceeding.

Idea:
1. Two players (clients) send "ping" and "pong" to each other via a server.
2. Server waits for both players' moves in each round before sending results back.

Key Point: The round only finishes when both players’ actions are received.

# 4. Asynchronous System Project – "Chat Without Guarantees"
- Concept: No assumptions about message delivery time — messages can be delayed or arrive out of order.
- Idea: A chat simulator where messages from users may arrive in random order and with random delays.

# 5. Stateless System Project – "Currency Converter API"
Concept:
- Stateless system doesn’t remember previous requests.
- Each request is independent and carries all necessary data.

Idea:A simple Flask API that converts currency without storing anything between calls.

Key Point: No session, no stored history — each call computes based on parameters only.

# 6. Stateful System Project – "To-Do List API"
Concept:
- Stateful system remembers previous interactions.
- Server stores data and changes over time.

Idea: Flask API to store and manage a user's to-do list in memory.

Key Point: The server retains the list in tasks across requests — client state depends on prior interactions.

<img width="1059" height="402" alt="image" src="https://github.com/user-attachments/assets/3f055222-e614-4fa0-8491-15ee91d8183f" />
