
from tracemalloc import start

def dfs(maze):
    stack = [(1, 1)]  # Position de départ (S)              # Pile LIFO
    goal = (maze.height-2, maze.width-2)  # Position d'arrivée (G)  
    visited = set()              # Cases déjà visitées
    parent = {}                  # Pour reconstruire le chemin
    exploration_order = []       # Ordre d'exploration

    while stack:
        current = stack.pop()    # On prend le dernier ajouté

        if current in visited:
            continue

        visited.add(current)
        exploration_order.append(current)

        # Si on atteint le but
        if current == goal:
            break

        x, y = current

        # Ordre demandé : droite, bas, gauche, haut
        neighbors = [
            (x, y+1),   # droite
            (x+1, y),   # bas
            (x, y-1),   # gauche
            (x-1, y)    # haut
        ]

        for nx, ny in neighbors:
            if (0 <= nx < len(maze) and
                0 <= ny < len(maze[0]) and
                maze[nx][ny] != '#' and
                (nx, ny) not in visited):

                stack.append((nx, ny))
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

    return exploration_order, path