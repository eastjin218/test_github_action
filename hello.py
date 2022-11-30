import os, glob

with open('./test.txt', 'r') as f:
    text = f.readlines()

print(text[0])