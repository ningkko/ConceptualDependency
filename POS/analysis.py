import json

with open('dictionaries/pos_words_nltk.json') as pwj: 
    pw_dict = json.load(pwj) 
    # print(pw_dict.keys())
    # print(len(pw_dict.keys()))

## 
# dict_keys(['NNS', 'VBP', '.', 'PRP', 'VBN', 'IN', 'NN', 'NNP', 'VBZ', 'DT', 'JJ', 'RB', 'RP', 'CC', 'JJS', 'CD', 'RBR', 'JJR', 'TO', 'VB', 'VBD', ',', 'WDT', 'PRP$', 'PDT', 'VBG', 'POS', 'EX', 'WRB', 'MD', '(', ')', 'WP', '``', "''", '$', 'FW', ':', 'UH', 'NNPS'])
# 40



with open('dictionaries/pos_words_stanza.json') as pwj: 
    pw_dict = json.load(pwj) 
    # print(pw_dict.keys())
    # print(len(pw_dict.keys()))

# #
# dict_keys(['NOUN', 'VERB', 'PUNCT', 'PRON', 'AUX', 'ADP', 'DET', 'ADJ', 'ADV', 'CCONJ', 'NUM', 'PART', 'PROPN', 'SCONJ', 'X', 'SYM'])
# 16

## =================== Verbs =================== 

# ------------ stanza ---------------
with open('dictionaries/verbs_stanza.json') as vsj: 
    vs_dict = json.load(vsj) 
    v_stanza = vs_dict.keys()
    print("Stanza detected %i unique verbs" % len(v_stanza))
    # print(v_stanza)

# write to a text for later use
with open("verbs_analysis/verbs_stanza.txt","w") as f:
    f.write("\n".join(v_stanza))

##### Stanza detected 1192 unique verbs


# ------------ nltk ---------------
with open('dictionaries/verbs_nltk.json') as vnj: 
    vn_dict = json.load(vnj) 
    v_nltk = vn_dict.keys()
    print("NLTK detected %i unique verbs" % len(v_nltk))
    # print(v_nltk)

##### NLTK detected 1102 unique verbs
# write to a text for later use
with open("verbs_analysis/verbs_nltk.txt","w") as f:
    f.write("\n".join(v_nltk))

# ------------ Different verbs in NLTK and stanza ---------------
def find_diff(li1, li2): 
    return (list(set(li1) - set(li2))) 

verb_diff = find_diff(list(v_nltk),list(v_stanza))
with open("verbs_analysis/different_verbs.txt","w") as f:
    f.write("\n".join(verb_diff))
# print(", ".join(verb_diff))

print("Union(NLTK, Stanza) - Intersection(NLTK, Stanza) = %i" % len(verb_diff))
## Union(NLTK, Stanza) - Intersection(NLTK, Stanza) = 121

# ------------ What's missed by NLTK? ---------------

n_missed = []
for n_verb in list(v_nltk):
    if n_verb not in vs_dict:
        n_missed.append(n_verb)
print("NLTK missed %i verbs detected by Stanza" % len(n_missed))
with open("verbs_analysis/NLTK_missed_verbs.txt","w") as f:
    f.write("\n".join(n_missed))
# print(", ".join(n_missed))

## NLTK missed 121 verbs detected by Stanza

s_missed = []
for s_verb in list(v_stanza):
    if s_verb not in vn_dict:
        s_missed.append(s_verb)
print("Stanza missed %i verbs detected by NLTK" % len(s_missed))
with open("verbs_analysis/Stanza_missed_verbs.txt","w") as f:
    f.write("\n".join(s_missed))
# print(", ".join(s_missed))

## Stanza missed 211 verbs detected by NLTK

