# AI MCTS Assignment

![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)  
![License](https://img.shields.io/github/license/paulCsGit/AI_MCTS_assign)

## GROUP MEMBERS
Pawlos Addisu     UGR/5732/15
Tariku Temesgen   UGR/7565/15
Simon beyene      UGR/6260/15
Ibrahim Ali       UGR/6991/15

## 📌 Overview

This repository contains an implementation of **Monte Carlo Tree Search (MCTS)** in Python — a powerful heuristic search algorithm commonly used in AI decision‑making tasks such as game playing and planning. :contentReference[oaicite:0]{index=0}

MCTS balances **exploration vs. exploitation** by building and sampling a search tree via random simulations, letting your AI make increasingly smarter decisions as it explores the decision space. :contentReference[oaicite:1]{index=1}

---

## 🧠 What is Monte Carlo Tree Search?

Monte Carlo Tree Search (MCTS) is an algorithm that works by iteratively building a search tree and selecting moves using statistical sampling with random simulations. It is widely used in game AI and other sequential decision problems. :contentReference[oaicite:2]{index=2}

Four main steps of the algorithm:

1. **Selection** — Traverse the tree and select the most promising node. :contentReference[oaicite:3]{index=3}  
2. **Expansion** — Expand one or more child nodes. :contentReference[oaicite:4]{index=4}  
3. **Simulation** — Perform random simulations from the node. :contentReference[oaicite:5]{index=5}  
4. **Backpropagation** — Propagate results back up the tree. :contentReference[oaicite:6]{index=6}

---

## 🚀 Features

- Clean MCTS implementation in Python
- Modular design (`mcts.py`, `node.py`, `game.py`)
- Easy to adapt to any game or decision problem
- Demonstrative entry point (`main.py`)

---

## 📁 Repository Structure

AI_MCTS_assign/
├── game.py # Game interface/logic handler
├── main.py # Example usage / entry point
├── mcts.py # MCTS implementation
├── node.py # MCTS tree node structure
├── README.md # This file

---

## 🛠️ Installation

1. **Clone the repo**

   ```sh
   git clone https://github.com/paulCsGit/AI_MCTS_assign.git
   cd AI_MCTS_assign
