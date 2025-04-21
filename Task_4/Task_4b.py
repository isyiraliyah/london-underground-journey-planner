from dijkstra import dijkstra
import matplotlib.pyplot as plt
from Task_4a import new_graph, unique_stations

# Use the new_graph from your MST calculation
print("\nReduced Network (Minimum Spanning Tree):")
for u in range(new_graph.get_card_V()):
    for edge in new_graph.get_adj_list(u):
        v = edge.get_v()
        weight = edge.get_weight()
        if u < v:  # To avoid printing duplicates in an undirected graph
            print(f"{unique_stations[u]} --- {unique_stations[v]} ({weight} minutes)")

# Calculate the longest path in the MST using Dijkstra's algorithm
longest_time = 0
longest_path = []

# Store all journey durations
time_durations = []

# Iterate over each station and compute Dijkstra's algorithm
for u in range(new_graph.get_card_V()):
    distances, predecessors = dijkstra(new_graph, u)  # Run Dijkstra from station `u`

    for v in range(new_graph.get_card_V()):
        if u != v and distances[v] != float('inf'):  # Ensure `v` is reachable
            # Reconstruct the 1
            path = []
            current = v
            total_time = distances[v]  # Total time is the distance to `v`

            while current is not None and current != -1:  # Ensure current is valid
                path.append(current)
                current = predecessors[current] if current < len(predecessors) else None

            path.reverse()

            # Store journey duration
            time_durations.append(total_time)

            # Update longest path if this is the longest
            if total_time > longest_time:
                longest_time = total_time
                longest_path = path

# Print longest path details
print("\nLongest Path in the MST:")
print(f"Duration: {longest_time} minutes")
print(f"Path: {' → '.join([unique_stations[node] for node in longest_path])}")

# Histogram of journey durations
plt.hist(time_durations, bins=20, edgecolor='black', align='left')
plt.xlabel("Journey Duration (minutes)")
plt.ylabel("Frequency")
plt.title("Histogram of Reduced Journey Durations in the MST")
plt.show()