#/usr/bin/env python3

import csv
import math

def main():
	with open('data.txt') as csvfile:
		t_list = [0 for i in range(-20, 31, 5)]
		for row in csvfile:
			for i in range(12):
				str = row[11 + i * 6:17 + i * 6]
				index = get_index(float(str))
				t_list[index] += 1

		print(t_list)
		e_value = get_expected_value(t_list)
		print('Expected value:', e_value)
		dispersia = get_dispersia(t_list, e_value)
		print('Dispersia:', dispersia)
		print('Standard deviation:', math.sqrt(dispersia))

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

def get_dispersia(t_list, e_value):
	count = 0
	sum = 0
	for index, value in enumerate(t_list):
		count += value;
		tmp = (-20 + index * 5) - e_value
		sum += tmp * tmp 

	return sum / count

def get_z(t_list, disp_sqrt):
	

if __name__ == '__main__':
	main()