#/usr/bin/env python3

import csv

def main():
	for i in range(-20, 31, 5):
		print(i)
	with open('data.txt') as csvfile:
		t_list = [0 for i in range(-20, 31, 5)]
		for row in csvfile:
			for i in range(12):
				str = row[11 + i * 6:17 + i * 6]
				index = get_index(float(str))
				t_list[index] += 1

		print(t_list)
		get_expected_value(t_list)

def get_index(temparature):
	index = 0
	for i in range(-20, 31, 5):
		if temparature < i:
			return index
		else:
			index += 1
	return index

def get_expected_value(t_list):
	count = 0
	sum = 0
	for index, value in enumerate(t_list):
		count += value;
		sum += (-20 + index * 5) * value

	return sum / count

if __name__ == '__main__':
	main()