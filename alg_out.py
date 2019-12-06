def realPath(tsp_path, all_paths):
	real_path = [tsp_path[0]]
	for i in range(len(tsp_path)-1):
		real_path.extend(all_paths[tsp_path[i]][tsp_path[i+1]])
	return real_path

# centroids: tsp_path
# clusters: dictionary of key = centroid and value is homes in the cluster
# homes:  set of homes
# distances: Matrix containing the distances
def dropOff(tsp_path, real_path, clusters, homes, distances):
	if tsp_path[0] in clusters:
		centroids = tsp_path[:]
	else:
		centroids = tsp_path[1:]
	drop = {}

	for v in real_path:
		drop_location = []

		if v in centroids:
			for h in clusters[v]:
				if h in homes:
					drop_location.append(h)
					homes.remove(h)
			centroids.pop()
		else:
			for h in homes:
				if distances[v][h] < distances[centroids[0]][h]:
					drop_location.append(h)
					homes.remove(h)

		if drop_location:
				drop[v] = drop_location

	return drop


