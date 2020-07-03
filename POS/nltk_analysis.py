import nltk
import pandas as pd
import json
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

data = pd.read_csv("../data/flattened_paragraphs.csv", index_col=None)
raw_sentences = data["sentence"].to_list()
sentence_id = data["sentence ID"].to_list()
paragraph_id = data["paragraphID"].to_list()

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
        word = text[0]

        if pos not in pos_dict:
            pos_dict[pos] = {word: str(paragraph_id[i])+","+str(sentence_id[i]) }
        else:
            if word not in pos_dict[pos]:
                pos_dict[pos][word] =  str(paragraph_id[i])+","+str(sentence_id[i]) 
            else:
                pos_dict[pos][word] = pos_dict[pos][word] + "|"+str(paragraph_id[i])+","+str(sentence_id[i]) 

        # if no word yet, add an empty frame
        if word not in all_words_dict:
            all_words_dict[word] = {"word_count": 1}
        # else update count
        else:
            all_words_dict[word]["word_count"] += 1

        # all data to the frame
        if pos not in all_words_dict[word]:
            # name_of_pos : {"count": 1,
            #                "id": paragraph_id,sentence_id|paragraph_id,sentence_id
            all_words_dict[word][pos] = {"count": 1,
                                         "id": str(paragraph_id[i])+","+str(sentence_id[i])}
        else:
            all_words_dict[word][pos]["count"] += 1
            all_words_dict[word][pos]["id"] = all_words_dict[word][pos]["id"] + "|"+str(paragraph_id[i])+","+str(sentence_id[i])

        # create a verb dict

        if str(pos) in verb_pos:
            if word in verb_dict:
                verb_dict[word]["count"] += 1
                verb_dict[word]["id"] = verb_dict[word]["id"] + "|"+str(paragraph_id[i])+","+str(sentence_id[i])

            else:
                verb_dict[word] = {"count":1,
                                   "id": str(paragraph_id[i])+","+str(sentence_id[i])}
    i+=1

with open('dictionaries/pos_words_nltk.json', 'w') as fp:
    json.dump(pos_dict, fp, indent=4)

with open('dictionaries/verbs_nltk.json', 'w') as fp:
    json.dump(verb_dict, fp, indent=4)

with open('dictionaries/words_nltk.json', 'w') as fp:
    json.dump(all_words_dict, fp, indent=4)

