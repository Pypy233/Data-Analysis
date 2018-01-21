import json
from collections import defaultdict as df
from collections import Counter
import pandas as pd, numpy as np
from pandas import DataFrame, Series
from matplotlib import pyplot

def print_line():
    print('-----------------------------------------------------------------------------------------------------')


path = 'data/example.txt'
records = [json.loads(line) for line in open(path)]
print(records)
print(records[0]['u'])
print(records[0]['tz'])
print_line()


timeZones = [rec['tz'] for rec in records if 'tz' in rec]
print(timeZones)
print_line()

def get_counts(sequence):
    counts = df(int)
    for x in sequence:
        counts[x] += 1
    return counts


counts = get_counts(timeZones)
print(counts['America/Los_Angeles'])


def top_counts(topCounts, n = 10):
    keyMapPair = [(counts, tz) for tz, counts in topCounts.items()]
    keyMapPair.sort()
    return keyMapPair[-n:]


'''It seems that the pair should be(tz, counts) instead of (counts, tz), 
later I find the sequence of tz, counts...'''
for i in top_counts(counts):
    print(i)

print_line()
counts = Counter(timeZones)
for i in counts.most_common(10):
    print(i)


print_line()
frame = DataFrame(records)
print(frame)
print_line()

tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])
print_line()


clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])
print_line()

tz_counts.plot()
pyplot.plot(tz_counts)
pyplot.savefig('output/jsonAnalysis.png')