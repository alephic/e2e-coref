import json
import random

def load_jsonlines(filename):
    d = []
    with open(filename) as f:
        for line in f:
            d.append(json.loads(line))
    return d

def dump_jsonlines(d, filename):
    with open(filename, mode='w') as f:
        for line_json in d:
            print(json.dumps(line_json), file=f)

def create_subset(d, keep_amount):
    return d[:int(len(d)*keep_amount)]

def create_subsets(d, min_amount=0.2, max_amount=1.0, subsets=4):
    for i in range(subsets):
        yield create_subset(d, (i/(subsets-1))*(max_amount-min_amount) + min_amount)

def keep_genre(d, genre_code):
    return list(filter((lambda doc: doc['doc_key'].startswith(genre_code)), d))

def remove_genre(d, genre_code):
    return list(filter((lambda doc: not doc['doc_key'].startswith(genre_code)), d))

def load_conll_lines(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def dump_conll_lines(lines, filename):
    with open(filename, mode='w') as f:
        f.writelines(lines)

def keep_genre_conll(lines, genre_code):
    filtered = []
    in_doc = False
    for line in lines:
        if line.startswith("#begin document (" + genre_code):
            in_doc = True
        if in_doc:
            filtered.append(line)
        if line.startswith("#end document"):
            in_doc = False
    return filtered

def remove_genre_conll(lines, genre_code):
    filtered = []
    in_doc = False
    for line in lines:
        if line.startswith("#begin document (" + genre_code):
            in_doc = True
        if not in_doc:
            filtered.append(line)
        if line.startswith("#end document"):
            in_doc = False
    return filtered


