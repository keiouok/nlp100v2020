def n_gram(target, i):
    return [target[idx:idx + n] for idx in range(len(target) - (n - 1))]

text = "I am an NLPer"
for n in range(1, 4):
    char_ans = n_gram(text, n)
    word_ans = n_gram(text.split(" "), n)
    print("N = ", n)
    print("char_ans:", char_ans)
    print("word_ans:", word_ans)


