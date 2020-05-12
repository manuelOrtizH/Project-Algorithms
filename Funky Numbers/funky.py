import math
import os
import random
import re
import sys

def is_triangular_number(n):
	for i in range(1,n):
		for j in range(2,n):
			if value_of_equation(j) + value_of_equation(i) == n:
				return 1

def value_of_equation(i):
	value = (i*(i+1))/2
	return value

if __name__ == '__main__':
	n = int(input())
	
	if is_triangular_number(n)==1:
		print("YES")
	else:
		print("NO")







	