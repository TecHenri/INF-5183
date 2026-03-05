# 
from collections import deque
import time


def bfs(maze):
    """
    BFS - Breadth First Search
    Retourne:
        path : liste des coordonnées du chemin
        explored : ensemble des noeuds explorés
        execution_time : temps en millisecondes
    """

    start_time = time.time()

    start = (1, 1)  # Position de départ (S)
    goal = (maze.height-2, maze.width-2)  # Position d'arrivée (G)  

    queue = deque([start])          # FIFO
    visited = set([start])
    parent = {}                     # Pour reconstruire le chemin
    explored = []                   # Pour visualisation (ordre exploration)

    # Ordre demandé: droite, bas, gauche, haut
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        current = queue.popleft()
        explored.append(current)

        if current == goal:
            break

        x, y = current

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < maze.height and
                0 <= ny < maze.width and
                maze.grid[nx][ny] != '#' and
                (nx, ny) not in visited):

                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = current

    # Reconstruction du chemin
    path = []
    if goal in parent or goal == start:
        node = goal
        while node != start:
            path.append(node)
            node = parent[node]
        path.append(start)
        path.reverse()

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # ms

    return path, explored, execution_time