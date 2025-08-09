import random, time

def flaky_server(request):
    if random.random() < 0.3:  # 30% omission
        return None
    return f"Processed {request}"

for i in range(10):
    resp = None
    while resp is None:
        resp = flaky_server(f"req-{i}")
        if resp is None:
            print(f"[Client] No response for req-{i}, retrying...")
            time.sleep(0.5)
    print(resp)
