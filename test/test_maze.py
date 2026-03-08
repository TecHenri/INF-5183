from src.maze import Maze

def test_maze_generation():

    maze = Maze(width=10, height=10, seed=42)

    maze.generate()

    assert len(maze.grid) == 10
    assert len(maze.grid[0]) == 10


def test_start_and_goal():

    maze = Maze(width=10, height=10, seed=42)

    maze.generate()

    start = maze.get_start()
    goal = maze.get_goal()

    assert maze.grid[start[0]][start[1]] == "S"
    assert maze.grid[goal[0]][goal[1]] == "G"


def test_neighbors():

    maze = Maze(width=10, height=10)

    maze.generate()

    start = maze.get_start()

    neighbors = maze.get_neighbors(start)

    assert isinstance(neighbors, list)


def test_is_wall():

    maze = Maze(width=10, height=10, seed=42)

    maze.generate()

    assert maze.is_wall((0, 0)) is True