cipher = "Zl qbt'f anzr vf Srgpu"

for i in range(26):
    result = ""

    for c in cipher:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') + i) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') + i) % 26 + ord('A'))
        else:
            result += c

    print(f"{i:2d}: {result}")
