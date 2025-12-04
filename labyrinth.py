from bfs import Graph, bfs

type Maze = list[list[int]]


def shortest_path_in_maze(maze: Maze) -> list[tuple[int, int]]:
    starting_point = (0, 0)
    ending_point = (len(maze[0]) - 1, len(maze) - 1)
    nodes, nodes_to_coordinates = maze_to_graph(maze)
    shortest_path_in_nodes = bfs(nodes, nodes_to_coordinates.index(starting_point), nodes_to_coordinates.index(ending_point))

    return [nodes_to_coordinates[node] for node in shortest_path_in_nodes]


def maze_to_graph(maze: Maze) -> tuple[Graph, list[tuple[int, int]]]:
    nodes: Graph = dict()
    nodes_to_coordinates: list[tuple[int, int]] = []
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                continue

            current_node = (x, y)
            if current_node not in nodes_to_coordinates:
                nodes_to_coordinates.append(current_node)
            current_node = nodes_to_coordinates.index(current_node)

            neighbours = get_neighbours(maze, x, y)
            for neighbour in neighbours:
                if neighbour not in nodes_to_coordinates:
                    nodes_to_coordinates.append(neighbour)
                nodes[current_node] = nodes.get(current_node, []) + [nodes_to_coordinates.index(neighbour)]

    return nodes, nodes_to_coordinates

def get_neighbours(maze: Maze, x: int, y: int) -> list[tuple[int, int]]:
    neighbours = []
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for direction in directions:
        direction_x = x + direction[0]
        direction_y = y + direction[1]
        if not (0 <= direction_y < len(maze) and 0 <= direction_x < len(maze[direction_y])):
            continue
        if maze[direction_y][direction_x] == 0:
            neighbours.append((direction_x, direction_y))

    return neighbours


if __name__ == "__main__":
    maze = [
        [0, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 1, 0]
    ]
    print(shortest_path_in_maze(maze))