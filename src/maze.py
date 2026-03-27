import random
from typing import List, Tuple, Optional, Set

import matplotlib.pyplot as plt

# Type alias pour représenter une position dans la grille
Position = Tuple[int, int]


class Maze:
    """
    Classe représentant un labyrinthe.

    Le labyrinthe est une grille contenant :
    '#' : mur
    '.' : passage
    'S' : position de départ
    'G' : position d'arrivée

    Le labyrinthe est généré avec l'algorithme Randomized Prim.
    """

    def __init__(
        self,
        width: int = 16,
        height: int = 16,
        seed: Optional[int] = None,
        fill_rate: float = 0.5,
    ) -> None:
        """
        Initialise les paramètres du labyrinthe.

        Args:
            width: largeur du labyrinthe
            height: hauteur du labyrinthe
            seed: graine aléatoire pour reproductibilité
            fill_rate: densité des murs (0 → peu de murs, 1 → très dense)
        """
        self.width = width
        self.height = height
        self.seed = seed
        self.fill_rate = fill_rate
        self.grid: List[List[str]] = []

        if self.seed is not None:
            random.seed(self.seed)

    def generate(self) -> None:
        """Génère le labyrinthe."""
        self._generate_maze()

    def get_start(self) -> Position:
        """Retourne la position de départ."""
        return (1, 1)

    def get_goal(self) -> Position:
        """Retourne la position d'arrivée."""
        return (self.height - 2, self.width - 2)

    def is_wall(self, pos: Position) -> bool:
        """
        Vérifie si une position correspond à un mur.
        """
        x, y = pos
        return self.grid[x][y] == "#"

    def get_neighbors(self, pos: Position) -> List[Position]:
        """
        Retourne les voisins accessibles (non murs).

        Args:
            pos: position courante

        Returns:
            Liste des positions voisines accessibles.
        """

        x, y = pos
        neighbors: List[Position] = []

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < self.height and 0 <= ny < self.width:
                if self.grid[nx][ny] != "#":
                    neighbors.append((nx, ny))

        return neighbors

    def display_maze(
        self,
        path: Optional[List[Position]] = None,
        explored: Optional[Set[Position]] = None,
    ) -> None:
        """
        Affiche le labyrinthe dans la console.

        Args:
            path: chemin trouvé par un algorithme
            explored: noeuds explorés
        """

        path_set = set(path) if path else set()
        explored_set = set(explored) if explored else set()

        for i in range(self.height):
            row = ""

            for j in range(self.width):
                cell = self.grid[i][j]

                if (i, j) in path_set and cell not in ("S", "G"):
                    row += "* "
                elif (i, j) in explored_set and cell not in ("S", "G"):
                    row += "p "
                else:
                    row += cell + " "

            print(row)

    def plot(
    self,
    path: Optional[List[Position]] = None,
    explored: Optional[Set[Position]] = None,
) -> None:

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_aspect("equal")
        ax.axis("off")

        path_set = set(path) if path else set()
        explored_set = set(explored) if explored else set()

        # fond blanc
        for i in range(self.height):
            for j in range(self.width):

                ax.add_patch(
                    plt.Rectangle(
                        (j, self.height - i - 1),
                        1,
                        1,
                        facecolor="white",
                        edgecolor="none",
                    )
                )

        # tracer les murs avec des lignes fines
        for i in range(self.height):
            for j in range(self.width):

                if self.grid[i][j] == "#":

                    x = j
                    y = self.height - i - 1

                    ax.plot([x, x + 1], [y, y], color="black", linewidth=1)
                    ax.plot([x, x + 1], [y + 1, y + 1], color="black", linewidth=1)
                    ax.plot([x, x], [y, y + 1], color="black", linewidth=1)
                    ax.plot([x + 1, x + 1], [y, y + 1], color="black", linewidth=1)

        # cellules explorées
        for i, j in explored_set:
            if self.grid[i][j] not in ("S", "G"):
                ax.add_patch(
                    plt.Rectangle(
                        (j, self.height - i - 1),
                        1,
                        1,
                        color="lightblue",
                        alpha=0.6,
                    )
                )

        # chemin final
        for i, j in path_set:
            if self.grid[i][j] not in ("S", "G"):
                ax.add_patch(
                    plt.Rectangle(
                        (j, self.height - i - 1),
                        1,
                        1,
                        color="yellow",
                        alpha=0.8,
                    )
                )

        # départ et arrivée
        sx, sy = self.get_start()
        gx, gy = self.get_goal()

        ax.add_patch(
            plt.Rectangle((sy, self.height - sx - 1), 1, 1, color="green")
        )

        ax.text(
            sy + 0.5,
            self.height - sx - 0.5,
            "S",
            ha="center",
            va="center",
            fontsize=16,
            color="white",
            weight="bold"
        )

        ax.add_patch(
            plt.Rectangle((gy, self.height - gx - 1), 1, 1, color="red")
        )

        ax.text(
            gy + 0.5,
            self.height - gx - 0.5,
            "G",
            ha="center",
            va="center",
            fontsize=16,
            color="white",
            weight="bold"
        )

        plt.xlim(0, self.width)
        plt.ylim(0, self.height)

        plt.title(f"Maze Visualization {self.width}x{self.height}", fontsize=18)
        plt.tight_layout()
        plt.show()

    def _generate_maze(self) -> None:
        """
        Génère la structure du labyrinthe avec Randomized Prim.
        """

        # grille finale remplie de murs
        self.grid = [["#"] * self.width for _ in range(self.height)]

        # dimensions internes (impaires pour l'algorithme)
        internal_w = self.width if self.width % 2 == 1 else self.width - 1
        internal_h = self.height if self.height % 2 == 1 else self.height - 1

        grid = [["#"] * internal_w for _ in range(internal_h)]

        # cellule initiale
        grid[1][1] = "."

        walls: List[Tuple[int, int, int, int]] = []

        # déplacements possibles dans la grille
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

        # initialisation des murs candidats
        for dx, dy in directions:
            nx = 1 + dx
            ny = 1 + dy

            if 1 <= nx < internal_h - 1 and 1 <= ny < internal_w - 1:
                walls.append((nx, ny, 1 + dx // 2, 1 + dy // 2))

        while walls:

            wx, wy, bx, by = random.choice(walls)
            walls.remove((wx, wy, bx, by))

            if grid[wx][wy] == "#":

                # creuser le mur
                grid[wx][wy] = "."
                grid[bx][by] = "."

                # ajouter les nouveaux murs candidats
                for dx, dy in directions:

                    nx = wx + dx
                    ny = wy + dy

                    if 1 <= nx < internal_h - 1 and 1 <= ny < internal_w - 1:
                        if grid[nx][ny] == "#":
                            walls.append((nx, ny, wx + dx // 2, wy + dy // 2))

        # copie dans la grille finale
        for i in range(internal_h):
            for j in range(internal_w):
                self.grid[i][j] = grid[i][j]

        start = self.get_start()
        goal = self.get_goal()

        self.grid[start[0]][start[1]] = "S"
        
        self.grid[goal[0]][goal[1]] = "G"

        # Surppresion de murs doubles 
        self._fix_last_inner_row()

         # garantir que la case goal est accessible

        if self.grid[goal[0] - 1][goal[1]] == "#":
            self.grid[goal[0] - 1][goal[1]] = "."

        if self.grid[goal[0]][goal[1]-1] == "#":
            self.grid[goal[0] ][goal[1]-1] = "."
        


        

        # ajustement de la densité du labyrinthe
        if self.fill_rate > 0.5:
            intensity = (self.fill_rate - 0.5) * 2
            self._add_walls(intensity)

        elif self.fill_rate < 0.5:
            intensity = (0.5 - self.fill_rate) * 2
            self._remove_walls(intensity)

    def _add_walls(self, intensity: float) -> None:
        """
        Ajoute des murs pour augmenter la densité du labyrinthe.
        """

        start = self.get_start()
        goal = self.get_goal()

        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):

                if (i, j) in (start, goal):
                    continue

                if self.grid[i][j] == "." and random.random() < intensity:
                    self.grid[i][j] = "#"

    def _remove_walls(self, intensity: float) -> None:
        """
        Supprime certains murs pour rendre le labyrinthe plus ouvert.
        """

        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):

                if self.grid[i][j] == "#" and random.random() < intensity:
                    self.grid[i][j] = "."
    
    def _fix_last_inner_row(self) -> None:
        """
        Modifie l'avant-dernière ligne pour éviter une double paroi
        avec la bordure inférieure du labyrinthe.
        """

        bottom_row = self.height - 2
        right_row = self.width - 2

        for col in range(1, self.width - 2):

            # ne jamais modifier la case goal
            #if self.grid[bottom_row][col] == "G":
            #    continue

            # génération aléatoire basée sur fill_rate
            if random.random() < self.fill_rate:
                self.grid[bottom_row][col] = "#"
            else:
                self.grid[bottom_row][col] = "."
        
        for col in range(1, self.width - 2):

            # ne jamais modifier la case goal
            #if self.grid[col][right_row] == "G":
            #    continue

            # génération aléatoire basée sur fill_rate
            if random.random() < self.fill_rate:
                self.grid[col][right_row] = "#"
            else:
                self.grid[col][right_row] = "."

# ------------------------------------------------- 
# Test 
# ------------------------------------------------- 
if __name__ == "__main__": 
    maze = Maze(width=16,height=16, seed=42)
    maze.generate() 
    #maze.display_maze()
    maze.plot()