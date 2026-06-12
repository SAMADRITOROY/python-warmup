
with open('pride.txt', 'r', encoding='utf-8') as file:
    text = file.read()
text_in_lowercase = text.lower()
words = text_in_lowercase.split()
words_with_count = {}
for word in set(words):
    count = words.count(word)
    words_with_count[word] = count
words_with_count_sorted_by_count_desc = sorted(words_with_count.items(), key=lambda item: item[1], reverse=True)
print(words_with_count_sorted_by_count_desc[:20])
