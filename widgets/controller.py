# -*- coding: utf-8 -*-
"""
widgets/controller.py
Contrôleur MVC : orchestre l'UI (Ui_MainWindow), le GridWidget
et les algorithmes de src/ (maze, bfs, dfs, astar).
"""

import sys
import os
import time
import random
from collections import deque
import heapq

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QFileDialog, QMessageBox

# ── Ajouter src/ au path ──────────────────────────────────────────────────────
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_SRC  = os.path.join(_ROOT, "src")
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)

# ── Import des modules src/ (avec fallback intégré) ───────────────────────────
try:
    from src.maze import Maze
    _HAS_MAZE = True
except ImportError:
    _HAS_MAZE = False

try:
    from src.bfs import bfs_search 
    _HAS_BFS = True
except ImportError:
    _HAS_BFS = False

try:
    from src.dfs import dfs_search
    _HAS_DFS = True
except ImportError:
    _HAS_DFS = False

try:
    from src.astar import astar_search
    _HAS_ASTAR = True
except ImportError:
    _HAS_ASTAR = False


# ═══════════════════════════════════════════════════════════════════════════════
#  COUCHE MAZE  (génération + recherche start/goal)
# ═══════════════════════════════════════════════════════════════════════════════

def generate_maze(rows: int, cols: int, fill_rate: float = 0.30, seed=None):
    """Appelle src/maze.py ou le générateur intégré."""
    if _HAS_MAZE:
        try:
            maze =  Maze(rows, cols, seed=seed, fill_rate=fill_rate) 
            maze.generate()
            return maze
        except Exception:
            pass
    return _builtin_generate(rows, cols, fill_rate, seed)


def _builtin_generate(rows, cols, fill_rate, seed):
    random.seed(seed)
    maze = [['#'] * cols for _ in range(rows)]
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            maze[r][c] = '.' if random.random() > fill_rate else '#'
    maze[1][1] = 'S'
    maze[rows - 2][cols - 2] = 'G'
    _carve(maze, (1, 1), (rows - 2, cols - 2), rows, cols)
    return maze


def _carve(maze, start, goal, rows, cols):
    visited = {start}; prev = {start: None}; q = deque([start])
    while q:
        r, c = q.popleft()
        if (r, c) == goal: break
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 < nr < rows-1 and 0 < nc < cols-1 and (nr,nc) not in visited:
                visited.add((nr,nc)); prev[(nr,nc)]=(r,c); q.append((nr,nc))
    node = goal
    while node and node != start:
        r, c = node
        if maze[r][c] not in ('S','G'): maze[r][c] = '.'
        node = prev.get(node)


def find_start_goal(maze):
    start = goal = None
    if _HAS_MAZE:
        try:
            start = maze.get_start()
            goal = maze.get_goal()
            return start, goal
        except Exception:
            pass

    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == 'S': start = (r, c)
            if cell == 'G': goal = (r, c)
    return start, goal


# ═══════════════════════════════════════════════════════════════════════════════
#  COUCHE ALGORITHMES  (avec fallback intégré si src/ absent)
# ═══════════════════════════════════════════════════════════════════════════════

def _steps_from_order(order):
    """Construit des snapshots progressifs pour l'animation."""
    steps, cur = [], set()
    for node in order:
        cur.add(node)
        steps.append(frozenset(cur))
    return steps


def _reconstruct(prev, goal):
    path = []; node = goal
    while node: path.append(node); node = prev.get(node)
    return list(reversed(path))


# ── BFS ───────────────────────────────────────────────────────────────────────

def run_bfs(maze, start, goal):
    """→ (steps, path, visited_set, time_ms)"""
    if _HAS_BFS:
        try:
            t0 = time.perf_counter()
            result = bfs_search(maze)
            ms = (time.perf_counter() - t0) * 1000
            # Adapte selon la signature de ton bfs.py :
            # supposé retourner (path, visited) ou (path, visited, time)
            path    = result[0] if isinstance(result[0], list) else list(result[0])
            visited = set(result[1])
            return _steps_from_order(list(visited)), path, visited, ms
        except Exception as e:
            print(f"[WARN] src/bfs.py échoué ({e}), fallback intégré.")
    return _builtin_bfs(maze, start, goal)


def _builtin_bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    visited = {start}; prev = {start: None}; q = deque([start]); order = []
    t0 = time.perf_counter()
    while q:
        curr = q.popleft(); order.append(curr)
        if curr == goal: break
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = curr[0]+dr, curr[1]+dc
            if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and maze[nr][nc]!='#':
                visited.add((nr,nc)); prev[(nr,nc)]=curr; q.append((nr,nc))
    ms = (time.perf_counter() - t0) * 1000
    return _steps_from_order(order), _reconstruct(prev, goal), visited, ms


# ── DFS ───────────────────────────────────────────────────────────────────────

def run_dfs(maze, start, goal):
    if _HAS_DFS:
        try:
            t0 = time.perf_counter()
            result = dfs_search(maze)
            ms = (time.perf_counter() - t0) * 1000
            path    = result[0] if isinstance(result[0], list) else list(result[0])
            visited = set(result[1])
            return _steps_from_order(list(visited)), path, visited, ms
        except Exception as e:
            print(f"[WARN] src/dfs.py échoué ({e}), fallback intégré.")
    return _builtin_dfs(maze, start, goal)


def _builtin_dfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    visited = set(); prev = {start: None}; stack = [start]; order = []
    t0 = time.perf_counter()
    while stack:
        curr = stack.pop()
        if curr in visited: continue
        visited.add(curr); order.append(curr)
        if curr == goal: break
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = curr[0]+dr, curr[1]+dc
            if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and maze[nr][nc]!='#':
                prev.setdefault((nr,nc), curr); stack.append((nr,nc))
    ms = (time.perf_counter() - t0) * 1000
    return _steps_from_order(order), _reconstruct(prev, goal), visited, ms


# ── A* ────────────────────────────────────────────────────────────────────────

def run_astar(maze, start, goal):
    if _HAS_ASTAR:
        try:
            t0 = time.perf_counter()
            result = astar_search(maze)
            ms = (time.perf_counter() - t0) * 1000
            path    = result[0] if isinstance(result[0], list) else list(result[0])
            visited = set(result[1])
            return _steps_from_order(list(visited)), path, visited, ms
        except Exception as e:
            print(f"[WARN] src/astar.py échoué ({e}), fallback intégré.")
    return _builtin_astar(maze, start, goal)


def _builtin_astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    def h(n): return abs(n[0]-goal[0]) + abs(n[1]-goal[1])
    open_set = [(h(start), 0, start)]
    g_score = {start: 0}; prev = {start: None}; visited = set(); order = []
    t0 = time.perf_counter()
    while open_set:
        _, g, curr = heapq.heappop(open_set)
        if curr in visited: continue
        visited.add(curr); order.append(curr)
        if curr == goal: break
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = curr[0]+dr, curr[1]+dc
            if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]!='#':
                ng = g + 1
                if ng < g_score.get((nr,nc), float('inf')):
                    g_score[(nr,nc)] = ng; prev[(nr,nc)] = curr
                    heapq.heappush(open_set, (ng + h((nr,nc)), ng, (nr,nc)))
    ms = (time.perf_counter() - t0) * 1000
    return _steps_from_order(order), _reconstruct(prev, goal), visited, ms


# ═══════════════════════════════════════════════════════════════════════════════
#  CONTROLLER
# ═══════════════════════════════════════════════════════════════════════════════

SPEED_MS = {'fast': 12, 'medium': 45, 'slow': 130}
ALGO_MAP  = {0: 'BFS', 1: 'DFS', 2: 'A*'}


class MazeController:
    """
    Relie :
      - self.ui         → Ui_MainWindow  (widgets PySide6)
      - self.grid       → GridWidget     (affichage labyrinthe)
      - algorithmes     → run_bfs / run_dfs / run_astar
    """

    def __init__(self, ui, grid_widget):
        self.ui   = ui
        self.grid = grid_widget

        # État interne
        self.maze:        list[list[str]] = []
        self.start                        = None
        self.goal                         = None
        self.steps:       list            = []
        self.path:        list            = []
        self.visited_all: set             = set()
        self.step_idx:    int             = 0
        self.compute_ms:  float           = 0.0
        self.anim_speed:  int             = SPEED_MS['medium']
        self._current_seed:int            = 42

        # Timer animation
        self._timer = QTimer()
        self._timer.timeout.connect(self._anim_step)

        # Connecter les signaux UI
        self._connect_signals()

        # Lancer avec un labyrinthe par défaut
        self._on_generate()

    # ── Connexions ────────────────────────────────────────────────────────────

    def _connect_signals(self):
        ui = self.ui
        ui.btnGenerate.clicked.connect(self._on_generate)
        ui.btnRun.clicked.connect(self._on_run)
        ui.checkBoxSeed.toggled.connect(self._on_seed_toggled)

        # Menu Fichier
        ui.actionNouveau.triggered.connect(self._on_generate)
        ui.actionSauvegarder.triggered.connect(self._on_save)

        # Menu Affichage
        ui.actionMode_sombre.triggered.connect(self._on_toggle_theme)

        # Menu Info
        ui.actionA_propos.triggered.connect(self._on_about)
        ui.actionRaccourcis.triggered.connect(self._on_shortcuts)

    # ── Génération ────────────────────────────────────────────────────────────

    def _on_generate(self):
        self._timer.stop()
        rows = cols = self.ui.spinBoxSize.value()
        fill = self.ui.spinBoxFillRate.value() / 100.0

        if self.ui.checkBoxSeed.isChecked():
            seed = self.ui.spinBoxSeed.value()
            self.ui.seedStatusLabel.setText(f"🔒 Seed fixe : {seed}")
        else:
            seed = random.randint(0, 999999)
            self.ui.seedStatusLabel.setText(f"🎲 Seed aléatoire : {seed}")

        self._current_seed = seed
        self.maze = generate_maze(rows, cols, fill_rate=fill, seed=seed)
        self.start, self.goal = find_start_goal(self.maze)

        self._reset_state()

        if _HAS_MAZE:
            self.grid.build(self.maze.grid)
        else:          # ← AFFICHE dans le scrollArea
            self.grid.build(self.maze)
        self._reset_stats()

        self._log(f"[GEN] Labyrinthe {rows}×{cols} — seed={seed} — murs={int(fill*100)}%")

    # ── Résolution ────────────────────────────────────────────────────────────

    def _on_run(self):
        if not self.maze:
            self._log("[WARN] Génère d'abord un labyrinthe (Ctrl+G).")
            return
        if self.start is None or self.goal is None:
            self._log("[ERR] Départ (S) ou arrivée (G) introuvable.")
            return

        self._timer.stop()
        self.grid.clear()           # remet les cellules à l'état initial
        self._reset_state()
        self._reset_stats()

        algo = ALGO_MAP.get(self.ui.comboAlgo.currentIndex(), 'A*')
        self._log(f"[RUN] {algo} en cours...")

        # Lancer l'algorithme
        if algo == 'BFS':
            self.steps, self.path, self.visited_all, self.compute_ms = \
                run_bfs(self.maze, self.start, self.goal)
        elif algo == 'DFS':
            self.steps, self.path, self.visited_all, self.compute_ms = \
                run_dfs(self.maze, self.start, self.goal)
        else:
            self.steps, self.path, self.visited_all, self.compute_ms = \
                run_astar(self.maze, self.start, self.goal)

        # Barre de progression
        self.ui.progressBar.setVisible(True)
        self.ui.progressBar.setMaximum(max(len(self.steps), 1))
        self.ui.progressBar.setValue(0)

        self.step_idx = 0
        self._timer.start(self.anim_speed)

    # ── Animation pas-à-pas ───────────────────────────────────────────────────

    def _anim_step(self):
        if self.step_idx < len(self.steps):
            snapshot = self.steps[self.step_idx]
            self.grid.mark_visited(snapshot)
            self.ui.progressBar.setValue(self.step_idx + 1)
            self.step_idx += 1
        else:
            self._timer.stop()
            self.grid.mark_path(self.path)          # ← chemin final en orange
            self._update_stats()
            self.ui.progressBar.setVisible(False)
            algo = ALGO_MAP.get(self.ui.comboAlgo.currentIndex(), '?')
            self._log(
                f"[OK] {algo} terminé — "
                f"explorés: {len(self.visited_all)} — "
                f"chemin: {len(self.path)} cellules — "
                f"temps: {self.compute_ms:.3f} ms"
            )

    # ── Seed toggle ───────────────────────────────────────────────────────────

    def _on_seed_toggled(self, checked: bool):
        self.ui.spinBoxSeed.setEnabled(checked)
        if checked:
            self.ui.seedStatusLabel.setText(
                f"🔒 Seed fixe : {self.ui.spinBoxSeed.value()}"
            )
        else:
            self.ui.seedStatusLabel.setText("🎲 Seed : aléatoire")

    # ── Stats ─────────────────────────────────────────────────────────────────

    def _update_stats(self):
        self.ui.valueCells.setText(str(len(self.visited_all)))
        self.ui.valuePath.setText(str(len(self.path)))
        self.ui.valueTime.setText(f"{self.compute_ms:.3f} ms")

    def _reset_stats(self):
        self.ui.valueCells.setText("—")
        self.ui.valuePath.setText("—")
        self.ui.valueTime.setText("—")
        self.ui.progressBar.setVisible(False)

    def _reset_state(self):
        self.steps       = []
        self.path        = []
        self.visited_all = set()
        self.step_idx    = 0
        self.compute_ms  = 0.0

    # ── Menu actions ──────────────────────────────────────────────────────────

    def _on_save(self):
        if not self.maze:
            self._log("[WARN] Aucun labyrinthe à sauvegarder.")
            return
        path, _ = QFileDialog.getSaveFileName(
            None, "Sauvegarder le labyrinthe", "", "Fichier texte (*.txt)"
        )
        if path:
            with open(path, 'w', encoding='utf-8') as f:
                for row in self.maze:
                    f.write(' '.join(row) + '\n')
            self._log(f"[SAVE] Sauvegardé → {path}")

    def _on_toggle_theme(self):
        self._log("[VIEW] Basculement de thème (à implémenter selon tes préférences)")

    def _on_about(self):
        QMessageBox.information(
            None, "À propos",
            "🔀  Maze Solver — INF-5183\n\n"
            "Auteur : Yao Henri Kouassi\n"
            "Université du Québec en Outaouais\n\n"
            "Algorithmes : BFS · DFS · A* (Manhattan)\n"
            "Interface : PySide6 (Qt 6)"
        )

    def _on_shortcuts(self):
        QMessageBox.information(
            None, "Raccourcis clavier",
            "Ctrl+G  →  Générer un labyrinthe\n"
            "Ctrl+R  →  Résoudre\n"
            "Ctrl+N  →  Nouveau labyrinthe\n"
            "Ctrl+S  →  Sauvegarder\n"
            "F1      →  Cette fenêtre"
        )

    # ── Journal ───────────────────────────────────────────────────────────────

    def _log(self, msg: str):
        palette = {
            '[GEN]':  '#2980b9',
            '[RUN]':  '#e67e22',
            '[OK]':   '#27ae60',
            '[ERR]':  '#e74c3c',
            '[WARN]': '#f39c12',
            '[SAVE]': '#8e44ad',
            '[VIEW]': '#7f8c8d',
            '[INFO]': '#16a085',
        }
        tag   = next((k for k in palette if msg.startswith(k)), None)
        color = palette.get(tag, '#aaaaaa')
        self.ui.textLog.append(f'<span style="color:{color};">{msg}</span>')