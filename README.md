# Motion Planning Algorithm Portfolio

A collection of motion planning algorithms spanning decades of research and development, from classical graph-based methods to cutting-edge learning-based approaches.

## Overview

This repository serves as a personal portfolio showcasing implementations and explorations of fundamental and state-of-the-art motion planning algorithms. The collection traces the evolution of the field from early deterministic graph search methods to modern hybrid approaches that combine optimization, machine learning, and safety guarantees.

## Algorithm Categories

### Classical Graph-Based Algorithms (1950-1989)
The foundational algorithms that established optimal pathfinding principles:
- **Dijkstra's Algorithm (1956)** - Optimal shortest path search
- **A* (1968)** - Heuristic-guided optimal search
- **D*** - Dynamic replanning for changing environments

### Sampling-Based Motion Planning (1990-2009)
Probabilistic approaches that revolutionized high-dimensional planning:
- **Probabilistic Roadmap (PRM)** - Multi-query roadmap construction
- **Rapidly-exploring Random Trees (RRT)** - Single-query tree expansion
- **RRT*** - Asymptotically optimal RRT variant
- **RRT-Connect** - Bidirectional tree growth
- **Informed RRT** - Sample space focusing for optimality

### Optimization-Based Approaches (2000-2019)
Trajectory optimization methods for smooth, dynamically feasible paths:
- **CHOMP** - Covariant Hamiltonian Optimization for Motion Planning
- **STOMP** - Stochastic Trajectory Optimization for Motion Planning
- **TrajOpt** - Sequential convex optimization for trajectory planning

### Modern Hybrid and Learning-Based Methods (2010s-Present)
Advanced techniques combining multiple paradigms:
- **FMT*** - Fast Marching Trees for asymptotic optimality
- **BIT*** - Batch Informed Trees with anytime properties
- **Neural RRT*** - Neural network enhanced tree planning
- **MPNet** - End-to-end neural motion planning networks
- **Lightning Framework** - Experience-based planning acceleration

### State-of-the-Art Methods (Current)
Cutting-edge approaches pushing the boundaries of the field:
- **MPPI** - Model Predictive Path Integral control
- **Diffusion Policy** - Generative models for trajectory synthesis
- **DDP / iLQG** - Differential Dynamic Programming for optimal control
- **CBF-QP** - Control Barrier Functions with Quadratic Programming for safety-critical systems


*Exploring the intersection of robotics, optimization, and machine learning through the lens of motion planning.*