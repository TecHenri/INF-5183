# bfs_solver.py
import matplotlib.pyplot as plt
from collections import deque
import time
from typing import List, Tuple, Optional
#from maze import Maze


def find_positions(maze: Maze) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Trouve automatiquement S (start) et G (goal) dans le labyrinthe.
    """
    start: Optional[Tuple[int, int]] = None
    goal: Optional[Tuple[int, int]] = None

    for i in range(maze.height):
        for j in range(maze.width):
            if maze.grid[i][j] == 'S':
                start = (i, j)
            elif maze.grid[i][j] == 'G':
                goal = (i, j)

    if start is None or goal is None:
        raise ValueError("Start (S) ou Goal (G) introuvable dans le labyrinthe")

    return start, goal


def bfs_search(maze: Maze) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]], float]:
    """
    BFS - Breadth First Search
    Retourne:
        path : liste des coordonnées du chemin
        explored : liste des noeuds explorés
        execution_time : temps en millisecondes
    """
    start_time = time.time()
    start, goal = find_positions(maze)

    queue: deque = deque([start])
    visited: set = set([start])
    parent: dict = {}

    explored: List[Tuple[int, int]] = []

    # ordre demandé : droite, bas, gauche, haut
    directions: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        current = queue.popleft()
        explored.append(current)

        if current == goal:
            break

        x, y = current

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < maze.height and 0 <= ny < maze.width:
                if maze.grid[nx][ny] != '#' and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = current

    # reconstruction du chemin
    path: List[Tuple[int, int]] = []
    if goal in parent or goal == start:
        node = goal
        while node != start:
            path.append(node)
            node = parent[node]
        path.append(start)
        path.reverse()

    execution_time = (time.time() - start_time) * 1000
    return path, explored, execution_time


def display_solution(maze: Maze, path: List[Position], explored: List[Position]) -> None:
    """
    Affiche le labyrinthe avec:
        - p pour exploration
        - * pour chemin
    """
    path_set = set(path)
    explored_set = set(explored)

    for i in range(maze.height):
        row = ""
        for j in range(maze.width):
            cell = maze.grid[i][j]
            pos = (i, j)
            if pos in path_set and cell not in ('S','G'):
                row += "* "
            elif pos in explored_set and cell not in ('S','G'):
                row += "p "
            else:
                row += cell + " "
        print(row)

'''
def plot_exploration(maze: Maze, explored: List[Tuple[int,int]], path: List[Tuple[int,int]]=None):
    """
    Affiche le labyrinthe avec :
        - Cases explorées (explored) en bleu clair
        - Chemin final (path) en jaune
        - S en vert et G en rouge
    """
    path = set(path) if path else set()
    explored = set(explored) if explored else set()

    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_aspect('equal')
    ax.axis('off')

    for i in range(maze.height):
        for j in range(maze.width):
            cell = maze.grid[i][j]

            if cell == '#':
                color = 'black'
            elif cell == 'S':
                color = 'green'
            elif cell == 'G':
                color = 'red'
            else:
                color = 'white'

            ax.add_patch(plt.Rectangle((j, maze.height-i-1), 1, 1, color=color, linewidth=1, edgecolor='black'))

    # Cases explorées
    for (i,j) in explored:
        if maze.grid[i][j] not in ('S','G'):
            ax.add_patch(plt.Rectangle((j, maze.height-i-1), 1, 1, color='lightblue', linewidth=1, edgecolor='black'))

    # Chemin final
    for (i,j) in path:
        if maze.grid[i][j] not in ('S','G'):
            ax.add_patch(plt.Rectangle((j, maze.height-i-1), 1, 1, color='yellow', linewidth=1, edgecolor='black'))

    # Légendes S et G
    sx, sy = maze.get_start()
    gx, gy = maze.get_goal()
    ax.text(sy + 0.5, maze.height - sx - 0.5, 'S', ha='center', va='center', fontsize=16, color='white', weight='bold')
    ax.text(gy + 0.5, maze.height - gx - 0.5, 'G', ha='center', va='center', fontsize=16, color='white', weight='bold')

    plt.title("Maze Exploration")
    plt.xlim(0, maze.width)
    plt.ylim(0, maze.height)
    plt.tight_layout()
    plt.show()'''


def plot_maze_exploration(
    maze: Maze,
    path: Optional[List[Position]] = None,
    explored: Optional[Set[Position]] = None,
) -> None:
    """
    Affiche le labyrinthe avec :
    - Murs en lignes fines
    - Cases explorées en bleu clair
    - Chemin final en jaune
    - S en vert et G en rouge
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect("equal")
    ax.axis("off")

    path_set = set(path) if path else set()
    explored_set = set(explored) if explored else set()

    # Fond blanc
    for i in range(maze.height):
        for j in range(maze.width):
            ax.add_patch(
                plt.Rectangle(
                    (j, maze.height - i - 1),
                    1,
                    1,
                    facecolor="white",
                    edgecolor="none",
                )
            )

    # Tracer les murs avec des lignes fines
    for i in range(maze.height):
        for j in range(maze.width):
            if maze.grid[i][j] == "#":
                x, y = j, maze.height - i - 1
                ax.plot([x, x + 1], [y, y], color="black", linewidth=1)
                ax.plot([x, x + 1], [y + 1, y + 1], color="black", linewidth=1)
                ax.plot([x, x], [y, y + 1], color="black", linewidth=1)
                ax.plot([x + 1, x + 1], [y, y + 1], color="black", linewidth=1)

    # Cases explorées
    for i, j in explored_set:
        if maze.grid[i][j] not in ("S", "G"):
            ax.add_patch(
                plt.Rectangle(
                    (j, maze.height - i - 1),
                    1,
                    1,
                    color="yellow",
                    alpha=0.6,
                )
            )

    # Chemin final
    for i, j in path_set:
        if maze.grid[i][j] not in ("S", "G"):
            ax.add_patch(
                plt.Rectangle(
                    (j, maze.height - i - 1),
                    1,
                    1,
                    color="lightblue",
                    alpha=0.8,
                )
            )

    # Départ et arrivée
    sx, sy = maze.get_start()
    gx, gy = maze.get_goal()

    ax.add_patch(
        plt.Rectangle((sy, maze.height - sx - 1), 1, 1, color="green")
    )
    ax.text(
            sy + 0.5,
            maze.height - sx - 0.5,
            "S",
            ha="center",
            va="center",
            fontsize=16,
            color="white",
            weight="bold"
        )
    ax.add_patch(
        plt.Rectangle((gy, maze.height - gx - 1), 1, 1, color="red")
    )
    ax.text(
            gy + 0.5,
            maze.height - gx - 0.5,
            "G",
            ha="center",
            va="center",
            fontsize=16,
            color="white",
            weight="bold"
        )

    plt.xlim(0, maze.width)
    plt.ylim(0, maze.height)
    plt.title("Breadth-First Search (BFS) Exploration")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    from maze import Maze

    # Paramètres configurables
    maze = Maze(width=16, height=16, seed=42, fill_rate=0.3)
    maze.generate()

    path, explored, execution_time = bfs_search(maze)

    print(f"Chemin trouvé : {path}")
    print(f"Longueur du chemin : {len(path)}")
    print(f"Nombre de noeuds explorés : {len(explored)}")
    print(f"Temps d'exécution : {execution_time:.2f} ms\n")

    #display_solution(maze, path)
    plot_maze_exploration(maze, explored, path)