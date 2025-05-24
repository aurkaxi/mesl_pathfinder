from networkx import Graph


def traverse(G: Graph, start_node: int) -> list[int]:
    """
    Perform a depth-first search (DFS) traversal of the graph starting from the given node.

    Args:
        G (Graph): The graph to traverse.
        start_node (int): The starting node for the DFS traversal.

    Returns:
        list[int]: A list of nodes in the order they were visited during the DFS traversal.
    """
    visited = set()
    queue = [start_node]
    order: list[int] = []

    while queue:
        vertex = queue.pop(0)
        if vertex in visited:
            continue
        visited.add(vertex)
        order.append(vertex)
        for neighbor in G.neighbors(vertex):
            if neighbor not in visited:
                queue.append(neighbor)

    return order
