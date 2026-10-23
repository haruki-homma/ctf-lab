plain = open("relay-heartbeat.json", "rb").read().rstrip(b"\r\n")
cipher = open("relay-heartbeat.enc", "rb").read()
target = open("relay-tasking.enc", "rb").read()

keystream = bytes(
    p ^ c for p, c in zip(plain, cipher)
)

decoded = bytes(
    c ^ k for c, k in zip(target, keystream)
)

print(decoded.decode("utf-8"))