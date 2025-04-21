import time
import matplotlib.pyplot as plt
from random import randint
from adjacency_list_graph import AdjacencyListGraph
from dijkstra import dijkstra
from generate_random_graph import generate_random_graph


def calculate_average_execution_time_with_path(n, num_trials=1):
    # Generate a random graph with `n` stations and an edge probability (e.g., 0.1)
    graph = generate_random_graph(n, 0.08, True, False , True, 1, 10)

    total_time_ms = 0
    for _ in range(num_trials):
        # Pick two random stations (source and destination)
        source = randint(0, n - 1)
        destination = randint(0, n - 1)
        while destination == source:
            destination = randint(0, n - 1)

        # Start time measurement
        start_time = time.time()

        # Run Dijkstra's algorithm from the source
        distances, predecessors = dijkstra(graph, source)

        # End time measurement
        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
        total_time_ms += execution_time_ms

        # Calculate path and journey duration
        journey_duration = distances[destination]
        path = []
        current = destination
        while current is not None:
            path.append(current)
            current = predecessors[current]
        path.reverse()  # Reverse to get path from source to destination

        # Print the results for this pair
        print(f"Trial: Journey from {source} to {destination}")
        print(f"Total duration: {journey_duration} minutes")
        print(f"Path taken: {' -> '.join(map(str, path))}")
        print(f"Execution time: {execution_time_ms:.2f} ms\n")

    # Calculate average execution time across all trials
    average_time_ms = total_time_ms / num_trials
    return average_time_ms


if __name__ == "__main__":
    # Test different network sizes
    network_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    average_times = []

    for n in network_sizes:
        avg_time = calculate_average_execution_time_with_path(n)
        average_times.append(avg_time)
        print(f"Average execution time for network size {n}: {avg_time:.2f} ms\n")

    # Plotting the empirical results
    plt.figure(figsize=(10, 6))
    plt.plot(network_sizes, average_times, label="Empirical Execution Time", marker="o")

    # Theoretical time complexity curve (assuming O(E + V log V) for Dijkstra's algorithm with priority queue)
    theoretical_times = [n * (0.1 * n * 0.5 + n ** 0.5) for n in network_sizes]  # Scaled for comparison
    plt.plot(network_sizes, theoretical_times, label="Theoretical Time Complexity (Scaled)", linestyle="--")

    plt.xlabel("Network Size (n)")
    plt.ylabel("Average Execution Time (ms)")
    plt.title("Average Execution Time vs Network Size")
    plt.legend()
    plt.grid(True)
    plt.show()
