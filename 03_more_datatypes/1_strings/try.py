def find_longest_word(words_list):
    print(words_list)
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
        print(word_len)
    word_len.sort()
    print(word_len)
    return word_len[-1][1]

print(find_longest_word(["PHP", "Exercises", "Backend"]))