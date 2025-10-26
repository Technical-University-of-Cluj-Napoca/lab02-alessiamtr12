import sys
from collections import deque


def read_maze(filename: str) -> list[list[str]]:
    """Reads a maze from a file and returns it as a list of lists (i.e. a matrix).

    Args:
        filename (str): The name of the file containing the maze.
    Returns:
        list: A 2D list (matrix) representing the maze.
    """
    with open(filename, "r") as f:
        maze = []
        for line in f:
            maze.append(list(line.strip()))
    return maze



def find_start_and_target(maze: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    """Finds the coordinates of start ('S') and target ('T') in the maze, i.e. the row and the column
    where they appear.

    Args:
        maze (list[list[str]): A 2D list (matrix) representing the maze.
    Returns:
        tuple[int, int]: A tuple containing the coordinates of the start and target positions.
        Each position is represented as a tuple (row, column).
    """
    start_pos = None
    target_pos = None

    for r, row in enumerate(maze):
        for c, col in enumerate(row):
            if col == 'S':
                start_pos = (r, c)
            if col == 'T':
                target_pos = (r, c)

    return start_pos, target_pos


def get_neighbors(maze: list[list[str]], position: tuple[int, int]) -> list[tuple[int, int]]:
    """Given a position in the maze, returns a list of valid neighboring positions: (up, down, left, right)
    where the player can be moved to. A neighbor is considered valid if (1) it is within the bounds of the maze
    and (2) not a wall ('#').

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        position (tuple[int, int]): The current position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of valid neighboring positions.
    """

    nb_rows = len(maze)
    nb_cols = len(maze[0])
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        posx = position[0] + dx
        posy = position[1] + dy
        if 0 <= posx < nb_rows and 0 <= posy < nb_cols:
            if maze[posx][posy] != '#':
                neighbors.append((posx, posy))
    return neighbors


def bfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    """Performs a breadth-first search (BFS) to find the shortest path from start to target in the maze.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        start (tuple[int, int]): The starting position in the maze as (row, column).
        target (tuple[int, int]): The target position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of positions representing the shortest path from start to target,
        including both start and target. If no path exists, returns an empty list.
    """
    if start is None or target is None:
        return []
    queue = deque()
    queue.append(start)
    visited = {start}
    came_from = {}
    came_from[start] = None
    while queue:
        current = queue.popleft()
        if current == target:
            path = []
            aux = target
            while aux is not None:
                path.append(aux)
                aux = came_from[aux]
            return path[::-1]  # reversed
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current
    return []




def dfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    """Performs a depth-first search (DFS) to find the shortest path from start to target in the maze.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        start (tuple[int, int]): The starting position in the maze as (row, column).
        target (tuple[int, int]): The target position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of positions representing the shortest path from start to target,
        including both start and target. If no path exists, returns an empty list.
    """
    # you can use a list as a stack in Python.
    if start is None or target is None:
        return []
    stack = [start]
    visited = {start}
    came_from = {}

    came_from[start] = None
    while stack:
        current = stack.pop()
        if current == target:
            path = []
            aux = target
            while aux is not None:
                path.append(aux)
                aux = came_from[aux]
            return path[::-1] #reversed
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current
    return []

def print_maze_with_path(maze: list[list[str]], path: list[tuple[int, int]]) -> None:
    """Prints the maze to the console, marking the path with '.' characters.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        path (list[tuple[int, int]]): A list of positions representing the path to be marked.
    Returns:
        None
    """
    # # ANSI escape code for red

    RED = "\033[91m"
    RESET = "\033[0m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    # encode a character with red color: RED + char + RESET

    path_set = set(path)

    for r, row in enumerate(maze):
        line_to_print = ""
        for c, char in enumerate(row):
            pos = (r, c)
            if char == 'S':
                line_to_print += f"{YELLOW}S{RESET}"
            elif char == 'T':
                line_to_print += f"{GREEN}T{RESET}"
            elif pos in path_set:
                line_to_print += f"{RED}*{RESET}"
            else:
                line_to_print += char

        print(line_to_print)

if __name__ == "__main__":
    # Example usage: py maze_search.py dfs/bfs maze.txt

    algorithm = sys.argv[1]
    filename = sys.argv[2]

    try:
        maze = read_maze(filename)
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        sys.exit(1)

    start, target = find_start_and_target(maze)
    path = []
    if algorithm == 'bfs':
        path = bfs(maze, start, target)
    elif algorithm == 'dfs':
        path = dfs(maze, start, target)
    if not path:
        print(f"No path found from Start to Target using {algorithm}.")
    else:
        print(f"Path found using {algorithm}:")
        print_maze_with_path(maze, path)