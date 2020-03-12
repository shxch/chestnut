import os
import re
from collections import OrderedDict

# read mode
read_mode = "cumulative"

# file paths
new_files_path = '../new_files/'
lemma_dict_file_path = '../AntBNC_lemmas_ver_001.txt'
word_frequency_file_path = '../google-books-common-words.txt'
person = '../students/current_students/cheng_ye.txt'

# global variables
lemma_dict = dict()


def load_lemma_dict(path=lemma_dict_file_path):
    # read the lemma file into a list separated by lines
    with open(path) as file:
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


def read_files_from_path(path):
    files = []

    # if path is a file
    if os.path.isfile(path):
        f = open(path, encoding='utf-8')
        files.append(f)

    # if path is a directory
    elif os.path.isdir(path):

        # gather every file in the directory
        for file in os.listdir(path):
            f = open(path + file, encoding='utf-8')
            files.append(f)

    return files


def read_words_from_files(files):
    words = []

    # ensure files list is not empty
    if files:

        text_from_all_files = ''

        for f in files:
            text_from_all_files += f.read() + '\n'

        words = text_from_all_files.split()

    return words


def read_words_from_path(path):
    return read_words_from_files(read_files_from_path(path))


def remove_non_alpha_chars(words):
    alpha_only_words = ""

    for w in words:
        # remove soft hyphens
        w = re.sub('­', '', w)
        # replace non-alpha chars with spaces
        w = re.sub(r"[^A-Za-z]+", ' ', w)

        # add spaces between each word
        alpha_only_words += w + " "
    return alpha_only_words.split()


def remove_learned(text, path=person):
    learned_words = read_words_from_path(path)
    result = []
    for w in text:
        if w not in learned_words:
            result.append(w)
    return result


def get_word_frequency(path=word_frequency_file_path):
    word_freq = {}
    for line in open(path):
        word, freq = line.split(",")
        word_freq[word] = int(freq)
    return word_freq


def lemmatize_words(text):
    # lower case all words
    lower_cased_words = [w.lower() for w in text]

    # lemmatize all words
    result = []
    for w in lower_cased_words:

        if w in lemma_dict:
            result.append(lemma_dict[w])
        else:
            result.append(w)

    return result


def store_and_print_words_in_freq_order(words):
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


def write_to_file(content, path):
    with open(path, 'w') as f:
        f.write(content)


def sort_dict_by_value(unsorted_dict):
    sorted_dict = OrderedDict(sorted(unsorted_dict.items(), key=lambda t: t[1], reverse=True))
    return sorted_dict


def process_words(words):
    words = remove_non_alpha_chars(words)
    words = lemmatize_words(words)
    words = set(words)
    words = remove_learned(words)

    return words


def main():
    # load lemma dictionary
    load_lemma_dict()

    # print('person: ' + person)
    # print('files: ' + new_files_path)

    if read_mode == 'cumulative':
        words = read_words_from_path(new_files_path)

        words = process_words(words)

        store_and_print_words_in_freq_order(words)

    elif read_mode == 'separate':

        files = read_files_from_path(new_files_path)

        for f in files:
            words = f.read().split()

            words = process_words(words)

            print()
            print(f.name)
            store_and_print_words_in_freq_order(words)


if __name__ == "__main__":
    main()
