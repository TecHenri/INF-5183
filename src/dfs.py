from collections import deque
from typing import List, Set, Tuple, Optional
import time
#from maze import Maze
from matplotlib import pyplot as plt

Position = Tuple[int, int]

# -----------------------------
# Trouver S et G automatiquement
# -----------------------------
def find_positions(maze: Maze) -> Tuple[Position, Position]:
    start = None
    goal = None
    for i in range(maze.height):
        for j in range(maze.width):
            if maze.grid[i][j] == 'S':
                start = (i, j)
            elif maze.grid[i][j] == 'G':
                goal = (i, j)
    if start is None or goal is None:
        raise ValueError("Start (S) ou Goal (G) introuvable")
    return start, goal

# -----------------------------
# DFS - Depth First Search
# -----------------------------
def dfs_search(maze: Maze) -> Tuple[List[Position], List[Position], float]:
    start_time = time.time()
    start, goal = find_positions(maze)

    stack = [start]
    visited = set([start])
    parent = {}
    explored: List[Position] = []

    # Ordre: droite, bas, gauche, haut
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while stack:
        current = stack.pop()
        explored.append(current)  # Visité maintenant

        if current == goal:
            break

        x, y = current
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < maze.height and 0 <= ny < maze.width:
                if maze.grid[nx][ny] != '#' and (nx, ny) not in visited:
                    stack.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = current

    # Reconstruction du chemin
    path: List[Position] = []
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

# -----------------------------
# Affichage console
# -----------------------------
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

# -----------------------------
# Plot graphique
# -----------------------------
def plot_maze_exploration(
    maze: Maze,
    path: Optional[List[Position]] = None,
    explored: Optional[List[Position]] = None
) -> None:
    import matplotlib.pyplot as plt
    path_set = set(path) if path else set()
    explored_set = set(explored) if explored else set()

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect("equal")
    ax.axis("off")

    # fond blanc
    for i in range(maze.height):
        for j in range(maze.width):
            ax.add_patch(
                plt.Rectangle((j, maze.height - i - 1), 1, 1, facecolor="white", edgecolor="none")
            )

    # murs avec lignes fines
    for i in range(maze.height):
        for j in range(maze.width):
            if maze.grid[i][j] == "#":
                x, y = j, maze.height - i - 1
                ax.plot([x, x + 1], [y, y], color="black", linewidth=1)
                ax.plot([x, x + 1], [y + 1, y + 1], color="black", linewidth=1)
                ax.plot([x, x], [y, y + 1], color="black", linewidth=1)
                ax.plot([x + 1, x + 1], [y, y + 1], color="black", linewidth=1)

    # cases explorées
    for i, j in explored_set:
        if maze.grid[i][j] not in ("S","G"):
            ax.add_patch(plt.Rectangle((j, maze.height - i - 1), 1, 1, color="lightblue", alpha=0.6))

    # chemin final
    for i, j in path_set:
        if maze.grid[i][j] not in ("S","G"):
            ax.add_patch(plt.Rectangle((j, maze.height - i - 1), 1, 1, color="yellow", alpha=0.8))

    # départ et arrivée
    sx, sy = maze.get_start()
    gx, gy = maze.get_goal()
    ax.add_patch(plt.Rectangle((sy, maze.height - sx - 1), 1, 1, color="green"))

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
    ax.add_patch(plt.Rectangle((gy, maze.height - gx - 1), 1, 1, color="red"))

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
    plt.title("Depth-First Search (DFS) Exploration")
    plt.tight_layout()
    plt.show()

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    from maze import Maze
    maze = Maze(width=16, height=16, seed=42, fill_rate=0.5)
    maze.generate()

    path, explored, exec_time = dfs_search(maze)

    print("\n--- Exploration DFS ---")
    display_solution(maze, path, explored)

    print("\n--- Chemin DFS ---")
    print(path)

    print(f"\nNombre de noeuds explorés : {len(explored)}")
    print(f"Temps d'exécution : {exec_time:.2f} ms")

    plot_maze_exploration(maze, path=path, explored=explored)