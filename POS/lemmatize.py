import nltk
from nltk.stem import WordNetLemmatizer 
import re
import stanza
import pandas as pd
# nltk.download('wordnet')
# stanza.download('en')


def join_punctuation(seq, characters='.,;?!'):
    characters = set(characters)
    seq = iter(seq)
    current = next(seq)

    for nxt in seq:
        if nxt in characters:
            current += nxt
        else:
            yield current
            current = nxt

    yield current


data = pd.read_csv("../data/flattened_paragraphs.csv", index_col=None)
raw_sentences = data["sentence"].to_list()
sentence_id = data["sentence ID"].to_list()
paragraph_id = data["paragraphID"].to_list()


# lemmatize first
lemmatizer = WordNetLemmatizer() 
nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma')

sentences = []

l = len(raw_sentences)
i = 1
for s in raw_sentences:
    print(i/l)
    stanza_lemmatized_word_list = []
    double_lemmatized_word_list = []

    doc = nlp(s)
    for sent in doc.sentences:
        for w in sent.words:
            stanza_lemmatized_word_list.append(w.lemma)

    for w in stanza_lemmatized_word_list:
        double_lemmatized_word_list.append(lemmatizer.lemmatize(w))

    sentences.append(" ".join(join_punctuation(double_lemmatized_word_list)))
    i += 1

df = pd.DataFrame(sentences)
df.columns = ["sentence"]
df["sentence ID"] = sentence_id
df["paragraphID" ] = paragraph_id

df.to_csv("../data/lemmatized_sentences.csv")
