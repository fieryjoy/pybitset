from bitset import *
import sys

def print_list(lst):
	n = len(lst)
	for j in range(n):
		print lst[j],
		if j != n-1:
			sys.stdout.write(', ')

def merge(a, b):	
	i = j = 0
	merged = []
	while i < len(a) and j < len(b):
		if a[i].lower(b[j]):
			merged.append(a[i]); i+=1
		elif b[j].lower(a[i]):
			merged.append(b[j]); j+=1
		else:
			merged.append(a[i].merge(b[j])); i+=1; j+=1
	merged+=a[i:]+b[j:]
	return merged

line = [[], []]
for i in range(0,2):
	s=[[e[0], int(e[1])] for e in [x.strip().split('/') for x in sys.stdin.readline().split(',')]]
	current=s[0][0]
	tmp=Bitset(current)
	for name, bit in s:
		if name!=current:
			line[i].append(tmp)
			current=name
			tmp=Bitset(current)
		tmp.set(bit)
	line[i].append(tmp)

for i in range(2):
	print_list(line[i])
	print
print_list(merge(line[0], line[1]))
print
