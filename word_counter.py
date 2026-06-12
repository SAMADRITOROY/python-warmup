
with open('pride.txt', 'r', encoding='utf-8') as file:
    text = file.read()
text_in_lowercase = text.lower()
words = text_in_lowercase.split()
words_with_count = {}
for word in words:
    words_with_count[word] = words_with_count.get(word, 0) + 1
sorted_words_by_count = sorted(words_with_count.items(), key=lambda item: item[1], reverse=True)
print(sorted_words_by_count[:20])
