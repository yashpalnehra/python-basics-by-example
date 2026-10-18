import sys


def shift_char(ch, shift):
    if ch.isascii() and ch.isalpha():
        base = "a" if ch.islower() else "A"
        return chr((ord(ch) - ord(base) + shift) % 26 + ord(base))
    # digits, spaces and punctuation pass through
    return ch


def encode(text, shift):
    return "".join(shift_char(ch, shift) for ch in text)


def decode(text, shift):
    return encode(text, -shift)


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in ("encode", "decode"):
        print("usage: caesar.py encode|decode SHIFT TEXT")
        sys.exit(1)
    action, shift, text = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    print(encode(text, shift) if action == "encode" else decode(text, shift))


if __name__ == "__main__":
    main()
