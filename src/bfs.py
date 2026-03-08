from collections import deque
import time
from maze import Maze


def find_positions(maze):
    """
    Trouve automatiquement S et G dans la grille
    """
    start = None
    goal = None

    for i in range(maze.height):
        for j in range(maze.width):
            if maze.grid[i][j] == 'S':
                start = (i, j)
            elif maze.grid[i][j] == 'G':
                goal = (i, j)

    return start, goal


def bfs(maze):
    """
    BFS - Breadth First Search

    Retourne:
        path : liste des coordonnées du chemin
        explored : liste des noeuds explorés
        execution_time : temps en millisecondes
    """

    start_time = time.time()

    start, goal = find_positions(maze)

    if start is None or goal is None:
        raise ValueError("Start (S) ou Goal (G) introuvable dans le labyrinthe")

    queue = deque([start])
    visited = set([start])
    parent = {}

    explored = []

    # ordre demandé : droite, bas, gauche, haut
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    while queue:

        current = queue.popleft()
        explored.append(current)

        if current == goal:
            break

        x, y = current

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if (
                0 <= nx < maze.height and
                0 <= ny < maze.width and
                maze.grid[nx][ny] != '#' and
                (nx, ny) not in visited
            ):

                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = current

    # reconstruction du chemin
    path = []

    if goal in parent or goal == start:

        node = goal

        while node != start:
            path.append(node)
            node = parent[node]

        path.append(start)
        path.reverse()

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000

    return path, explored, execution_time

def display_solution(maze, path):

    grid_copy = [row[:] for row in maze.grid]

    for x, y in path:
        if grid_copy[x][y] not in ('S', 'G'):
            grid_copy[x][y] = '+'

    for row in grid_copy:
        print(" ".join(row))

if __name__ == "__main__":

    maze = Maze(width=16, height=16, fill_rate=0.5)
    maze.generate()

    path, explored, execution_time = bfs(maze)

    print(f"Chemin trouvé : {path}")
    print(f"Nombre de noeuds explorés : {len(explored)}")
    print(f"Temps d'exécution : {execution_time:.2f} ms")

    display_solution(maze, path)