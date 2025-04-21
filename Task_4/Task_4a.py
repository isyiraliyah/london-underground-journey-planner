# it is a module builtin which allows reading and processing Excel file
import openpyxl
# it creates a graph where nodes represent station and edges represents the line which connects them
from adjacency_list_graph import AdjacencyListGraph
# incorporated kruskals algorithm to find minimum spanning tree which connects all stations with minimum accumulated distance
from mst import kruskal
# imports bfs module to ensure connectivity within the graphs
from bfs import bfs

# Specifies the location of the Excel data stored
location = 'London Underground data.xlsx'
# loads the data file using openpyxl
load_file = openpyxl.load_workbook(location)
# focuses on the rows and columns containing the data within the Excel sheet
data = load_file.active
# creates an empty list which would store all the data from the Excel sheet
store_data = []
# Reads each row of data from the focused Excel sheet
for row in data.iter_rows(values_only=True):
    # Checks if there are any empty cells within the rows
    if None not in row:
        # If no empty cells then adds the rows to the store_data list created
        # Also stripping the data with any whitespaces otherwise the mst is not going to work on data with whitespaces
        store_data.append((row[0], row[1].strip(), row[2].strip(), row[3]))

# Creates an empty list which stores unique stations
unique_stations = []
# for each rows in data it checks if each station are not already in unique_station list, if not it adds them
for row in store_data:
    if row[1] not in unique_stations:
        unique_stations.append(row[1])
    if row[2] not in unique_stations:
        unique_stations.append(row[2])

# Creates an empty dictionary for travel times between stations.
travel_time = {}
# For each row in stored data list it maps each station as keys and the time between them as values
for i in store_data:
    travel_time[i[1], i[2]] = i[3]

# Initializes an undirected and weighted graph with connections as edges and stations as nodes
graph = AdjacencyListGraph(len(unique_stations), directed=False, weighted=True)
# retrieves each pair of stations as keys and time as values from the dictionary created
for (station1, station2), time in travel_time.items():
    # retrieves all the names of the stations from unique_stations list and adds indices to it for graph implementation
    index1 = unique_stations.index(station1)
    index2 = unique_stations.index(station2)
    # checks if there is no duplication in the edges as the graph is undirected edge A to B is same as B to A
    if not graph.has_edge(index1, index2) and not graph.has_edge(index2, index1):
        # if there are no edges between to indices(stations) it adds it with the weight(time)
        graph.insert_edge(index1, index2, time)

# Checks if all the nodes/stations in the created graph is reachable and there are no isolated nodes
# Uses bfs module to perform breadth first search for this graph starting from node 0
dist, _ = bfs(graph, 0)
# Checks if all distance between the nodes with in the graph are not infinite = unreachable
if float('inf') in dist:
    print("Warning! : The original graph is not completely reachable.")
else:
    print("The original graph is completely reachable.")

# Calculates the Minimum Spanning Tree using kruskals algorithm for the above graph
new_graph = kruskal(graph)

# Creates an empty list containing edges (lines) which are not a part of minimum spanning tree
closed_lines = []
# Iterates through each entry from the travel_time dictionary
for (station1, station2), time in travel_time.items():
    # Retrieves the indices of the respective stations from the unique station list
    index1 = unique_stations.index(station1)
    index2 = unique_stations.index(station2)
    # Checks if there is no edge(connections) between two stations in the MST
    if not new_graph.has_edge(index1, index2):
        # If no edges then it adds them into closed_lines list created
        closed_lines.append((station1, station2))

# Gives us the output with the closed lines
print("THE LINE SECTIONS TO BE CLOSED WHILE ENSURING CONNECTIVITY ARE:")
for station1, station2 in closed_lines:
    print(f"{station1} --- {station2}")

# Checks if all the nodes/stations in the newly created mst graph are connected
# Uses bfs library code to perform breadth first search for this graph starting from node 0
dist, _ = bfs(new_graph, 0)
# Checks if all distance between the nodes within the graph are not infinite = unreachable which tells us that mst is fully connected
if float('inf') in dist:
    print("!!!!! THE TRAIN NETWORK IS NOT COMPLETELY CONNECTED !!!!!")
else:
    print("******** THE TRAIN NETWORK REMAINS COMPLETELY CONNECTED AFTER CLOSURES ********")

print("Total number of Nodes/Stations =", len(unique_stations))
# From the Adjacency List Graph library code it uses get edge list functionality to get the list of the edges and finds its length
edge_list = new_graph.get_edge_list()
num_edges = len(edge_list)
print("Total number of edges/lines in the MST graph:", num_edges)
print("This result proves that the MST graph is acyclic as it has n nodes and n-1 edges")

# Represent and output the reduced network
print("\nReduced Network (Minimum Spanning Tree):")
for u in range(new_graph.get_card_V()):
    for edge in new_graph.get_adj_list(u):
        v = edge.get_v()
        weight = edge.get_weight()
        if u < v:  # To avoid printing duplicates in an undirected graph
            print(f"{unique_stations[u]} --- {unique_stations[v]} ({weight} minutes)")
