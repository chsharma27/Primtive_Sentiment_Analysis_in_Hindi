###############################
#  Author - CHETAN SHARMA
#  Python version = 3.9.5
#  Title : Primitive sentiment
#          Analysis in Hindi
###############################

import codecs

## This module defines base classes for standard Python codecs
## (encoders and decoders) and provides access to the internal
## Python codec registry, which manages the codec and error
## handling lookup process. Most standard codecs are text
## encodings, which encode text to bytes, but there are
## also codecs provided that encode text to text, and bytes to bytes.

with codecs.open('dataset.txt', encoding='utf-8') as dataset:
    data = dataset.read()
## To split the sentences
data=data.split("।")

with codecs.open('Positive_words.txt', encoding='utf-8') as positive:
    positives = positive.read()
positives=positives.split(",")

with codecs.open('Negative_words.txt', encoding='utf-8') as negative:
    negatives = negative.read()
negatives=negatives.split(",")

print("Positive words: ",len(positives))
print("Negative words: ",len(negatives))

## the output
out={}

sentiments = {'Positive':0,'Negative':0,'Neutral':0}

def classifier(sentence):
    out[sentence]=[]
    words=sentence.split(" ")
    score = 0
    for i in words:
        if i =="नहीं":
            if score == 0:
                score-=1
            else:
                score=-score
            continue
        if i in positives:
            score+=1
        if i in negatives:
            score-=1
    if score >0:
        out[sentence].append("Positive")
        sentiments['Positive']+=1
    if score <0:
        out[sentence].append("Negative")
        sentiments['Negative']+=1
    if score == 0:
        out[sentence].append("Neutral")
        sentiments['Neutral']+=1
        
for k in range(len(data)-1):
    classifier(data[k])
    
o = codecs.open('output.txt', 'w', 'utf-8')

for key,value in out.items():
    o.write(key+" - "+value[0])

o.close()
positive.close()
negative.close()
dataset.close()
