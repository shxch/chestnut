import os
import re
from pathlib import Path


def read_lemma_dict(lemma_dict_file_path):
    # read the lemma file into a list separated by lines
    with open(lemma_dict_file_path) as file:
        content = file.readlines()

    # replace tabs with whitespace
    content = [x.replace('\t', ' ') for x in content]

    # remove whitespace characters
    content = [x.strip() for x in content]

    # put everything in the dictionary
    lemma_dict = dict()
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


def read_files_from_paths(paths):
    files = []

    for path in paths:
        files += read_files_from_path(path)

    return files


def read_words_from_files(files):
    words = []

    # ensure files list is not empty
    if files:

        text_from_all_files = ''

        for file in files:
            text_from_all_files += file.read() + '\n'

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


def remove_learned_words(text, person_file_path):
    learned_words = read_words_from_path(person_file_path)
    result = []
    for w in text:
        if w not in learned_words:
            result.append(w)
    return result


def get_word_frequency(word_freq_file_path):
    word_freq = {}
    for line in open(word_freq_file_path):
        word, freq = line.split(",")
        word_freq[word] = int(freq)
    return word_freq


def lemmatize_words(lemma_dict, text):
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


def add_to_learned(words, person_file_path):
    with open(person_file_path, 'a') as f:
        for w in words:
            f.write(w + "\n")


def get_words_sorted_by_freq(words, word_freq_file_path):
    word_freq = get_word_frequency(word_freq_file_path)
    sorted_words = {}
    for w in words:
        if w in word_freq:
            sorted_words[w] = word_freq[w]
        else:
            sorted_words[w] = 1

    ret = []
    for w in sorted(sorted_words, key=sorted_words.get, reverse=True):
        ret.append(w)
    return ret


def standardize_words(lemma_dict, words):
    words = remove_non_alpha_chars(words)
    words = lemmatize_words(lemma_dict, words)
    words = set(words)

    return words


def get_new_words(student_file_path, passage_files_paths, output_mode):
    word_freq_file_path = '../google-books-common-words.txt'
    lemma_dict = read_lemma_dict('../AntBNC_lemmas_ver_001.txt')

    new_files = read_files_from_paths(passage_files_paths)

    if output_mode == 'cumulative':
        new_words = read_words_from_files(new_files)
        new_words = standardize_words(lemma_dict, new_words)
        new_words = remove_learned_words(new_words, student_file_path)
        sorted_words = get_words_sorted_by_freq(new_words, word_freq_file_path)
        add_to_learned(sorted_words, student_file_path)
        return sorted_words

    elif output_mode == 'separate':

        ret = []
        for f in new_files:
            new_words = f.read().split()
            new_words = standardize_words(lemma_dict, new_words)
            new_words = remove_learned_words(new_words, student_file_path)
            sorted_words = get_words_sorted_by_freq(new_words, word_freq_file_path)
            add_to_learned(sorted_words, student_file_path)

            ret.append(' ')
            ret.append(Path(f.name).stem)
            ret += sorted_words
        return ret


def main():
    new_file_dir_path = '../new_files/'
    student_file_path = '../students/test/miniming'
    output_mode = "separate"

    get_new_words(student_file_path, [new_file_dir_path], output_mode)


if __name__ == "__main__":
    main()
