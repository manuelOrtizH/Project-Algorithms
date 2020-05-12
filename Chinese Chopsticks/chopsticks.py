import math
import os
import random
import re
import sys

def moveChopsticks(chopsticks):
	totalOfChopsticks = n
	for i in range(0,n-1):
		for j in range(i+1,n):
			doTheyIntersect = intersect(chopsticks[i], chopsticks[j])
			if doTheyIntersect:
				totalOfChopsticks-=2
	if totalOfChopsticks < 0:
		totalOfChopsticks = 0
	
	return totalOfChopsticks


def intersect(chopOne, chopTwo):

	if chopOne[0] == chopOne[2] and chopTwo[0] == chopTwo[2]:
		if (chopTwo[0] == chopOne[0] or chopTwo[2] == chopOne[2]) and (chopTwo[1] <= chopOne[3] or chopTwo[1] >= chopOne[1]):
			return True
		else:
			return False

	if chopOne[0] == chopOne[2] and chopTwo[1] == chopTwo[3]:
		if chopTwo[1] <= chopOne[3] or chopTwo[1] >= chopOne[1]:
			return True
		else:
			return False

	if chopOne[1] == chopOne[3] and chopTwo[1] == chopTwo[3]:
		if (chopTwo[1] == chopOne[1] or chopTwo[3] == chopOne[3]) and (chopTwo[0] <= chopOne[2] or chopTwo[0] >= chopOne[0]):
			return True
		else:
			return False


if __name__ == '__main__':

    n = int(input("Number of chopsticks: "))
    chopsticks = []

    for i in range(0,n):
    	chopstick = list(map(int, input().split()))
    	chopsticks.append(chopstick)
   	
    print(moveChopsticks(chopsticks))



    

    
    
