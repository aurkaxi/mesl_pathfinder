from queue import Queue
from typing import Any

from networkx import Graph


def traverse(G: Graph, start_node: int) -> list[Any]:
    visited = set()
    q = Queue()
    q.put(start_node)
    order: list = []

    while not q.empty():
        vertex = q.get()
        if vertex in visited:
            continue
        visited.add(vertex)
        order.append(vertex)
        for neighbor in G.neighbors(vertex):
            if neighbor not in visited:
                q.put(neighbor)
    return order
