from queue import Queue
from typing import Optional


def edges_to_nodes(edges: list[tuple[int, int]]) -> dict[int, list[int]]:
    nodes: dict[int, list[int]] = {}
    for edge in edges:
        nodes[edge[0]] = nodes.get(edge[0], []) + [edge[1]]
        nodes[edge[1]] = nodes.get(edge[1], []) + [edge[0]]

    return nodes


def bfs(nodes: dict[int, list[int]], start_node: Optional[int]=0, end_node: Optional[int]=None) -> list[int]:
    node_queue: Queue[int] = Queue()
    node_queue.put(start_node)
    destination = max(nodes.keys()) if end_node is None else end_node
    visited_nodes: set[int] = {0}
    parent_nodes: dict[int, int] = {}

    while node_queue.not_empty:
        current_node = node_queue.get()
        adjacent_nodes = nodes[current_node]
        if current_node == destination:
            break
        for node in adjacent_nodes:
            if node not in visited_nodes:
                parent_nodes[node] = current_node
                node_queue.put(node)
                visited_nodes.add(node)
    route = []
    while current_node != start_node:
        route.append(current_node)
        current_node = parent_nodes[current_node]

    route.append(start_node)

    return route[::-1]


if __name__ == "__main__":
    print(bfs(edges_to_nodes([(0,1),(0,2),(0,3),(1,3),(2,4),(3,4),(3,5),(2,3)])))