import matplotlib
import nltk
from scipy import spatial
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import copy
import numpy
import matplotlib.pyplot as plt

features = ['print','pandas','pd','import']
ngram_value = 1


def read_file_n_gram(file_path):
    try:
        with open(file_path) as f:
            s=''
            for line in f.readlines():
                s=s+line
            return s
    except Exception as e:
        print(e.__str__)


def normalize(lines):
    replaceLines=lines
    normalizedLines=''
    for line in replaceLines.split('\n'):
        s=''
        for word in line.split(' '):
            if word not in features:
                line=line.replace(word,'')
        normalizedLines+=line
    return normalizedLines



file1 = read_file_n_gram("usama.py")
file2=read_file_n_gram("usama1.py")


FILE1=normalize(file1)
FILE2= normalize(file2)

tk_words1 = nltk.word_tokenize(FILE1)
tk_words2 = nltk.word_tokenize(FILE2)

feature_vector = {}
fv = nltk.ngrams(features, ngram_value)
for f in fv:
    feature_vector[f] = 0

ngram1 = nltk.ngrams(tk_words1, ngram_value)
ngram2 = nltk.ngrams(tk_words2, ngram_value)

freq_file1 = nltk.FreqDist(ngram1)
freq_file2 = nltk.FreqDist(ngram2)


def assign_value(vector):
    vcopy = copy.deepcopy(feature_vector)
    for vec in vcopy:
        if vec in vector:
            vcopy[vec] = vector[vec]
    return vcopy
f1 = assign_value(freq_file1)
f2 = assign_value(freq_file2)
df1 = pd.DataFrame([f1])
df2 = pd.DataFrame([f2])



import numpy as np
res = cosine_similarity(df1.values, df2.values)
print("Cosine Similarity:", float(res))
length=len(features)
print(length)
x = np.arange(length)
plt.bar(x,height=f1.values())
plt.xticks(x, features)
plt.show()