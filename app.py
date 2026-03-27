
import sys
import os

# Rendre tous les sous-packages importables
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PySide6.QtWidgets import QApplication
from widgets.main_window import MainWindow
from PySide6.QtWidgets import QApplication, QStyle



def main():
    app = QApplication(sys.argv)

    app.setStyle("Fusion")
    app.setApplicationName("Maze Solver")
    app.setApplicationVersion("1.0")
    app.setOrganizationName("UQO - INF-5183")
    app.setOrganizationDomain("uqo.ca")

    # ✅ CORRECTION ICI
    app.setWindowIcon(app.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()