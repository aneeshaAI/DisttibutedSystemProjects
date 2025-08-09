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
