from queue import Queue

from bfs import edges_to_nodes, Graph


def is_graph_coherent(nodes_with_adjacency: Graph) -> bool:
    nodes = nodes_with_adjacency.keys()
    if possible_destinations(min(nodes), nodes_with_adjacency) != nodes:
        return False

    return True

def possible_destinations(node: int, nodes_with_adjacency: Graph) -> set[int]:
    possible_destinations = set()
    node_queue = Queue()
    node_queue.put(node)

    while not node_queue.empty():
        current_node = node_queue.get()
        adjacent_nodes = nodes_with_adjacency[current_node]
        if possible_destinations == nodes_with_adjacency.keys():
            break
        for node in adjacent_nodes:
            if node not in possible_destinations:
                node_queue.put(node)
                possible_destinations.add(node)

    return possible_destinations


if __name__ == "__main__":
    print(is_graph_coherent(edges_to_nodes([(0,1),(0,2),(0,3),(1,3),(2,4),(3,5)])))