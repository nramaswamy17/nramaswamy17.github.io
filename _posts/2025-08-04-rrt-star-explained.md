---
title: "RRT*: Explained (Unfinished)"
date: 2025-08-04
permalink: /posts/2025/08/rrt-star-explained/
categories: motion-planning
tags:
  - algorithms
  - path-planning
  - robotics
  - sampling-based
  - optimization
  - computer-science
---

## Article Goal
Explain in the most straightforward way how RRT* (Rapidly-exploring Random Tree Star) works. This is an asymptotically optimal variant of RRT that continuously improves path quality through rewiring.

## What is RRT*?

RRT* is an asymptotically optimal variant of the RRT algorithm. While basic RRT finds feasible paths quickly, RRT* goes further by continuously optimizing the path quality as the tree grows. It achieves this through a clever rewiring strategy that maintains the tree structure while improving path costs.

The key insight of RRT* is that as the tree grows, better paths to existing nodes may be discovered. The algorithm continuously updates these paths, ensuring that the solution converges to the optimal path given enough time.

**[RRT*: Written Walkthrough](/files/RRTstar.pdf)**

## Core Components

### 1. Tree Structure (Same as RRT)
- **Nodes**: Represent configurations (positions, orientations)
- **Edges**: Represent feasible paths between configurations
- **Root**: Starting configuration

### 2. Cost Function
- Each node stores the cost from start to that node
- Used for path optimization decisions

### 3. Rewiring Strategy
- **Choose Parent**: Find the best parent for new nodes
- **Rewire Neighbors**: Update existing nodes if better paths are found

## Algorithm

1. **Initialization**
   - Initialize tree with start configuration as root
   - Set cost of start node to 0
   - Set maximum iterations or time limit

2. **Random Sampling**
   - Sample a random configuration $$q_{\text{rand}}$$ in the configuration space
   - With probability $$p_{\text{goal}}$$, set $$q_{\text{rand}} = q_{\text{goal}}$$ (goal bias)

3. **Nearest Neighbor**
   - Find the nearest node $$q_{\text{near}}$$ in the tree to $$q_{\text{rand}}$$

4. **Extend Towards Sample**
   - Calculate $$q_{\text{new}}$$ by extending from $$q_{\text{near}}$$ towards $$q_{\text{rand}}$$
   - If the path from $$q_{\text{near}}$$ to $$q_{\text{new}}$$ is collision-free:
       - Add $$q_{\text{new}}$$ to the tree

5. **Choose Parent**
   - Find all nodes within radius $$r$$ of $$q_{\text{new}}$$
   - Calculate cost to $$q_{\text{new}}$$ through each potential parent
   - Choose the parent that minimizes the cost to $$q_{\text{new}}$$

6. **Rewire Neighbors**
   - For each neighbor $$q_{\text{neighbor}}$$ within radius $$r$$ of $$q_{\text{new}}$$:
       - Calculate cost to $$q_{\text{neighbor}}$$ through $$q_{\text{new}}$$
       - If this cost is less than current cost to $$q_{\text{neighbor}}$$:
           - Update parent of $$q_{\text{neighbor}}$$ to $$q_{\text{new}}$$
           - Update cost of $$q_{\text{neighbor}}$$

7. **Goal Check**
   - If $$q_{\text{new}}$$ is close enough to the goal:
       - Reconstruct path from goal to start
       - Return the path

8. **Repeat**
   - Repeat steps 2-7 until goal is reached or maximum iterations exceeded

## Key Features

### Asymptotic Optimality
RRT* is asymptotically optimal, meaning that as the number of samples approaches infinity, the solution converges to the optimal path.

### Continuous Optimization
Unlike basic RRT, RRT* continuously improves path quality through:
- **Choose Parent**: Always selecting the best parent for new nodes
- **Rewire Neighbors**: Updating existing paths when better options are found

### Radius Function
The rewiring radius $$r$$ is crucial for performance:
- Too small: Limited optimization
- Too large: High computational cost
- Typically decreases with tree size: $$r = \gamma \left(\frac{\log n}{n}\right)^{1/d}$$

## Performance

**Complexity**
- **Time:** $$O(n \log n)$$ where $$n$$ is the number of nodes
- **Space:** $$O(n)$$ for storing the tree

**Advantages**
- Asymptotically optimal
- Continuous path improvement
- No need for grid discretization
- Works in high-dimensional spaces

**Limitations**
- Higher computational cost than basic RRT
- Requires careful tuning of radius function
- May be slower for simple environments

## Simple Example

Let's walk through a 2D example showing how RRT* improves paths over time.

### Step 1: Initial Tree Growth
```
Start: (0, 0)
Goal: (8, 8)
Initial nodes: A(0,0), B(1,1), C(2,0)
```

### Step 2: Adding New Node
1. Sample point near (3, 2)
2. Find nearest neighbor (node C)
3. Extend to create new node D(2.8, 1.6)

### Step 3: Choose Parent
- Check all nodes within radius r of D
- Calculate costs: cost(A→D) = 3.2, cost(C→D) = 1.8
- Choose C as parent (lower cost)

### Step 4: Rewire Neighbors
- Check if any existing nodes can reach their goal cheaper through D
- If cost(D→B) < cost(A→B), update B's parent to D

### Step 5: Continuous Improvement
As more nodes are added, the algorithm continuously finds better paths through the rewiring process.

## Comparison with RRT

| Feature | RRT | RRT* |
|---------|-----|------|
| Optimality | No | Asymptotically optimal |
| Path Quality | Variable | Continuously improving |
| Computation | Faster | Slower |
| Memory | Lower demand | Higher demand |

## Python Implementation

A full Python implementation of RRT* is available in my repository:  
[algorithms/sampling/rrt_star.py](https://github.com/nramaswamy17/PlannerComparisons/blob/main/algorithms/sampling/rrt_star.py)

## References

Karaman, S., & Frazzoli, E. (2011). Sampling-based algorithms for optimal motion planning. The International Journal of Robotics Research, 30(7), 846-894.
