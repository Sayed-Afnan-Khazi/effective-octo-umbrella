# A Big Thank You to Dina Bavli: https://betterprogramming.pub/unlocking-emotions-in-text-using-python-6d062b48d71f

import nltk
nltk.download('punkt')
import pandas as pd
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import requests

from LeXmo import LeXmo

def getEmotion(text):


    text = "Like did I do a mistake by messaging them?" 

    emo=LeXmo.LeXmo(text)

    # print(emo)

    maxm = 'anger'
    for x in ['anticipation', 'disgust', 'fear', 'joy',  'sadness', 'surprise']:
        if emo[x] > emo[maxm]:
            maxm = x
    else:
        mostProbableEmo = maxm

    maxm = 'negative'
    for x in ['positive',  'trust']:
        if emo[x] > emo[maxm]:
            maxm = x
    else:
        mostProbableExtraEmo = maxm

    return mostProbableEmo, mostProbableExtraEmo

if __name__ == "__main__":
    # testing the function
    text = "Like did I do a mistake by messaging them?" 
    mostProbableEmo, mostProbableExtraEmo = getEmotion(text)
    print("Most Probable Emotion:", mostProbableEmo)
    print("Most Probable State:", mostProbableExtraEmo)

