import math

class City():
	def __init__(self,name,coordenates,value,numOfCity):
		self._name = name
		self._coordenates = coordenates
		self._value = value
		self._numOfCity = numOfCity

	def name(self):
		return self._name

	def coordenates(self):
		return self.coordenates

	def value(self):
		return self.value

	def __iter__(self):
		return iter(self._numOfCity)
	
class Road():
	def __init__(self, city):
		self._city = city
		
	def __getitem__(self, city_number):
		return self._city[city_number]

def coor_to_list(coordenate):
	temp = coordenate.replace("(","").replace(")","").split(",")
	temp = [int(i) for i in temp]
	return temp

def read_data():
	n = int(input("N cities: "))
	cities = [] #list of objects
	for i in range(n):
		name = input("City: ")
		coordenates = input("Coordenates: ")
		temp = coor_to_list(coordenates)
		value = int(input("Value: "))
		cities.append(City(name,coordenates,value, i))

	return cities

def getRoads(cities):
	totalOfCitites = len(cities)
	roads = []
	if totalOfCitites <=1:
		return [cities]
	
	#Find the remaining paths after the first city


	
	return roads

def find_all_paths(cities, start, end, path):
	path = path + [start]
	newpaths = []
	if start == end:
		return [path]
	paths = []
	for node in cities:
		if node not in path:
			newpaths = find_all_paths(cities, node, end, path)
		for newpath in newpaths:
			paths.append(newpath)

	
	return paths

def main():	
	cities = read_data()
	path = []
	print(find_all_paths(cities, 0, 1, path))
	
	#g = { C1 : [C2,C3,C4],
		#  C2 : [C3,C4],
		#  C3 : [C2,C4],
		#  C4 : [C3,C2]}
	



main()