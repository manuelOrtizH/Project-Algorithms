def caluculateMoney(cities, tankCapacity):
	money = tankCapacity
	gas = tankCapacity
	toFill = 0
	i = 1
	while (i<=len(cities)):
		gas-=1
		if not gasReaches(i, tankCapacity, len(cities), gas):
			toFill = tankCapacity -gas
			money += toFill*cities[i]
			gas = tankCapacity
			i+=1
		else: 
			break
	return money

def gasReaches(city, tankCapacity, n, gas):
	city+=1
	difference = n-city
	if gas < difference:
		return False
	if gas == difference or gas > difference:
		return True

def main():
	car = list(map(int, input().split()))
	cities = [x for x in range(1,car[0]+1)]
	tankCapacity = car[1]
	print(caluculateMoney(cities, tankCapacity))
	
main()