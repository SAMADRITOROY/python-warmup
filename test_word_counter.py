from word_counter import count_top_n_words  

def test_count_top_n_words():
    text = "hello world hello everyone"
    expected = [('hello', 2), ('everyone', 1), ('world', 1)]
    assert count_top_n_words(text, 10) == expected

def test_count_top_n_words_with_punctuation():
    text = "Hello, world! Hello everyone!"
    expected = [('everyone!', 1), ('hello', 1), ('hello,', 1), ('world!', 1)]
    assert count_top_n_words(text, 10) == expected

def test_count_top_n_words_with_mixed_case():
    text = "Hello World! hello everyone."
    expected = [('hello', 2), ('everyone.', 1), ('world!', 1)]
    assert count_top_n_words(text, 10) == expected

def test_count_top_n_words_with_empty_string():
    text = ""
    expected = []
    assert count_top_n_words(text, 10) == expected

def test_count_top_n_words_with_n_greater_than_unique_words():
    text = "Hello world! Hello everyone."
    expected = [('hello', 2), ('everyone.', 1), ('world!', 1)]
    assert count_top_n_words(text, 5) == expected

def test_count_top_n_words_in_pride_with_n_less_than_unique_words():
    text = "Hello world! Hello everyone."
    expected = []
    assert count_top_n_words(text, 0) == expected

def test_count_top_n_words_in_pride_with_surrounding_whitespace():
    text = "  hello world hello everyone  "
    expected = [('hello', 2), ('everyone', 1), ('world', 1)]
    assert count_top_n_words(text, 10) == expected