def main():
    # read the lemma file into a list separated by lines
    with open('AntBNC_lemmas_ver_001.txt') as file:
        content = file.readlines()

    # replace tabs with whitespace
    content = [x.replace('\t', ' ') for x in content]

    # remove whitespace characters
    content = [x.strip() for x in content]

    # create lemma dictionary
    lemma_dict = {}

    # put everything in a dictionary
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

    # for key, val in lemma_dict.items():
    #     print(key, val)

    # test word
    test_word = 'broken'
    print(lemma_dict.get(test_word))


if __name__ == "__main__":
    main()
