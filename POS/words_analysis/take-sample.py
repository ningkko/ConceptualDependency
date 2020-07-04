# From the multi-pos lists, randomly choose 10%
import json
import random

# stanza
with open('../dictionaries/lemmatized/words_stanza_multi_typed.json') as nltk:
    words_stanza_dict = json.load(nltk)
    sample_keys = random.sample(list(words_stanza_dict), int(0.1*len(words_stanza_dict.keys())))
    sample = {}
    for key in sample_keys:
        sample[key] = words_stanza_dict[key]

    sample = dict(sorted(sample.items(), key=lambda x: x[0].lower()))

with open('stanza_sample.json', 'w') as fp:
    json.dump(sample, fp, indent=4)


# nltk
with open('../dictionaries/lemmatized/words_nltk_multi_typed.json') as nltk:
    words_nltk_dict = json.load(nltk)
    sample_keys = random.sample(list(words_nltk_dict), int(0.1*len(words_nltk_dict.keys())))
    sample = {}
    for key in sample_keys:
        sample[key] = words_nltk_dict[key]

    sample = dict(sorted(sample.items(), key=lambda x: x[0].lower()))


with open('sample.json', 'w') as fp:
    json.dump(sample, fp, indent=4)
