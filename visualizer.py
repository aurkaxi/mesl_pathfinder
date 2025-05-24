from typing import List

import matplotlib.pyplot as plt
import networkx as nx


def visualize_search(
    order: List,
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
    for visited in order:
        new_nodes = visited - prev_visited
        if prev_visited:
            nx.draw_networkx_nodes(
                G, pos, nodelist=list(prev_visited), node_color="orange"
            )
        if new_nodes:
            nx.draw_networkx_nodes(G, pos, nodelist=list(new_nodes), node_color="red")
        # Show currently visited list
        plt.gcf().texts.clear()
        plt.text(
            0.05,
            0.95,
            f"Visited: {sorted(visited)}",
            fontsize=14,
            transform=plt.gca().transAxes,
            verticalalignment="top",
            bbox=dict(facecolor="white", alpha=0.7, edgecolor="gray"),
        )
        plt.pause(1.5)
        prev_visited = set(visited)
    plt.show()
