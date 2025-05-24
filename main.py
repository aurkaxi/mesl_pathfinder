import sys
from types import ModuleType

import networkx as nx

from algorithms import bfs
from visualizer import visualize_search

algorithms: dict[str, tuple[ModuleType, str]] = {
    "bfs": (bfs, "Breadth-First Search"),
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an algorithm name (e.g., bfs).")
        sys.exit(1)
    algo_name = sys.argv[1]
    if algo_name not in algorithms:
        print(f"Algorithm '{algo_name}' not found.")
        sys.exit(1)

    node_count = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    edge_count = int(sys.argv[3]) if len(sys.argv) > 3 else 5

    Graph = nx.gnm_random_graph(node_count, edge_count)

    pos = dict(nx.spring_layout(Graph))

    order = algorithms[algo_name][0].traverse(Graph, 0)
    visualize_search(order, algorithms[algo_name][1], Graph, pos)
