import nltk
import os
from nltk.stem import WordNetLemmatizer


def alpha_lower(text):
    result = []
    for word in text:
        if word.isalpha():
            result += [word.lower()]
    return result


def lemmatize(text):
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatized_text = []
    for word in text:
        # first lemmatize the word to verb
        lemmatized_word = wordnet_lemmatizer.lemmatize(word, "v")
        # if it cannot be lemmatized to verb, lemmatize it to noun
        if word == lemmatized_word:
            noun = wordnet_lemmatizer.lemmatize(word, "n")
            lemmatized_text += [noun]
        else:
            lemmatized_text += [lemmatized_word]
    return lemmatized_text


path = "test2"
ordered_words = {}
for file in os.listdir(path):
    f = open(path + "/" + file, 'r', encoding='utf-8')
    passage_text = nltk.word_tokenize(f.read())

    # normalize all words
    standard_text = alpha_lower(passage_text)
    standard_text = lemmatize(standard_text)

    # delete duplicates
    word_set = set(standard_text)

    for word in word_set:
        if word in ordered_words:
            ordered_words[word] += 1
        else:
            ordered_words[word] = 1

minimum_frequency = 1
for w in sorted(ordered_words, key=ordered_words.get, reverse=True):
    if ordered_words[w] >= minimum_frequency:
        print(w + "," + str(ordered_words[w]))
        # print(w)
