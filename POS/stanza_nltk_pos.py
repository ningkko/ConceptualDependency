import stanza
import nltk
import pandas as pd
import json

data = pd.read_csv("../data/flattened_paragraphs.csv", index_col=None)
raw_sentences = data["sentence"].to_list()
sentence_id = data["sentence ID"].to_list()
paragraph_id = data["paragraphID"].to_list()

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# stanza.download('en')

# initialize stanza nlp pipeline
nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos')
# sentence - paragrapg ID
#          - sentence ID
#          - NLTK pos
#          - Stanza pos

l = len(raw_sentences)
sentences_dict = {}

i = 0
for s in raw_sentences:
    print(i/l)

    cur_dict = {"paragraph_id": paragraph_id[i],
                "sentence_id": sentence_id[i]}

    # ------------- stanza pos -------------
    stanza_pos = []
    doc = nlp(s)
    for sent in doc.sentences:
        for word in sent.words:
            stanza_pos.append(word.upos)

    cur_dict["stanza"] = stanza_pos

    # ------------- nltk pos -------------
    nltk_pos = []
    tokens = nltk.word_tokenize(s)
    doc = nltk.pos_tag(tokens)
    for word in doc:
        pos = word[1]
        nltk_pos.append(pos)

    cur_dict["nltk"] = nltk_pos

    if s not in sentences_dict:
        sentences_dict[s] = [cur_dict]
    else:
        sentences_dict[s].append(cur_dict)

    i+=1

with open('dictionaries/stanza_nltk_pos_comparison.json', 'w') as fp:
    json.dump(sentences_dict, fp, indent=4)

