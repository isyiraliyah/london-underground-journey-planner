from adjacency_list_graph import AdjacencyListGraph
from dijkstra import dijkstra

# Testing
if __name__ == "__main__":
	# Define the London Underground graph with each edge weight as 1 (number of stops)
	stations = ['Holborn', 'Oxford Circus', 'Leicester SQ', 'Piccadilly Circus', 'Green Park']
	edges = [
		('Holborn', 'Oxford Circus', 1), # 1 represent the stops
		('Holborn', 'Leicester SQ', 1),
		('Leicester SQ', 'Piccadilly Circus', 1),
		('Oxford Circus', 'Piccadilly Circus', 1),
		('Piccadilly Circus', 'Green Park',  1),
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
	total_stops = distances[destination_index]

	# Get path
	path = []
	current = destination_index
	while current is not None:
		path.append(stations[current])
		current = predecessors[current]
	path = path[::-1]

	# Output results
	print(f"Total number of stops from {source_station} to {destination_station}: {total_stops}")
	print(f"Route taken: {' -> '.join(path)}")
	print(f"Start: {path[0]}, End: {path[-1]}")
