import json
import pprint

with open('wordbank.txt', 'r') as f:
    lines = f.read()

wordbankpre = lines.split(" ")
f.close()
wordbank = []

for i in wordbankpre:
    i = i.strip()
    i = i.upper()
    wordbank.append(i)

lines = []
with open('wordpuzzle.txt') as f:
    lines = f.readlines()
f.close()
wordpuzzle = []

for i in lines:
    i = i.strip()
    wordpuzzle.append(i)


out_dict = {x: {'position':"[]", 'direction':"[]"} for x in wordbank}

def forward_search(word):
    r = -1
    c = -1
    for i in range(0,len(wordpuzzle)):
        k = wordpuzzle[i].find(word)
        if k != -1:
            r = i + 1
            c = k + 1
            coord = "[" + str(r) + ", " + str(c) + "]"
            if out_dict[word]["position"] == "[]":
                out_dict[word]["position"] = coord
                out_dict[word]["direction"] = "[forwards]"
            else:
                out_dict[word]["position"] = out_dict[word]["position"], coord
                out_dict[word]["direction"] = out_dict[word]["direction"], "[forwards]"

    return None

def backward_search(word):
    r = -1
    c = -1
    for i in range(0,len(wordpuzzle)):
        k = wordpuzzle[i].find(word[::-1])
        if k != -1:
            r = i + 1
            c = k + 1
            coord = "[" + str(r) + ", " + str(c) + "]"
            if out_dict[word]["position"] == "[]":
                out_dict[word]["position"] = coord
                out_dict[word]["direction"] = "[backwards]"
            else:
                out_dict[word]["position"] = out_dict[word]["position"], coord
                out_dict[word]["direction"] = out_dict[word]["direction"], "[backwards]"
    return None

def up_search(word):
    r = -1
    c = -1
    length = len(wordpuzzle)
    for j in range(0,len(wordpuzzle)):
        wordline = ''
        for i in range(0,len(wordpuzzle)):
            wordline += wordpuzzle[i][j]

        row_ind = (wordline.find(word[::-1]))

        if row_ind >= 0:
            r = length - row_ind + 1
            c = j + 1

        coord = "[" + str(r) + ", " + str(c) + "]"
        if r != -1:
            if out_dict[word]["position"] == "[]":
                out_dict[word]["position"] = coord
                out_dict[word]["direction"] = "[up]"
            else:
                out_dict[word]["position"] = out_dict[word]["position"], coord
                out_dict[word]["direction"] = out_dict[word]["direction"], "[up]"
        r = -1
        c = -1
    return None

def down_search(word):
    r = -1
    c = -1
    length = len(wordpuzzle)
    for j in range(0,len(wordpuzzle)):
        wordline = ''
        for i in range(0,len(wordpuzzle)):
            wordline += wordpuzzle[i][j]

        row_ind = (wordline.find(word))

        if row_ind >= 0:
            r = row_ind + 1
            c = j + 1


        coord = "[" + str(r) + ", " + str(c) + "]"
        if r != -1:
            if out_dict[word]["position"] == "[]":
                out_dict[word]["position"] = coord
                out_dict[word]["direction"] = "[down]"
            else:
                out_dict[word]["position"] = out_dict[word]["position"], coord
                out_dict[word]["direction"] = out_dict[word]["direction"], "[down]"
        r = -1
        c = -1
    return None

def search(word):
    forward_search(i)
    backward_search(i)
    up_search(i)
    down_search(i)
    return None

for i in wordbank:
    search(i)

found_words = out_dict

with open('output.json', 'w') as f:
    json.dump(found_words, f, indent = 4)