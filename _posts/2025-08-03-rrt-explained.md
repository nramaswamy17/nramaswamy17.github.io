---
title: "RRT: Explained (Unfinished)"
date: 2025-08-03
permalink: /posts/2025/08/rrt-explained/
categories: motion-planning
tags:
  - algorithms
  - path-planning
  - robotics
  - sampling-based
  - computer-science
---

## Article Goal
Explain in the most straightforward way how RRT (Rapidly-exploring Random Tree) works. This sampling-based algorithm is widely used in robotics and autonomous systems for path planning in complex environments.

## What is RRT?

RRT (Rapidly-exploring Random Tree) is a sampling-based path planning algorithm that efficiently explores high-dimensional spaces. Unlike grid-based algorithms like A* or Dijkstra's, RRT doesn't require discretizing the space into a grid. Instead, it builds a tree structure by randomly sampling points in the configuration space and connecting them to the nearest existing tree node.

RRT is particularly effective for:
- High-dimensional spaces (robotic arms with many joints)
- Dynamic environments
- Real-time path planning
- Non-holonomic constraints

## Core Components

### 1. Tree Structure
- **Nodes**: Represent configurations (positions, orientations)
- **Edges**: Represent feasible paths between configurations
- **Root**: Starting configuration

### 2. Sampling Strategy
- Random sampling in the configuration space
- Goal-biased sampling (occasionally sample the goal)
- Obstacle-aware sampling

### 3. Nearest Neighbor Search
- Find the closest existing tree node to a sampled point
- Critical for efficient tree expansion

## Algorithm

1. **Initialization**
   - Initialize tree with start configuration as root
   - Set maximum iterations or time limit

2. **Random Sampling**
   - Sample a random configuration $q_{\text{rand}}$ in the configuration space
   - With probability $p_{\text{goal}}$, set $q_{\text{rand}} = q_{\text{goal}}$ (goal bias)

3. **Nearest Neighbor**
   - Find the nearest node $q_{\text{near}}$ in the tree to $q_{\text{rand}}$

4. **Extend Towards Sample**
   - Calculate $q_{\text{new}}$ by extending from $q_{\text{near}}$ towards $q_{\text{rand}}$
   - If the path from $q_{\text{near}}$ to $q_{\text{new}}$ is collision-free:
       - Add $q_{\text{new}}$ to the tree
       - Set $q_{\text{near}}$ as parent of $q_{\text{new}}$

5. **Goal Check**
   - If $q_{\text{new}}$ is close enough to the goal:
       - Reconstruct path from goal to start
       - Return the path

6. **Repeat**
   - Repeat steps 2-5 until goal is reached or maximum iterations exceeded

## Cool Features

### Probabilistic Completeness
RRT is probabilistically complete, meaning it will find a path if one exists, given enough time.

### Rapid Exploration
The algorithm efficiently explores the configuration space by:
- Random sampling prevents getting stuck in local minima
- Goal bias ensures progress toward the goal
- Tree structure allows efficient nearest neighbor searches

### Adaptability
- Works in continuous spaces
- Handles complex constraints
- Suitable for real-time applications

## Performance

**Complexity**
- **Time:** $O(n \log n)$ where $n$ is the number of nodes (with efficient nearest neighbor search)
- **Space:** $O(n)$ for storing the tree

**Advantages**
- No need for grid discretization
- Works in high-dimensional spaces
- Probabilistically complete
- Fast exploration of large spaces

**Limitations**
- Paths may not be optimal
- Can be inefficient in narrow passages
- Random nature means performance varies

## Simple Example

Let's walk through a 2D example where we want to navigate from start to goal while avoiding obstacles.

### Step 1: Initialization
```
Start: (0, 0)
Goal: (8, 8)
Obstacles: Various rectangles
```

### Step 2: First Few Iterations
1. Sample random point (7.2, 3.1)
2. Find nearest tree node (start at (0,0))
3. Extend towards sample with step size 1.0
4. Add new node at (0.7, 0.3) if collision-free

### Step 3: Tree Growth
The tree grows by:
- Randomly sampling points
- Finding nearest existing node
- Extending towards sample
- Adding collision-free paths

### Step 4: Goal Reached
Eventually, a node gets close enough to the goal, and we trace back the path.

## Python Implementation

A full Python implementation of RRT is available in my repository:  
[algorithms/sampling/rrt.py](https://github.com/nramaswamy17/PlannerComparisons/blob/main/algorithms/sampling/rrt.py)


## Simple Example

**[RRT: Detailed Mathematical Analysis](/files/RRT.pdf)**

## References

LaValle, S. M. (1998). Rapidly-exploring random trees: A new tool for path planning. Technical Report 98-11, Computer Science Department, Iowa State University.
