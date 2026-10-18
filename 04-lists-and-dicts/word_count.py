import sys
from pathlib import Path

SAMPLE = """the quick brown fox jumps over the lazy dog
the dog sleeps and the fox runs"""


def count_words(text):
    counts = {}
    for word in text.lower().split():
        word = word.strip(".,!?\"'")
        if not word:
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_words(counts, n=3):
    # most common first, ties alphabetical so the output is stable
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ordered[:n]


def main():
    text = Path(sys.argv[1]).read_text() if len(sys.argv) > 1 else SAMPLE
    counts = count_words(text)
    print(f"{len(counts)} different words")
    for word, n in top_words(counts, 5):
        print(f"{word:<10} {n}")


if __name__ == "__main__":
    main()
