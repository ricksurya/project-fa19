import math

# Floyd-Warshall Algorithm
def shortestDistance(matrix):
	distances = []
	paths = []

	for u in range(len(matrix)):
		dist_u_v = []
		path_u_v = []
		for v in range (len(matrix)):
			if (u == v):
				dist_u_v.append([0] * len(matrix))
			else:
				dist_u_v.append([float('inf')] * len(matrix))
			path_u_v.append([])

		distances.append(dist_u_v)
		paths.append(path_u_v)

	for u in range(len(matrix)):
		for v in range(len(matrix)):
			if u != v and matrix[u][v] != 'x':
				distances[u][v][0] = matrix[u][v]
				paths[u][v].append(v)

	for k in range(1, len(matrix)):
		for u in range(len(matrix)):
			for v in range(len(matrix)):
				uses_k = distances[u][k-1][k-1] + distances[k-1][v][k-1]
				bypass_k = distances[u][v][k-1]

				if (uses_k < bypass_k):
					distances[u][v][k] = uses_k
					paths[u][v] = paths[u][k-1] + paths[k-1][v]
				else:
					distances[u][v][k] = bypass_k

	shortestDistance = []
	for u in range(len(matrix)):
		node = []
		for v in range(len(matrix)):
			node.append(min(distances[u][v]))
		shortestDistance.append(node)

	return shortestDistance, paths

matrix = [['x', 1 , 2 , 3 , 4 ],
		  [ 1 ,'x','x','x', 5 ],
		  [ 2 ,'x','x','x','x'],
		  [ 3 ,'x','x','x','x'],
		  [ 4 , 5 ,'x','x','x']]

shortestDistance, path = shortestDistance(matrix)

def printDistance(shortestDistance):
	for i in range(len(shortestDistance)):
		print("shortestDistance for node " + str(i) + ": ")
		for j in range(len(shortestDistance)):
			print("node " + str(i) + " to node " + str(j) + " min distance: " + str(shortestDistance[i][j]))
		print('')

def printPath(path):
	for i in range(len(path)):
		print ("path for node " + str(i) + ": ")
		for j in range(len(path)):
			print ("node " + str(i) + " to node " + str(j) + ": " + str(path[i][j]))
		print('')
