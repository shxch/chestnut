import os


def read_text(path):
    text = []
    if os.path.isfile(path):
        file = open(path)
        # text = nltk.word_tokenize(file.read())
    elif os.path.isdir(path):
        all = ""
        for file in os.listdir(path):
            f = open(path + file, encoding='utf-8')
            all += f.read()
            # text = nltk.word_tokenize(all)
    return text


def remove_learned(text, path="learned.txt"):
    learned_words = read_text(path)
    result = []
    for w in text:
        if w not in learned_words:
            result.append(w)
    return result


def get_word_frequency(path="word_frequency.csv"):
    word_freq = {}
    for line in open(path):
        word, freq = line.split(",")
        word_freq[word] = int(freq)
    return word_freq


def normalize_words(text):
    # lower case
    temp = [w.lower() for w in text if w.isalpha()]

    # lemmatize all words
    # wordnet_lemmatizer = WordNetLemmatizer()
    result = []
    # for w in temp:
    # lemmatized_word = wordnet_lemmatizer.lemmatize(w, "v")
        # if it cannot be lemmatized to verb, lemmatize it to noun
    # if w == lemmatized_word:
    # noun = wordnet_lemmatizer.lemmatize(w, "n")
    # result += [noun]
    # else:
    # result += [lemmatized_word]
    return result


def print_ordered_words(words):
    word_freq = get_word_frequency()
    ordered_words = {}
    for w in words:
        if w in word_freq:
            ordered_words[w] = word_freq[w]
            # print(w, word_freq[w])

    for w in sorted(ordered_words, key=ordered_words.get, reverse=True):
        # print(w + "," + str(ordered_words[w]))
        print(w)


def add_to_learned(text):
    with open('learned.txt', 'a') as f:
        for w in text:
            f.write(w + "\n")


def main():
    all_words = read_text("test1/")
    all_words = normalize_words(all_words)
    all_words = set(all_words)
    all_words = remove_learned(all_words)
    print_ordered_words(all_words)
    print("\n", len(all_words))

    # add_to_learned(all_words)


if __name__ == "__main__":
    main()
