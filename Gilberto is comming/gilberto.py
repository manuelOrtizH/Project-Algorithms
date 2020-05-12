class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __repr__(self):
		return "%s, %s" % (self.x, self.y)
	def __str__(self):
		return "%s, %s" % (self.x, self.y)

def coorToList(coordenate):
	list_coor = coordenate.replace("(","").replace(")","").replace(" ", ",").split(",")
	list_coor = [int(i) for i in list_coor]
	return list_coor

def list_to_coor(points):
	list_coor = points.replace("[","(").replace("]",")").replace(" ", "")
	return list_coor

def read_data():
	riskSites = int(input("Sites of risk: "))
	coordenates = []
	points = []
	separatedPoints = []
	for i in range(riskSites):
		coor = input("Coordenates: ")
		points = coorToList(coor)	
		separatedPoints.append(Point(points[0], points[1])) 
		separatedPoints.append(Point(points[0], points[3]))
		separatedPoints.append(Point(points[2], points[3]))
		separatedPoints.append(Point(points[2], points[1])) 

	return separatedPoints
	
def left_most_point(points):
	minimum = 0
	for i in range(1, len(points)):
		if points[i].x < points[minimum].x:
			minimum = i
		elif points[i].x == points[minimum].x:
			if points[i].y > points[minimum].y:
				minimum = i
	return minimum

def convex_hull(points):
	left = left_most_point(points)
	n = len(points)
	p = left
	q = 0
	solution = []
	while True:
		solution.append(p)
		q = (p+1)%n 
		for i in range(n):
			if orientation(points[p],points[i],points[q]):
				q = i
		p = q

		if p == left:
			break

	sol = []
	for each in solution:
		sol.append([points[each].x, points[each].y])

	sol.sort()

	return sol

def orientation(p,q,r):
	m = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
	if m>0:
		return True
	else:
		return False

def main():
	points = convex_hull(read_data())
	for i in points:
		str(i)
		listString = list_to_coor(str(i))
		print(listString)	

main()