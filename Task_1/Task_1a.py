from adjacency_list_graph import AdjacencyListGraph
from dijkstra import dijkstra

if __name__ == "__main__":


	# Define the London Underground graph
	stations = ['Holborn', 'Oxford Circus', 'Leicester SQ', 'Piccadilly Circus', 'Green Park']
	edges = [
		('Holborn', 'Oxford Circus', 2),
		('Holborn', 'Leicester SQ', 2),
		('Leicester SQ', 'Piccadilly Circus', 2),
		('Oxford Circus', 'Piccadilly Circus', 3),
		('Piccadilly Circus', 'Green Park',  2),
		('Oxford Circus', 'Green Park', 1)
	]

	underground_graph = AdjacencyListGraph(len(stations), directed=True, weighted=True)
	for start, end, weight in edges:
		underground_graph.insert_edge(stations.index(start), stations.index(end), weight)

	# Run Dijkstra's algorithm
	source_station = 'Holborn'
	destination_station = 'Green Park'
	distances, predecessors = dijkstra(underground_graph, stations.index(source_station))
	destination_index = stations.index(destination_station)
	total_distance = distances[destination_index]

	# Get path
	path = []
	current = destination_index
	while current is not None:
		path.append(stations[current])
		current = predecessors[current]
	path = path[::-1]

	# Output results
	print(f"Total duration from {source_station} to {destination_station}: {total_distance} minutes")
	print(f"Route taken: {' -> '.join(path)}")
	print(f"Start: {path[0]}, End: {path[2]}")