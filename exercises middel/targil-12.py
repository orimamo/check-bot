from collections import defaultdict, Counter
import collections

str1 = input("insert each word you want : ")
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))



