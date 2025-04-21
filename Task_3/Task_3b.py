import pandas as pd
import matplotlib.pyplot as plt
from dijkstra import dijkstra  # Import the dijkstra.py file


# Define the Edge classes
class Edge:
    def __init__(self, v, weight=1):
        self.v = v
        self.weight = weight

    def get_v(self):
        return self.v

    def get_weight(self):
        return self.weight


# Define the CustomGraph class
class CustomGraph:
    def __init__(self):
        self.nodes = {}
        self.station_line_mapping = {}

    def add_station(self, station_line, station_index):
        if station_index not in self.nodes:
            self.nodes[station_index] = []
            self.station_line_mapping[station_index] = station_line

    def add_edge(self, station_index1, station_index2, weight=1):
        if station_index1 in self.nodes and station_index2 in self.nodes:
            self.nodes[station_index1].append(Edge(station_index2, weight))
            self.nodes[station_index2].append(Edge(station_index1, weight))

    def get_neighbors(self, node):
        return self.nodes.get(node, [])

    def get_card_V(self):
        # Return the number of nodes in the graph
        return len(self.nodes)

    def get_adj_list(self, node):
        # Return the list of edges for the given node
        return self.nodes.get(node, [])


# Function to reconstruct path from predecessors
def reconstruct_path(predecessors, start, end):
    path = []
    current = end
    while current != start:
        if current is None or current not in predecessors:
            return []
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path


# Load data and create graph
file_path = 'London Underground data.xlsx'
data = pd.read_excel(file_path, header=None)
data.columns = ['Line', 'Station A', 'Station B', 'Time']

station_to_index = {}
graph = CustomGraph()
current_index = 0

# Build the graph with nodes and edges
for _, row in data.iterrows():
    line, station_a, station_b = row['Line'], row['Station A'], row['Station B']
    if pd.isna(station_a) or pd.isna(station_b) or pd.isna(line):
        continue
    station_a_key = f"{station_a} ({line})"
    station_b_key = f"{station_b} ({line})"
    if station_a_key not in station_to_index:
        station_to_index[station_a_key] = current_index
        graph.add_station(station_a_key, current_index)
        current_index += 1
    if station_b_key not in station_to_index:
        station_to_index[station_b_key] = current_index
        graph.add_station(station_b_key, current_index)
        current_index += 1
    graph.add_edge(station_to_index[station_a_key], station_to_index[station_b_key])

# Add interchange stations
interchanges = [
    ("Paddington", ["Bakerloo", "Circle", "District", "Hammersmith & City"]),
    ("Baker Street", ["Bakerloo", "Circle", "Hammersmith & City", "Jubilee", "Metropolitan"]),
    ("Oxford Circus", ["Bakerloo", "Central", "Victoria"]),
    ("King's Cross St. Pancras", ["Circle", "Hammersmith & City", "Metropolitan", "Northern", "Piccadilly", "Victoria"]),
    ("Liverpool Street", ["Central", "Circle", "Hammersmith & City", "Metropolitan"]),
    ("Moorgate", ["Circle", "Hammersmith & City", "Metropolitan", "Northern"]),
    ("Bank", ["Central", "Northern", "Waterloo & City"]),
    ("Stratford", ["Central", "Jubilee"]),
    ("Euston", ["Northern", "Victoria"]),
    ("Waterloo", ["Bakerloo", "Jubilee", "Northern", "Waterloo & City"]),
    ("Piccadilly Circus", ["Bakerloo", "Piccadilly"])
]
for station, lines in interchanges:
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            line1_key = f"{station} ({lines[i]})"
            line2_key = f"{station} ({lines[j]})"
            if line1_key in station_to_index and line2_key in station_to_index:
                idx1 = station_to_index[line1_key]
                idx2 = station_to_index[line2_key]
                graph.add_edge(idx1, idx2)

# Initialize list for storing journey durations and identifying the longest path
stop_counts = []
longest_path = []
max_stops = 0

# Calculate journey duration by stops for each unique pair of stations
for start_station, start_idx in station_to_index.items():
    distances, predecessors = dijkstra(graph, start_idx)

    for end_station, end_idx in station_to_index.items():
        if start_idx != end_idx and end_idx in distances:  # Avoid same start and end
            # Get path and calculate stops
            path_indices = reconstruct_path(predecessors, start_idx, end_idx)
            num_stops = len(path_indices) - 1
            stop_counts.append(num_stops)

            # Track the longest path
            if num_stops > max_stops:
                max_stops = num_stops
                longest_path = [graph.station_line_mapping[idx] for idx in path_indices]

# Print debug information
print(f"Total journeys calculated: {len(stop_counts)}")
print(f"Longest journey by stops: {max_stops} stops")
print("Path for the longest journey:", " → ".join([station.split(" (")[0] for station in longest_path]))

# Plot histogram of journey durations
plt.hist(stop_counts, bins=range(1, max(stop_counts) + 2), edgecolor='black', align='left')
plt.xlabel("Number of Stops")
plt.ylabel("Frequency of Journeys")
plt.title("Histogram of Journey Durations by Number of Stops")
plt.show()
