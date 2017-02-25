#/usr/bin/env python3

import csv

def main():
	with open('data.txt') as csvfile:
		map = [0 for i in range(-20, 36, 5)]
		for row in csvfile:
			for i in range(12):
				str = row[11 + i * 6:17 + i * 6]
				index = get_index(float(str))
				map[index] += 1

		print(map)

def get_index(temparature):
	index = 0
	for i in range(-20, 31, 5):
		if temparature < i:
			return index
		else:
			index += 1
	return index

if __name__ == '__main__':
	main()