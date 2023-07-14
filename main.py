import argparse


def find_unique_character(text):
    word_set = set()
    unique_chars = []

    for word in text.split():
        chars = list(word.lower())  # or list(word.lower())

        for char in chars:
            if chars.count(char) == 1:
                unique_chars.append(char)
                word_set.add(char)
                break

    for char in unique_chars:
        if unique_chars.count(char) == 1:
            return char

    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find the first unique character in a text')
    parser.add_argument('text', type=str, help='Text to analyze')

    args = parser.parse_args()
    result = find_unique_character(args.text)
    print("First unique symbol:", result)
