import time
import matplotlib.pyplot as plt
from random import randint
from adjacency_list_graph import AdjacencyListGraph
from dijkstra import dijkstra
from generate_random_graph import generate_random_graph


def calculate_average_execution_time_with_stops(n, num_trials=1):
    # Generate a random graph with `n` stations and set all edge weights to 1 (indicating stops)
    graph = generate_random_graph(n, 0.08, True, False, True, 1, 10)
    total_time_ms = 0
    for _ in range(num_trials):
        # Pick two random stations (source and destination)
        source = randint(1000, n - 1)
        destination = randint(1000, n - 1)
        while destination == source:
            destination = randint(1000, n - 1)

        # Start time measurement
        start_time = time.time()

        # Run Dijkstra's algorithm from the source
        distances, predecessors = dijkstra(graph, source)

        # End time measurement
        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
        total_time_ms += execution_time_ms

        # Calculate the number of stops and path
        total_stops = distances[destination]
        path = []
        current = destination
        while current is not None:
            path.append(current)
            current = predecessors[current]
        path.reverse()  # Reverse to get path from source to destination

        # Print the results for this pair
        print(f"Trial: Journey from {source} to {destination}")
        print(f"Total stops: {total_stops}")
        print(f"Path taken: {' -> '.join(map(str, path))}")
        print(f"Execution time: {execution_time_ms:.2f} ms\n")

    # Calculate average execution time across all trials
    average_time_ms = total_time_ms / num_trials
    return average_time_ms


if __name__ == "__main__":
    # Test different network sizes
    network_sizes = [1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
    average_times = []

    for n in network_sizes:
        avg_time = calculate_average_execution_time_with_stops(n)
        average_times.append(avg_time)
        print(f"Average execution time for network size {n}: {avg_time:.2f} ms\n")

    # Plotting the empirical results
    plt.figure(figsize=(10, 6))
    plt.plot(network_sizes, average_times, label="Empirical Execution Time (Stops)", marker="o")

    # Theoretical time complexity curve (assuming O(E + V log V) for Dijkstra's algorithm with priority queue)
    theoretical_times = [n * (0.1 * n * 0.5 + n ** 0.5) for n in network_sizes]  # Scaled for comparison
    plt.plot(network_sizes, theoretical_times, label="Theoretical Time Complexity (Scaled)", linestyle="--")

    plt.xlabel("Network Size (n)")
    plt.ylabel("Average Execution Time (ms)")
    plt.title("Average Execution Time vs Network Size (Using Stops)")
    plt.legend()
    plt.grid(True)
    plt.show()
