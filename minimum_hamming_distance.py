import random
import numpy as numpy
import pandas as pd
from hamming_practice import hamming

df = pd.read_csv('sample.csv', names=['word', 'bin'])

count = 1
min = 32 # bin의 길이, 

for i in range(len(df)):
    for j in range(i+1, len(df)):
        hd = hamming(df.iloc[i, 1], df.iloc[j, 1])
        print(count, " ( ", df.iloc[i, 0], df.iloc[j, 0], " )hamming_distance: ", hd)
        count = count+1
        if min > hd:
            min = hd

print("min hamming distance ", min)
