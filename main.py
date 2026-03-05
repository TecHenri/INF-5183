from maze import Maze
from bfs import bfs

def main():
    maze = Maze(8, 8, seed=42)
    maze.generate()
    maze.display_maze()

    path, explored, exec_time = bfs(maze)

    print("Nombre de noeuds explorés :", len(explored))
    print("Longueur du chemin :", path)
    print("Temps d'exécution (ms) :", exec_time)

    # maze.plot(path=path, explored=explored)

if __name__ == "__main__":
    main()