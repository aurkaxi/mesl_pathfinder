from typing import List

import matplotlib.pyplot as plt
import networkx as nx


def visualize_search(
    order: List[int],
    title: str,
    G: nx.Graph,
    pos: dict,
):
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
