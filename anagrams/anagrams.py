from collections import defaultdict
import sys, json

if len(sys.argv) < 3:
	sys.exit("usage: py anagrams.py [dictionary] [output file]")

eq_class = defaultdict(list)

word_list = [ x.strip() for x in open(sys.argv[1]).readlines() ]

for word in word_list:
	key = ''.join(sorted(word))
	eq_class[key].append(word)

with open(sys.argv[2], 'w') as ana_file:
	json.dump(eq_class, ana_file, sort_keys = True, indent = 4, ensure_ascii=False)
