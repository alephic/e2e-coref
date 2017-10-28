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

def create_subsets(d, min_amount=0.5, max_amount=1.0, subsets=10):
    for i in range(subsets):
        yield create_subset(d, (i/(subsets-1))*(max_amount-min_amount) + min_amount)

if __name__ == '__main__':
    d = load_jsonlines('train.english.jsonlines')
    random.shuffle(d)
    for i, subset in enumerate(create_subsets(d)):
         dump_jsonlines(subset, 'train.english.%d.jsonlines' % len(subset))

