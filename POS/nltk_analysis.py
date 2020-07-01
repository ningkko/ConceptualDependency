import nltk
import pandas as pd
import json
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

data = pd.read_csv("../data/flattened_paragraphs.csv", index_col=None)
raw_sentences = data["sentence"].to_list()

verb_dict = {}
# for sentence in sentences:
all_words_dict = {}
# for storing each type of word
pos_dict = {}

verb_pos = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]

l = len(raw_sentences)

i = 0
for s in raw_sentences:
    print(i/l)
    tokens = nltk.word_tokenize(s)
    doc = nltk.pos_tag(tokens)

    #[("word","pos")]
    for text in doc:
        # print(text)
        # print(type(text))
        pos = text[1]
        text = text[0]
        if text not in pos_dict:
            pos_dict[pos] = [text]
        else:
            pos_dict[pos].append(text)

        # if no word yet, add an empty frame
        if text not in all_words_dict:
            all_words_dict[text] = {"word_count":1}
        # else update count
        else:
            all_words_dict[text]["word_count"] += 1

        # all data to the frame
        if pos not in all_words_dict[text]:
            all_words_dict[text][pos] = 1
        else:
            all_words_dict[text][pos] += 1

        # create a verb dict
        if str(pos) in verb_pos:
            if text in verb_dict:
                verb_dict[text] += 1
            else:
                verb_dict[text] = 1
    i+=1

with open('pos_words_nltk.json', 'w') as fp:
    json.dump(str(pos_dict), fp, indent=4)

with open('verbs_nltk.json', 'w') as fp:
    json.dump(str(verb_dict), fp, indent=4)

with open('words_nltk.json', 'w') as fp:
    json.dump(str(all_words_dict), fp, indent=4)

