# -*- coding: utf-8 -*-
"""
widgets/grid_widget.py
Affiche le labyrinthe dans le scrollAreaWidgetContents via QGridLayout + QLabel.

STRATÉGIE :
  Qt Designer a déjà posé un QGridLayout (self.ui.gridLayout) sur
  scrollAreaWidgetContents. On réutilise CE layout existant —
  on n'en crée JAMAIS un deuxième.
"""

from PySide6.QtWidgets import QLabel, QWidget, QGridLayout
from PySide6.QtCore import Qt

CELL_SIZE = 28   # pixels par cellule

COLORS = {
    '#':       ("#0837f2", "#1a1e30"),   # mur
    '.':       ("#1e2234", "#161a28"),   # libre
    'S':       ("#16a085", "#0e6b5a"),   # départ  (vert)
    'G':       ("#e74c3c", "#9b2c2c"),   # arrivée (rouge)
    'visited': ("#259e1a", "#0f2d6a"),   # visité  (bleu)
    'path':    ("#f39c12", "#8a5c00"),   # chemin  (orange)
}

LABEL_STYLE = {
    'S':    "color:#ffffff; font-weight:bold; font-size:9pt;",
    'G':    "color:#ffffff; font-weight:bold; font-size:9pt;",
    'path': "color:#5d3a00; font-size:8pt;",
}


class CellWidget(QLabel):
    """Un carré coloré = une cellule du labyrinthe."""

    def __init__(self, row: int, col: int, cell_type: str, parent: QWidget = None):
        super().__init__(parent)
        self.row       = row
        self.col       = col
        self.base_type = cell_type
        self.state     = cell_type
        self.setFixedSize(CELL_SIZE, CELL_SIZE)
        self.setAlignment(Qt.AlignCenter)
        self._refresh()

    def set_state(self, state: str):
        if self.state != state:
            self.state = state
            self._refresh()

    def reset(self):
        self.set_state(self.base_type)

    def _refresh(self):
        s = self.state
        bg, border = COLORS.get(s, COLORS['.'])
        css = (
            f"background-color:{bg};"
            f"border:1px solid {border};"
            f"border-radius:2px;"
            + LABEL_STYLE.get(s, "color:transparent;")
        )
        self.setStyleSheet(css)
        self.setText(
            "S" if s == 'S' else
            "G" if s == 'G' else
            "*" if s == 'path' else
            ""
        )


class GridWidget:
    """
    Gère la grille de CellWidget dans le scrollAreaWidgetContents.

    IMPORTANT : on passe le QGridLayout déjà créé par Qt Designer
    (self.ui.gridLayout), pas le container — pour éviter tout conflit.

    Instanciation dans MainWindow :
        self.grid = GridWidget(
            layout    = self.ui.gridLayout,           # layout existant Qt Designer
            container = self.ui.scrollAreaWidgetContents  # pour setMinimumSize
        )
        self.grid.build(maze)
    """

    def __init__(self, layout: QGridLayout, container: QWidget):
        self._layout    = layout
        self._container = container
        self._cells: list[list[CellWidget]] = []

        # Vider le layout existant (il peut contenir des placeholders)
        self._clear()

        # Paramètres du layout
        self._layout.setSpacing(1)
        self._layout.setContentsMargins(6, 6, 6, 6)

    # ── API publique ──────────────────────────────────────────────────────────

    def build(self, maze: list[list[str]]):
        """Reconstruit la grille complète."""
        self._clear()

        rows = len(maze)
        cols = len(maze[0]) if rows else 0

        for r in range(rows):
            row_cells = []
            for c in range(cols):
                cell = CellWidget(r, c, maze[r][c], self._container)
                self._layout.addWidget(cell, r, c)
                row_cells.append(cell)
            self._cells.append(row_cells)

        # Redimensionner pour activer le scroll si nécessaire
        w = cols * (CELL_SIZE + 1) + 12
        h = rows * (CELL_SIZE + 1) + 12
        self._container.setMinimumSize(w, h)
        self._container.adjustSize()

    def mark_visited(self, positions):
        """Colorie un snapshot de cellules visitées (animation)."""
        for r, c in positions:
            cell = self._cells[r][c]
            if cell.base_type not in ('S', 'G'):
                cell.set_state('visited')

    def mark_path(self, path: list):
        """Colorie le chemin final."""
        for r, c in path:
            cell = self._cells[r][c]
            if cell.base_type not in ('S', 'G'):
                cell.set_state('path')

    def clear(self):
        """Remet toutes les cellules à leur couleur d'origine."""
        for row in self._cells:
            for cell in row:
                cell.reset()

    # ── Interne ───────────────────────────────────────────────────────────────

    def _clear(self):
        """Vide le layout sans supprimer le layout lui-même."""
        while self._layout.count():
            item = self._layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()
        self._cells = []