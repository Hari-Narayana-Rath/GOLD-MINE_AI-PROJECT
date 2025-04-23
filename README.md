# 🏆 Gold Mine Game AI with Optimal Path Visualization

[Live Demo on Streamlit Cloud](https://gold-mine-ai-project.streamlit.app)

An interactive web application that simulates a miner traversing an \(n \times m\) gold-mine grid to collect the maximum possible gold. Built with Python, Streamlit for the front-end, and a combination of propositional logic and dynamic programming under the hood.

---

## 📋 Table of Contents

- [Features](#features)  
- [Algorithms & Methodology](#algorithms--methodology)  
  - [1. Propositional Logic Mapping](#1-propositional-logic-mapping)  
  - [2. Dynamic Programming Solver](#2-dynamic-programming-solver)  
  - [3. Path Reconstruction & Visualization](#3-path-reconstruction--visualization)  
- [Tech Stack](#tech-stack)  
- [Repository Structure](#repository-structure)  
- [Getting Started](#getting-started)  
  - [Clone the Repo](#clone-the-repo)  
  - [Install Dependencies](#install-dependencies)  
  - [Run Locally](#run-locally)  
- [Deploying Your Own Instance](#deploying-your-own-instance)  
- [Contributing](#contributing)  
- [Authors & Acknowledgments](#authors--acknowledgments)  
- [License](#license)  

---

## 🚀 Features

- **Interactive Grid Input**: Enter your gold-mine matrix manually or upload a JSON file.  
- **Dynamic Programming Table**: View the DP matrix showing the maximum gold collectible from each cell.  
- **Optimal Path Highlighting**: The chosen path is overlaid on the grid with step numbers and gold values.  
- **Step-by-Step Move List**: See exactly which moves the miner takes and how much gold is picked up at each step.  
- **One-Click Deployment**: Easily clone and deploy on Streamlit Cloud or any standard Python environment.

---

## 🧠 Algorithms & Methodology

### 1. Propositional Logic Mapping

We treat each grid position \((i,j)\) as a logical proposition \(P_{i,j}\). From any position, the miner may move to one of three positions in the next column:

\[
P_{i,j} \;\longrightarrow\; 
\bigl\{P_{i,j+1},\; P_{i-1,j+1},\; P_{i+1,j+1}\bigr\}
\]

This mapping enforces the movement constraints (right, diagonally up/right, diagonally down/right) in a clear, rule-based form.

### 2. Dynamic Programming Solver

We construct a 2D table `dp` of the same dimensions as the grid. The recurrence is:

\[
dp[i][j] = \;gold[i][j]\;+\;\max
\begin{cases}
dp[i][j+1],\\
dp[i-1][j+1]\quad(\text{if }i>0),\\
dp[i+1][j+1]\quad(\text{if }i<n-1)
\end{cases}
\]

- **Initialization**: In the last column `j = m-1`, set `dp[i][m-1] = gold[i][m-1]` for each row \(i\).  
- **Backward Fill**: Iterate columns from right to left, computing `dp[i][j]` via the above recurrence.  
- **Result**: The maximum gold collectible is \(\max_i \, dp[i][0]\).

This guarantees \(O(n \times m)\) time complexity and \(O(n \times m)\) space.

### 3. Path Reconstruction & Visualization

- While filling `dp`, we also track a `path` array storing, for each \((i,j)\), the next cell that leads to that maximum.  
- After filling, we start from the row \(r\) with the largest `dp[r][0]` and follow the stored pointers to reconstruct the sequence of moves.  
- The Streamlit UI overlays this path on the grid, highlights each visited cell, and prints a step-by-step list with the gold collected at each move.

---

## 🛠 Tech Stack

- **Python 3.x**  
- **Streamlit** – for the web interface  
- **NumPy** – efficient numeric operations  
- **Pandas** – DataFrame displays of the grid and DP table  
- **LaTeX** – documentation (in `report/`)  

---

### Clone the Repo

```bash
git clone https://github.com/your-username/gold-mine-game.git
cd gold-mine-game
```

### Install the Requirements 
```
pip install -r requirements.txt
```

### Run locally
```
streamlit run app.py
```

### 👥 Authors & Acknowledgments
HARI NARAYANA RATH – AP22110010601

Pranav S Krishnan – AP22110010653

Christo – AP22110010399

Sri Ram – AP22110010509

Y J Linus – AP22110010619

### Mentor: Dr. Susmi Jacob
