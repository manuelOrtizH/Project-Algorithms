
def sortByNation(collection):
	collection.sort()
	print()
	for i in collection:
		print(i[-1])
	


if __name__ == '__main__':

	teams = int(input("Number of teams: " ))
	collection = []

	for i in range(teams):
		print(i+1, "º team and nationality")
		team = input()
		country = input()
		collection.append([country, team])

	sortByNation(collection)



