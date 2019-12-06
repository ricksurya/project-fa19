def dfs(adj_lst):
	visited = [False] * len(adj_lst)
	path = []

	def explore(v):
		visited[v] = True
		path.append(v)
		for u in adj_lst[v]:
			if not visited[u]:
				explore(u)
				path.append(v)

	explore(0)
	return path

def translate(dic, path):
	toReturn = []
	for i in path:
		toReturn.append(dic[i])
	return toReturn

def deleteRepetition(path):
	toReturn = []
	for i in path:
		if i not in toReturn:
			toReturn.append(i)
	toReturn.append(0)
	return toReturn


dic = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}

adj_lst = [[1],
		   [0, 2, 3],
		   [2],
		   [2, 4, 5],
		   [4],
		   [4]]

path = dfs(adj_lst)
cleaned_path = deleteRepetition(path)
final_path = translate(dic, cleaned_path)


