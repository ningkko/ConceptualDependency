# Samples 10% of each POS tag type in dictionaries/words_nltk.json and dictionaries/words_stanza.json
# Before sampling, filter out ones with only 1 type pos, threshold -> appeared 3 times.
import pandas as pd
import json

# nltk
with open('../dictionaries/lemmatized/words_nltk.json') as nltk:
    words_nltk_dict = json.load(nltk)
    print(len(words_nltk_dict.keys()))
    new_word_dict = {key:val for key, val in words_nltk_dict.items() if not (val["word_count"]>=3 and len(val.keys())==2)}
    new_word_dict = dict( sorted(new_word_dict.items(), key=lambda x: x[0].lower()) )

with open('../dictionaries/lemmatized/words_nltk_multi_typed.json', 'w') as fp:
    json.dump(new_word_dict, fp, indent=4)

# stanza
with open('../dictionaries/lemmatized/words_stanza.json') as stanza:
    words_stanza_dict = json.load(stanza)
    print(len(words_stanza_dict.keys()))

    new_word_dict = {key:val for key, val in words_stanza_dict.items() if not (val["word_count"]>=3 and len(val.keys())==2)}
    new_word_dict = dict( sorted(new_word_dict.items(), key=lambda x: x[0].lower()) )

with open('../dictionaries/lemmatized/words_stanza_multi_typed.json', 'w') as fp:
    json.dump(new_word_dict, fp, indent=4)