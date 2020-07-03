import json

with open('dictionaries/words_nltk_multi_typed.json') as nltk:
    words_nltk_dict = json.load(nltk)
with open('dictionaries/words_stanza_multi_typed.json') as stanza:
    words_stanza_dict = json.load(stanza)

nltk_words = words_nltk_dict.keys()
stanza_words = words_stanza_dict.keys()

print(len(nltk_words))
## 2690
print(len(stanza_words))
## 2487


## what are missing?
def find_diff(li1, li2):
    return list(set(li1) - set(li2))


words_diff = find_diff(list(nltk_words), list(stanza_words))
with open("words_analysis/diff_words.txt", "w") as f:
    f.write("\n".join(words_diff))
