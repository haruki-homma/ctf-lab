hex_data = "02362b2964302c2164372c25202b3337642b226417342127303621641021272c2a2b282b233d7e6420212520222527213f3c2b361b751b263d30771b70301b701b3075297739"

print(bytes.fromhex(hex_data).decode())

cipher = "02362b2964302c2164372c25202b3337642b226417342127303621641021272c2a2b282b233d7e6420212520222527213f3c2b361b751b263d30771b70301b701b3075297739"

data = bytes.fromhex(cipher)

for key in range(256):
    plaintext = bytes(b ^ key for b in data)
    if b"deadface{" in plaintext.lower():
        print(f"Key: 0x{key:02x}")
        print(plaintext.decode())