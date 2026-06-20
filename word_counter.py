import csv


def count_top_n_words(text, n):
    text_in_lowercase = text.lower()
    words = text_in_lowercase.split()
    words_with_count = {}
    for word in words:
        words_with_count[word] = words_with_count.get(word, 0) + 1
    sorted_words_by_count = sorted(
        words_with_count.items(), key=lambda item: (-item[1], item[0])
    )
    return sorted_words_by_count[:n]


def main():
    with open("pride.txt", "r", encoding="utf-8") as file:
        text = file.read()

    top_20_words = count_top_n_words(text, 20)

    with open("pride_word_counted.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        writer.writerows(top_20_words)


if __name__ == "__main__":
    main()
