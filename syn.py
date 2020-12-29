# read in verbs

import pandas as pd
import json

df = pd.read_json('data/stanza_verbs.json')
verbs = list(df.columns)

import nltk
from nltk.stem import WordNetLemmatizer 
import re
import stanza
import pandas as pd
# nltk.download('wordnet')
# stanza.download('en')


# lemmatize first
lemmatizer = WordNetLemmatizer() 
nlp = stanza.Pipeline(lang='en', processors='pos,tokenize,lemma')
verbs_lemmatized = []
for v in verbs:
	vvv=[]
	doc = nlp(v)
	for sent in doc.sentences:
		for w in sent.words:
			vvv.append(w.lemma)

	verbs_lemmatized.append(lemmatizer.lemmatize(vvv[0]))

# print("\n".join(verbs_lemmatized))

with open("data/stanza_verbs.json",'r') as fp:
	d = json.load(fp)

values = [v for k,v in d.items()]
# print(len(verbs_lemmatized))
# print(len(values))
df=pd.DataFrame({"keys":verbs_lemmatized,
				"value":values})

df.to_csv("lemmatized_verbs.csv")



from nltk.corpus import wordnet

ddd={}

for v in verbs_lemmatized:
	if v not in ddd:
		synonyms = []
		antonyms = []
		for syn in wordnet.synsets(v):
			for l in syn.lemmas():
				synonyms.append(l.name())
				if l.antonyms():
					antonyms.append(l.antonyms()[0].name())
		synonyms = ", ".join(set(synonyms))
		antonyms = ", ".join(set(antonyms))
		ddd[v] = {"synonyms":synonyms,
				  "antonyms":antonyms}
				  
with open("syn_ant.json","w") as fp:
	json.dump(ddd,fp,indent=4)