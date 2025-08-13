---
title: 'D*: Explained (Unfinished)'
date: 2025-08-01
permalink: /posts/2025/08/d-star-explained/
tags:
  - algorithms
  - pathfinding
  - robotics
  - dynamic planning
  - computer science
---

## Article Goal
Explain in the most straightforward way how D*'s Algorithm works and why it's essential for dynamic pathfinding.

## What is D*?

D* (Dynamic A*) is a pathfinding algorithm optimized for dynamic environments where obstacles can appear, disappear, or move during navigation. Unlike A*, which assumes a static environment, D* can **efficiently** replan paths when the environment changes. This makes it particularly valuable in robotics and real-world navigation systems.

D* maintains a balance between:

1. Efficient initial path planning
2. Fast replanning when obstacles change
3. Reusing previous computational work

Contrasting from A*, the D* algorithm searches backwards from the goal to the start and maintains information about previous searches to enable efficient replanning when the environment changes.

### 1. State Categories

D* classifies each node into one of several states:

- **NEW**: Node has never been placed on the OPEN list
- **OPEN**: Node is currently on the OPEN list (pending processing)
- **CLOSED**: Node has been processed and removed from OPEN list
- **RAISE**: Node's cost has increased and needs propagation
- **LOWER**: Node's cost has decreased and needs propagation

### 2. Cost Functions

- **h(n)**: The estimated cost from node n to the goal
- **k(n)**: The key value used for prioritizing nodes in the OPEN list
- **c(n,m)**: The cost of moving from node n to node m
- **t(n)**: Tag indicating the state of node n

### 3. The OPEN List

Unlike A*'s priority queue, D* uses a priority queue where nodes can have different priority values (k-values) that may not always equal their h-values. This allows for efficient handling of cost changes.

## Simple Example

**[D*: Detailed Mathematical Analysis](/files/Dstar.pdf)**

# References

Stentz, A. (1994). Optimal and Efficient Path Planning for Partially-Known Environments. Proceedings of the IEEE International Conference on Robotics and Automation.