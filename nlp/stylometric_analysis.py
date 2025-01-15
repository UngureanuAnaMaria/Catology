import string
import re
from collections import Counter
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from colorama import Fore, Style
from detect_language import detect_language
from find_language import find_language


def is_word(word: str):
    return any(c.isalpha() for c in word)


def stylometric_analysis(text):
    """
    Extracts and prints stylometric characteristics of the given text.

    Parameters:
        text (str): The input text to analyze.
    """
    print(f"{Fore.LIGHTGREEN_EX}\nStylometric characteristics:\n{Style.RESET_ALL}")

    # Tokenize text into words and sentences
    words = word_tokenize(text)
    print(f"Words in the text:")
    for i in range(0, len(words), 15):
        print(f"['{"', '".join([f'{Fore.BLUE}{word}{Style.RESET_ALL}' for word in words[i:i + 15]])}']")
    words_without_punctuation = [word for word in words if is_word(word)]
    # words = [word.lower() for word in words if re.match(r"^[a-zA-Z'-]+$", word)]
    sentences = sent_tokenize(text)

    # Frequency of words without punctuation (including common words)
    word_freq = Counter(words_without_punctuation)
    print(f"\nFrequency of words without punctuation (including common words):")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

    # Frequency of words without punctuation (excluding common words)
    abbreviation, probability = detect_language(text)
    language = find_language(abbreviation)
    stopwords = set(nltk.corpus.stopwords.words(language))
    filtered_words = [word for word in words_without_punctuation if word not in stopwords]
    filtered_word_freq = Counter(filtered_words)
    print(f"\nFrequency of words without punctuation (excluding common words):")
    for word, freq in filtered_word_freq.items():
        print(f"{word}: {freq}")
    print("\n")

    # Count of words
    word_count = len(words)
    print(f"{word_count=}")

    # Count of words without punctuation
    words_without_punctuation_count = len(words_without_punctuation)
    print(f"{words_without_punctuation_count=}")

    # Count of punctuations
    punctuation_count = sum(1 for char in text if char in string.punctuation)
    print(f"{punctuation_count=}")

    # Count of characters
    char_count = len(text)
    print(f"{char_count=}")

    # Lexical features
    # Type-token ratio (TTR) = unique words / total words.
    ttr = len(set(words_without_punctuation)) / len(words_without_punctuation)
    print(f"{ttr=}")

    # Most common words
    freq_dist = FreqDist(words_without_punctuation)
    print(f"Top 5 most common words: {freq_dist.most_common(5)}")

    # Average word length
    avg_word_length = sum(len(word) for word in words_without_punctuation) / len(words_without_punctuation)
    print(f"{avg_word_length=}")

    # hapax legomena: Count of words that occur only once in the text
    hapax_legomena = [word for word, count in freq_dist.items() if count == 1]
    print(f"hapax_legomena={hapax_legomena[:5]}")

    # hapax dislegomena: Count of words that occur exactly twice in the text
    hapax_dislegomena = [word for word, count in freq_dist.items() if count == 2]
    print(f"hapax_dislegomena={hapax_dislegomena[:5]}")

    # Syntactic features
    # Average sentence length
    avg_sentence_length = sum(len(word_tokenize(sent)) for sent in sentences) / len(sentences)
    print(f"{avg_sentence_length=}")
