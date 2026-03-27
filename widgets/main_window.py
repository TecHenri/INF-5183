# -*- coding: utf-8 -*-
"""
widgets/main_window.py
Assemble UI + GridWidget + Controller.
"""

import sys, os

from PySide6.QtWidgets import QMainWindow

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _p in [_ROOT, os.path.join(_ROOT, "ui"), os.path.join(_ROOT, "src")]:
    if _p not in sys.path:
        sys.path.insert(0, _p)

from ui.ui_main_window  import Ui_MainWindow
from widgets.grid_widget import GridWidget
from widgets.controller  import MazeController


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. UI générée par Qt Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 2. GridWidget : on lui passe le QGridLayout EXISTANT (self.ui.gridLayout)
        #    et le container pour le redimensionnement (scrollAreaWidgetContents)
        self.grid = GridWidget(
            layout    = self.ui.gridLayout,
            container = self.ui.scrollAreaWidgetContents,
        )

        # 3. Contrôleur
        self.controller = MazeController(self.ui, self.grid)