# London Tube Network Journey Planner

This repository contains the source code for a project focused on modeling and analyzing the London Underground system. It was developed as part of the COMP1828 – Advanced Algorithms and Data Structures module at the University of Greenwich.

The project is organized around four key tasks, each applying graph algorithms and data analysis techniques to simulate and explore journey planning scenarios across the Tube network.

---

## Tasks Overview

- **Task 1a**: Constructs a small graph with five stations and applies Dijkstra’s algorithm to find the shortest path in terms of journey time. Prints both the optimal path and total duration.

- **Task 1b**: Expands the approach from Task 1a to work on randomly generated networks. Measures and reports the algorithm's execution time on larger graphs.

- **Task 2a**: Reuses the structure from Task 1a but treats all edges equally (each set to weight 1), calculating the shortest path based on the number of stops rather than time.

- **Task 2b**: Measures the performance of the approach from Task 2a on larger random networks, reporting execution time for various graph sizes.

- **Task 3a**: Parses real-world station and journey data from an Excel file and builds a weighted graph. Calculates journey times between all pairs of stations, identifies the longest journey by time, and generates a histogram to visualize the overall distribution.

- **Task 3b**: Similar to 3a but based on stop counts instead of journey time. Identifies the journey with the highest number of stops and produces a corresponding histogram.

- **Task 4**: Uses Kruskal’s algorithm to determine which connections in the Tube network can be removed while preserving full network connectivity. Constructs a Minimum Spanning Tree (MST), lists closed connections, and compares journey durations before and after closures through both histogram analysis and path comparison.

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/isyiraliyah/london-underground-journey-planner
cd london-underground-journey-planner
```

2. **Install required packages:**

```bash
pip install pandas matplotlib openpyxl numpy
```

3. Ensure `London Underground data.xlsx` is in the root directory if running Task 3 or Task 4.

---

## Usage

Run each task independently using Python:

```bash
python task_1a.py
```

### Example Outputs:

- `task_1a.py` → Displays shortest path and journey time using a toy dataset.
- `task_1b.py` → Prints algorithm runtime on random networks of increasing size.
- `task_2a.py` → Calculates shortest path in number of stops.
- `task_2b.py` → Measures and displays performance on large stop-based graphs.
- `task_3a.py` → Outputs longest time-based journey and histogram of journey durations.
- `task_3b.py` → Outputs longest stop-based journey and histogram of stop counts.
- `task_4.py` → Displays MST results, removed connections, updated longest journey, and new histogram.

---

## Credits

This coursework project was developed by **isyiraliyah**, submitted to the **University of Greenwich**.
All graph algorithm implementations where required were adapted from the official **CLRS Python library** provided for this module.

---

## License

This repository is made available for academic and portfolio use. It is not licensed for commercial redistribution.

---

## Contact

© 2024 Aliyah – All Rights Reserved.
