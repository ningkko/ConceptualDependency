import stanza
import pandas as pd
import json

data = pd.read_csv("../data/flattened_paragraphs.csv", index_col=None)
raw_sentences = data["sentence"].to_list()
# stanza.download('en')

nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos')
verb_dict = {}
# for sentence in sentences:
all_words_dict = {}
# for storing each type of word
pos_dict = {}

l = len(raw_sentences)

i = 0
for s in raw_sentences:
    print(i/l)
    doc = nlp(s)
    for sent in doc.sentences:
        for word in sent.words:
            if word.upos not in pos_dict:
                pos_dict[word.upos] = [word.text]
            else:
                pos_dict[word.upos].append(word.text)

            # if no word yet, add the frame
            if word.text not in all_words_dict:
                all_words_dict[word.text] = {"word_count":1,
                                            "upos": {},
                                            "xpos": {},
                                            "feats": {}}
            # else update count
            else:
                all_words_dict[word.text]["word_count"] += 1 

            # all data to the frame
            if word.upos not in all_words_dict[word.text]["upos"]:
                all_words_dict[word.text]["upos"][word.upos] = 1
            else:
                all_words_dict[word.text]["upos"][word.upos] += 1 

            if word.xpos not in all_words_dict[word.text]["xpos"]:
                all_words_dict[word.text]["xpos"][word.xpos] = 1
            else:
                all_words_dict[word.text]["xpos"][word.xpos] += 1 

            if word.feats not in all_words_dict[word.text]["feats"]:
                all_words_dict[word.text]["feats"][word.feats] = 1
            else:
                all_words_dict[word.text]["feats"][word.feats] += 1 


            if str(word.upos) == "VERB":
                if word in verb_dict:
                    verb_dict[word.text] += 1
                else:
                    verb_dict[word.text] = 1
    i+=1

with open('pos_words_stanza.json', 'w') as fp:
    json.dump(str(pos_dict), fp, indent=4)

with open('verbs_stanza.json', 'w') as fp:
    json.dump(str(verb_dict), fp, indent=4)

with open('words_stanza.json', 'w') as fp:
    json.dump(str(all_words_dict), fp, indent=4)

