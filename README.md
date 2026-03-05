# Maze Search Algorithms – INF-5183

## Overview

This project implements fundamental **Artificial Intelligence search algorithms** to solve a classical path-finding problem in a maze.

The goal is to automatically find a path from a **start position (S)** to a **goal position (G)** inside a maze while avoiding obstacles.

Three algorithms are implemented and compared:

* **Depth-First Search (DFS)**
* **Breadth-First Search (BFS)**
* **A* Search (A-Star)** using the **Manhattan heuristic**

The project also includes a **random maze generator** that guarantees the existence of a valid path between the start and the goal.

This work was developed as part of the course:

**INF-5183 – Foundations of Artificial Intelligence**

---

# Problem Description

The maze is represented as a **2D grid** where:

| Symbol | Meaning         |
| ------ | --------------- |
| `#`    | Wall (obstacle) |
| `.`    | Free cell       |
| `S`    | Start position  |
| `G`    | Goal position   |

Example of maze representation:

```
# # # # # # # #
# S . . # . . #
# . # . . . . #
# . # # # . # #
# . . . . . . #
# # # . # # . #
# . . . . . G #
# # # # # # # #
```

Allowed movements:

* Up
* Down
* Left
* Right

Diagonal moves are **not allowed**.

---

# Project Structure

```
Devoir_I/

maze.py          # Maze generation and grid utilities
dfs.py           # Depth First Search implementation
bfs.py           # Breadth First Search implementation
astar.py         # A* algorithm implementation
main.py          # Main program entry point

requirements.txt # Project dependencies
README.md        # Project documentation
```

---

# Algorithms Implemented

## Depth-First Search (DFS)

DFS explores the maze **as deep as possible** before backtracking.

Characteristics:

* Uses a **stack (LIFO)**
* Does **not guarantee the shortest path**
* Often explores fewer nodes but may produce longer paths

Exploration order:

```
Right → Down → Left → Up
```

---

## Breadth-First Search (BFS)

BFS explores the maze **level by level**.

Characteristics:

* Uses a **queue (FIFO)**
* Guarantees the **shortest path**
* Usually explores more nodes than DFS

---

## A* Search Algorithm

A* is an **informed search algorithm** that combines:

* the cost from the start `g(n)`
* an estimate to the goal `h(n)`

Evaluation function:

```
f(n) = g(n) + h(n)
```

Heuristic used:

**Manhattan Distance**

```
h(n) = |x_n - x_goal| + |y_n - y_goal|
```

A* typically finds the **optimal path faster** than BFS by guiding the search toward the goal.

---

# Maze Generation

The maze generator creates a **16 × 16 grid** with the following properties:

* Outer borders are always **walls**
* Internal walls are placed **randomly**
* Start position `S` is located at **(1,1)**
* Goal position `G` is located near the **bottom-right corner**
* A **valid path between S and G is guaranteed**
* A **random seed** can be used for reproducibility

---

# Program Output

For each algorithm the program displays:

### Maze Exploration

Visited cells are marked with:

```
p
```

### Final Path

The solution path is marked with:

```
*
```

Example output:

```
Chemin : S(1,1) → (2,1) → (3,1) → ... → G(14,14)
```

### Statistics

The program also reports:

* Number of explored nodes
* Length of the path
* Execution time (milliseconds)

---

# Performance Comparison

Example comparison table:

| Algorithm      | Explored Nodes | Path Length | Time (ms) |
| -------------- | -------------- | ----------- | --------- |
| DFS            | 78             | 45          | 0.521     |
| BFS            | 112            | 27          | 0.634     |
| A* (Manhattan) | 45             | 27          | 0.312     |

---

# Installation

Clone the repository:

```
git clone https://github.com/TecHenri/INF-5183.git
```

Move into the project directory:

```
cd maze-search-ai
```

Install dependencies (if needed):

```
pip install -r requirements.txt
```

---

# Usage

Run the program with:

```
python main.py
```

The program will:

1. Generate a random maze
2. Run DFS
3. Run BFS
4. Run A*
5. Display the results and statistics

---

# Requirements

* Python **3.11**
* Standard Python libraries

No external libraries are required.

---

# Educational Purpose

This project aims to:

* Understand **uninformed search algorithms**
* Understand **heuristic search**
* Compare algorithm **efficiency and optimality**
* Practice **algorithm implementation in Python**

---

# Author

**Yao Henri Kouassi**

Master's Student
Université du Québec en Outaouais

Course:

**INF-5183 – Foundations of Artificial Intelligence**

Instructor:

**Mohamed Lamine ALLAOUI**
