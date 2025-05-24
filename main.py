import sys
from types import ModuleType
from typing import List

import matplotlib.pyplot as plt
import networkx as nx

from algorithms import bfs, dfs

algorithms: dict[str, tuple[ModuleType, str]] = {
    "bfs": (bfs, "Breadth-First Search"),
    "dfs": (dfs, "Depth-First Search"),
}


def visualize_search(
    order: List[int],
    title: str,
    G: nx.Graph,
    pos: dict,
):
    """
    Visualizes the step-by-step process of a graph search algorithm.

    Args:
        order (List[int]): The sequence of node indices visited during the search.
        title (str): The title for the plot.
        G (nx.Graph): The NetworkX graph to visualize.
        pos (dict): A dictionary mapping nodes to their positions for drawing.

    The function animates the search process by highlighting previously visited nodes in orange,
    the currently visited node in red, and displaying the list of visited nodes at each step.
    """
    plt.figure(figsize=(8, 6))
    plt.title(title)
    nx.draw(
        G, pos, with_labels=True, node_color="lightblue", node_size=700, font_size=16
    )
    prev_visited = set()
    for idx, visited in enumerate(order):
        new_nodes = {visited} - prev_visited
        if prev_visited:
            nx.draw_networkx_nodes(
                G, pos, nodelist=list(prev_visited), node_color="orange"
            )
        if new_nodes:
            nx.draw_networkx_nodes(G, pos, nodelist=list(new_nodes), node_color="red")
        # Show currently visited list
        plt.gcf().texts.clear()
        plt.text(
            0,
            0,
            f"Visited: {order[: idx + 1]}",
            fontsize=14,
            transform=plt.gca().transAxes,
            bbox=dict(facecolor="white", edgecolor="gray"),
        )
        plt.pause(1.5)
        prev_visited.add(visited)
    plt.show()


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
