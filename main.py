from src.maze import Maze
from src.bfs import bfs_search, display_solution as display_solution_bfs, plot_maze_exploration as plot_maze_exploration_bfs
from src.dfs import dfs_search, display_solution as display_solution_dfs, plot_maze_exploration as plot_maze_exploration_dfs
from src.astar import astar_search, display_solution as display_solution_astar, plot_maze_exploration as plot_maze_exploration_astar

def generate_maze(width: int = 16, height: int = 16, seed: int = 42, fill_rate: float = 0.5) -> Maze:
    """
    Create and generate a maze.
    """
    maze = Maze(width=width, height=height, seed=seed, fill_rate=fill_rate)
    maze.generate()
    return maze


def display_maze_console(maze: Maze) -> None:
    """
    Display the maze in the terminal.
    """

    print("\n==============================")
    print("Generation du labyrinthe :")
    print("==============================\n")
    print("Taille:", maze.width, "x", maze.height)
    print("Seed:", maze.seed)
    print("Fill rate:", maze.fill_rate)
    print()
    maze.display_maze()


def display_solution_console(maze: Maze, path, explored) -> None:
    """
    Display explored nodes and path in console.
    p = explored
    * = final path
    """
    print()
    maze.display_solution(maze, path, explored)
    

def display_maze_graphical(maze: Maze, path=None, explored=None) -> None:
    """
    Display the maze graphically using matplotlib.
    """

    maze.plot_maze_exploration (path=path, explored=explored)


def run_algorithm(maze: Maze, name: str, algo_func, display_func, graph_func) -> None:
    """
    Run a search algorithm and display results.
    """
    print("\n==============================")
    print(f"Algorithm: {name}")
    print("==============================")

    path, explored, execution_time = algo_func(maze)

    display_func(maze, path, explored)

    print("\nChemin trouvé :")
    print(path)

    print("\nNombre de noeuds explorés :", len(explored))
    print("\nLongueur du chemin trouvé :", len(path))
    print(f"Temps d'exécution : {execution_time:.2f} ms")

    choice = input("\nVoulez-vous visualiser le graphe du labyrinthe ? (o/n) : ").lower()

    if choice == "o" or choice == "oui":
        graph_func(maze, path=path, explored=explored)
    else:
        print("Visualisation ignorée.")

    
def main() -> None:
    """
    Main function to run the program.
    """
    maze = generate_maze()

    display_maze_console(maze)

    # BFS
    run_algorithm(maze, "BFS", bfs_search, display_solution_bfs, plot_maze_exploration_bfs)

    # DFS
    run_algorithm(maze, "DFS", dfs_search, display_solution_dfs, plot_maze_exploration_dfs)

    # A*
    run_algorithm(maze, "A*", astar_search, display_solution_astar, plot_maze_exploration_astar)


if __name__ == "__main__":
    main()