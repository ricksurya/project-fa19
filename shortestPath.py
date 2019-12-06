import math

# Floyd-Warshall Algorithm
def shortestDistance(matrix):
	distances = []
	for u in range(len(matrix)):
		dist_u_v = []
		for v in range (len(matrix)):
			if (u == v):
				dist_u_v.append([0] * len(matrix))
			else:
				dist_u_v.append([float('inf')] * len(matrix))
		distances.append(dist_u_v)

	for u in range(len(matrix)):
		for v in range(len(matrix)):
			if u != v and matrix[u][v] != 'x':
				distances[u][v][0] = matrix[u][v]

	for k in range(1, len(matrix)):
		for u in range(len(matrix)):
			for v in range(len(matrix)):
				distances[u][v][k] = min(distances[u][k-1][k-1] + distances[k-1][v][k-1], distances[u][v][k-1])

	shortestDistance = []
	for u in range(len(matrix)):
		node = []
		for v in range(len(matrix)):
			node.append(min(distances[u][v]))
		shortestDistance.append(node)

	return shortestDistance

matrix = [['x', 1 , 2 , 3 , 4 ],
		  [ 1 ,'x','x','x', 5 ],
		  [ 2 ,'x','x','x','x'],
		  [ 3 ,'x','x','x','x'],
		  [ 4 , 5 ,'x','x','x']]

shortestDistance = shortestDistance(matrix)

def printDistance(shortestDistance):
	for i in range(len(shortestDistance)):
		print("shortestDistance for node " + str(i) + ": ")
		for j in range(len(shortestDistance)):
			print("node " + str(i) + " to node " + str(j) + " min distance: " + str(shortestDistance[i][j]))
		print('')
