import random
import matplotlib.pyplot as plt
import numpy as np


class Maze:
    def __init__(self, width, height, seed=None, fill_rate=0.5):
        self.width = width
        self.height = height
        self.fill_rate = fill_rate

        self.grid = [['#' for _ in range(width)] for _ in range(height)]
        if seed is not None:
            random.seed(seed)

    def generate(self):
        # Placer les cases libres aléatoirement
        for i in range(1, self.height-1):
            for j in range(1, self.width-1):
                self.grid[i][j] = '#' if random.random() < self.fill_rate else '.' 

        # Placer le départ et l'arrivée
        self.grid[1][1] = 'S'
        self.grid[self.height-2][self.width-2] = 'G'

        # Garantir qu'un chemin existe (ex: utiliser un DFS simple pour créer un chemin)
        self._ensure_path()
    def _ensure_path(self):
        # Algorithme simple pour créer un chemin direct S → G
        for i in range(1, self.height-1):
            if self.grid[i][1] == 'S':
                continue
            self.grid[i][1] = '.'
        for j in range(1, self.width-1):
            if self.grid[self.height-2][j] == 'G':
                continue    
            self.grid[self.height-2][j] = '.'


    def display_maze(self, path=None):
        # Affiche le labyrinthe et éventuellement le chemin trouvé
        for i in range(self.height):
            row = ''
            for j in range(self.width):
                if path and (i,j) in path:
                    row += '* '
                else:
                    row += self.grid[i][j] + ' '
            print(row)
    
    """""
    def plot(self, path=None):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.axis('off')

        # Loop through the grid
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == '#':
                    # Draw a square wall as a filled rectangle
                    ax.add_patch(plt.Rectangle((j, self.height - i - 1), 1, 1, color='black'))

        # Optionally, mark start and goal
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == 'S':
                    ax.add_patch(plt.Rectangle((j, self.height - i - 1), 1, 1, color='green'))
                elif self.grid[i][j] == 'G':
                    ax.add_patch(plt.Rectangle((j, self.height - i - 1), 1, 1, color='red'))

        plt.show()""" 

if __name__ == "__main__":
    maze = Maze(16, 16)
    maze.generate()
    maze.display_maze()
    #maze.plot()
