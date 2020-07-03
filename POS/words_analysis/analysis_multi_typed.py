import json

with open('../dictionaries/lemmatized/words_nltk_multi_typed.json') as nltk:
    words_nltk_dict = json.load(nltk)
with open('../dictionaries/lemmatized/words_stanza_multi_typed.json') as stanza:
    words_stanza_dict = json.load(stanza)

nltk_words = words_nltk_dict.keys()
stanza_words = words_stanza_dict.keys()

## what are missing?
def find_diff(li1, li2):
    return list(set(li1) - set(li2))

words_diff = find_diff(list(nltk_words), list(stanza_words))
print(len(words_diff))
with open("diff_words_lemmatized.txt", "w") as f:
    f.write("\n".join(words_diff))
