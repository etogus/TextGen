import random

import nltk

file_name = input()
file = open(file_name, "r", encoding="utf-8")

data = file.read()
tokens = data.split()

tri_grams = list(nltk.trigrams(tokens))

tg_dict = {}

for head1, head2, tail in tri_grams:
    tg_dict.setdefault(head1 + " " + head2, []).append(tail)

text_size = 0
sentence_size = 0
sentence = ""

while text_size < 10:
    if sentence_size >= 5 and sentence.strip().endswith(tuple(['.', '!', '?'])):
        print(sentence)
        sentence_size = 0
        text_size += 1
        sentence = ""
    head = random.choices(list(tg_dict.keys()))[0]
    while head.split()[0].endswith((tuple(['.', '!', '?']))) or (not head[0].isupper() and sentence_size == 0) or sentence_size == 0 and head.endswith(tuple(['.', '!', '?'])) or (sentence_size == 0 and head.startswith(tuple(['.', '!', '?', '-', ' ', '"']))):
        head = random.choices(list(tg_dict.keys()))[0]
    tails = nltk.Counter(tg_dict[head])
    if sentence_size == 0:
        sentence = sentence + head + " "
        sentence_size += 2
    while True:
        if len(tails.keys()) == 0 or (sentence_size >= 5 and sentence.rstrip().endswith(tuple(['.', '!', '?']))):
            break
        random_word = tails.most_common(1)[0][0]
        sentence = sentence + random_word + " "
        sentence_size += 1
        head = sentence.split()[-2] + " " + sentence.split()[-1]
        tails = nltk.Counter(tg_dict[head])
