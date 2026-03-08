from src.maze import Maze

def generate_maze(width=16, height=16, seed=42, fill_rate=0.5) -> Maze:
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
    print("Generation du labyrinthe :")
    print("Taille", maze.width, "x", maze.height)
    print("Seed:", maze.seed)
    print("Le taux de remplissage:", maze.fill_rate)
    print("\n")
    maze.display_maze()

def display_maze_graphical(maze: Maze, path=None, explored=None) -> None:
    """
    Display the maze graphically using matplotlib.
    """
    maze.plot(path=path, explored=explored)

def main() -> None:
    """
    Main function to run the program.
    """
    maze = generate_maze()
    display_maze_console(maze)
    #display_maze_graphical(maze)
    # Future: run_algorithms(maze) → path, explored → for GIF/Stats

if __name__ == "__main__":
    main()