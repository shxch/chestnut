import os
import string
from collections import OrderedDict

lemma_dict = {}
person = 'students/current_students/qichao_lin.txt'


def load_lemma_list(lemma_path):
    # read the lemma file into a list separated by lines
    with open(lemma_path) as file:
        content = file.readlines()

    # replace tabs with whitespace
    content = [x.replace('\t', ' ') for x in content]

    # remove whitespace characters
    content = [x.strip() for x in content]

    # put everything in the dictionary
    for x in content:
        # split ->
        t = x.split('->')
        post_lemma = t[0].strip()
        pre_lemma_string = t[1].strip()

        # split pre lemma words
        pre_lemma_words_list = pre_lemma_string.split()

        # add a dict pair
        for i in pre_lemma_words_list:
            lemma_dict[i] = post_lemma

    return lemma_dict


def read_text(path):
    word_tokens = []

    # if path is a file
    if os.path.isfile(path):
        file = open(path)
        word_tokens = file.read().split()

    # if path is a directory
    elif os.path.isdir(path):
        text_from_all_files = ""

        # gather every file in the directory
        for file in os.listdir(path):
            f = open(path + file, encoding='utf-8')
            text_from_all_files += f.read()
            word_tokens = text_from_all_files.split()

    return word_tokens


def remove_learned(text, path=person):
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
    # lower case all words
    lower_cased_words = [w.lower() for w in text]

    # remove numbers
    for w in lower_cased_words:
        if any(char.isdigit() for char in w):
            lower_cased_words.remove(w)
            # debug
            # print("removed: " + w)

    # trim punctuations
    trimmed_punctuations_words = []
    for w in lower_cased_words:

        # remove strings that only contain punctuations
        if all(char in string.punctuation for char in w):
            # debug
            # print("removed punctuations: " + w)
            w = ''
        # else trim punctuations
        else:
            while w[0] in string.punctuation:
                w = w[1:]
            while w[-1] in string.punctuation:
                w = w[:-1]

        # make sure w is not empty
        if w:
            trimmed_punctuations_words.append(w)

    # remove 's
    for w in trimmed_punctuations_words:
        if w.endswith("'s"):
            trimmed_punctuations_words.remove(w)
            trimmed_punctuations_words.append(w[:-2])

    # lemmatize all words
    result = []
    for w in trimmed_punctuations_words:

        if w in lemma_dict:
            result.append(lemma_dict[w])
        else:
            result.append(w)

    return result


def print_ordered_words(words):
    word_freq = get_word_frequency()
    ordered_words = {}
    for w in words:
        if w in word_freq:
            ordered_words[w] = word_freq[w]
        else:
            ordered_words[w] = 1

    with open(person, 'a') as f:

        for w in sorted(ordered_words, key=ordered_words.get, reverse=True):
            # print(w + "," + str(ordered_words[w]))
            print(w)
            f.write(w + "\n")


def add_to_learned(text):
    with open(person, 'a') as f:
        for w in text:
            f.write(w + "\n")


def write_to_file(content, path):
    with open(path, 'w') as f:
        f.write(content)


def sort_dict_by_value(unsorted_dict):
    sorted_dict = OrderedDict(sorted(unsorted_dict.items(), key=lambda t: t[1], reverse=True))
    return sorted_dict


def count_words(text):
    word_count = {}

    for word in text:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] = word_count[word] + 1

    return word_count


def main():
    global lemma_dict
    lemma_dict = load_lemma_list('AntBNC_lemmas_ver_001.txt')

    all_words = read_text("files_to_add/")
    all_words = normalize_words(all_words)
    all_words = set(all_words)

    all_words = remove_learned(all_words)

    print_ordered_words(all_words)

    # print("\n", len(all_words))


if __name__ == "__main__":
    main()
