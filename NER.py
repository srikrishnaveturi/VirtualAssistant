#his is the basic code to find out the named entities in your string

import spacy
nlp = spacy.load('en_core_web_sm')

text = nlp(input("enter your sentence here: "))

for word in text.ents:
    print(word.text,word.label_)
