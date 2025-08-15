---
title: "Fast Marching Trees (FMT*)"
date: 2025-08-13
permalink: /posts/2025/08/fmt-star-explained/
categories: motion-planning
tags:
  - algorithms
  - path-planning
  - robotics
  - sampling-based
  - optimal
  - computer-science
---


## Article Goal
Explain FMT* (Fast Marching Tree) algorithm for optimal motion planning

## What is FMT*?
**FMT*** is an asymptotically optimal sampling-based motion planning algorithm that efficiently finds collision-free paths in high-dimensional configuration spaces. FMT* performs a "lazy" dynamic programming recursion on a predetermined set of probabilistically-drawn samples to grow a tree of paths that moves steadily outward in cost-to-arrive space.

Unlike RRT* which incrementally samples and builds the tree, FMT* pre-samples all points and then systematically connects them using a heap-based approach similar to Dijkstra's algorithm. This makes FMT* particularly efficient when collision checking is expensive, as it defers collision checks until absolutely necessary.

**[FMT*: Written Walkthrough](/files/FMT.pdf)**

## Core Concepts
1. **Batch Sampling** - FMT* pre-samples all points in the configuration space before starting the tree construction process.
2. **Lazy Dynamic Programming** - Uses a systematic approach to build the tree by expanding nodes in order of their cost-to-come, similar to Dijkstra's algorithm.
3. **Heap-Based Expansion** - Maintains a priority queue (heap) to always expand the lowest-cost node next, ensuring optimal substructure.
4. **Deferred Collision Checking** - Only performs collision checks when a connection is about to be added to the tree, reducing computational overhead.

## The Math

### Cost Function
$$c(x) = \text{cost-to-come from start to node } x$$

### Sample Sets
FMT* partitions samples into three sets:
- $$V_{\text{unvisited}}$$: nodes not yet considered
- $$V_{\text{open}}$$: nodes in the heap ready for expansion  
- $$V_{\text{closed}}$$: nodes already expanded

### Connection Radius
$$r_n = \gamma \left(\frac{\log n}{n}\right)^{1/d}$$

Where:
- $$\gamma$$ is a problem-dependent constant
- $$n$$ is the number of samples
- $$d$$ is the dimension of the configuration space

### Near Neighbor Set
$$N_r(x) = \{y \in V : \|x - y\| \leq r_n\}$$

### Tree Update Rule
For each node $$z$$ in the open set, FMT* finds the minimum cost connection:
$$\text{parent}(z) = \arg\min_{y \in V_{\text{open}} \cap N_r(z)} c(y) + \|y - z\|$$

### Convergence Rate
FMT* achieves a convergence rate of:
$$O(n^{-1/d+\rho})$$

Where $$\rho$$ is an arbitrarily small positive constant.

## Algorithm Steps
1. **Initialize** - Sample $$n$$ points uniformly in the free configuration space
2. **Setup Sets** - Place start in $$V_{\text{open}}$$, goal and others in $$V_{\text{unvisited}}$$ 
3. **Heap Expansion** - Extract minimum cost node $$z$$ from $$V_{\text{open}}$$
4. **Find Neighbors** - Identify all unvisited neighbors $$N_r(z) \cap V_{\text{unvisited}}$$
5. **Lazy Connection** - For each neighbor, check if connection improves cost-to-come
6. **Collision Check** - Only now perform collision checking for promising connections
7. **Update Tree** - Add collision-free connections to tree, move nodes to appropriate sets
8. **Repeat** - Continue until goal is reached or $$V_{\text{open}}$$ is empty



## Advantages of FMT*
1. **Asymptotic Optimality** - Guaranteed to converge to optimal solution
2. **Fast Initial Convergence** - Quickly finds good solutions, then slowly improves them
3. **Efficient for Expensive Collision Checking** - Lazy evaluation reduces unnecessary collision checks
4. **High-Dimensional Performance** - Particularly effective in high-dimensional spaces
5. **Deterministic Expansion** - Uses systematic heap-based expansion rather than random sampling

## Limitations
1. **Memory Requirements** - Must store all n samples in memory from the start
2. **Parameter Tuning** - Connection radius requires careful tuning for optimal performance
3. **Plateau Behavior** - May converge slowly to true optimum within a homotopy class
4. **Static Planning** - Not inherently designed for dynamic replanning scenarios
