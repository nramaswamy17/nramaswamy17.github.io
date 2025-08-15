---
title: "TrajOpt: Explained"
date: 2025-08-13
permalink: /posts/2025/08/trajopt-explained/
categories: motion-planning
tags:
  - algorithms
  - trajectory-optimization
  - robotics
  - optimization
  - computer-science
---

## Article Goal
Explain TrajOpt (Trajectory Optimization using Sequential Convex Programming)

## What is TrajOpt?
**TrajOpt** is a trajectory optimization algorithm that formulates motion planning as a sequence of convex optimization problems. TrajOpt converts the inherently non-convex trajectory optimization problem into a series of convex subproblems that can be solved efficiently using standard optimization solvers.

The key insight is to linearize non-convex constraints (like collision avoidance) around the current trajectory estimate, solve the resulting convex problem, then iterate. This approach combines the theoretical guarantees of convex optimization with practical handling of complex geometric constraints.

TrajOpt starts with an initial trajectory guess and iteratively refines it by solving convex approximations of the original problem, using trust regions to ensure convergence.

**[TrajOpt: Simple Example](/files/TrajOpt.pdf)**


## Core Concepts
1. **Sequential Convex Programming (SCP)** - Converting non-convex problems into a sequence of convex subproblems
2. **Signed Distance Functions** - Using distance fields to represent collision constraints in a differentiable way
3. **Trust Regions** - Limiting step sizes to ensure the linear approximations remain valid
4. **Penalty Methods** - Converting hard constraints into soft penalties in the objective function

## The Math

### Problem Formulation
The trajectory optimization problem is formulated as:

$$\min_{\mathbf{x}} f(\mathbf{x}) + \sum_{i} \lambda_i g_i(\mathbf{x})^2$$

Where:
- $\mathbf{x} = [x_0, x_1, ..., x_T]$ represents the trajectory (sequence of robot configurations)
- $f(\mathbf{x})$ is the primary objective (e.g., minimize path length, smoothness)
- $g_i(\mathbf{x})$ are constraint functions (collision avoidance, joint limits, etc.)
- $\lambda_i$ are penalty weights

### Linearization of Constraints
For each constraint $g_i(\mathbf{x})$, TrajOpt computes the linear approximation around current estimate $\mathbf{x}^{(k)}$:

$$g_i(\mathbf{x}) \approx g_i(\mathbf{x}^{(k)}) + \nabla g_i(\mathbf{x}^{(k)})^T (\mathbf{x} - \mathbf{x}^{(k)})$$

### Trust Region Constraint
To ensure the linearization remains valid:

$$||\mathbf{x} - \mathbf{x}^{(k)}||_{\infty} \leq \Delta^{(k)}$$

Where $\Delta^{(k)}$ is the trust region radius at iteration $k$.

### Signed Distance Functions
For collision avoidance, TrajOpt uses signed distance functions:

$$d(\mathbf{x}_t) = \min_{p \in \text{obstacles}} ||\text{robot}(\mathbf{x}_t) - p||$$

The collision constraint becomes:
$$g_{\text{collision}}(\mathbf{x}_t) = \max(0, \epsilon - d(\mathbf{x}_t))$$

Where $\epsilon$ is the minimum safe distance.

### Sequential Updates
At each iteration $k$:
$$\mathbf{x}^{(k+1)} = \arg\min_{\mathbf{x}} f(\mathbf{x}) + \sum_i \lambda_i [g_i(\mathbf{x}^{(k)}) + \nabla g_i(\mathbf{x}^{(k)})^T (\mathbf{x} - \mathbf{x}^{(k)})]^2$$

Subject to: $||\mathbf{x} - \mathbf{x}^{(k)}||_{\infty} \leq \Delta^{(k)}$

## Algorithm Steps
1. **Initialize** - Start with initial trajectory guess (e.g., straight line interpolation)
2. **Linearize Constraints** - Compute linear approximations of all non-convex constraints around current trajectory
3. **Formulate Convex Subproblem** - Create convex optimization problem with linearized constraints and trust region
4. **Solve Subproblem** - Use convex optimization solver (e.g., OSQP, Gurobi) to find optimal step
5. **Update Trust Region** - Adjust trust region radius based on solution quality
6. **Check Convergence** - Test for convergence criteria or maximum iterations
7. **Repeat** - Continue until convergence achieved

## Performance Analysis

### Time Complexity
- **Per iteration**: O(n³) where n is the number of trajectory variables (dominated by convex solver)
- **Total**: O(I * n³) where I is number of iterations
- **Practical**: Often converges in 10-50 iterations

### Space Complexity
- **Trajectory storage**: O(T * d) where T is time steps, d is robot DOF
- **Jacobian matrices**: O(C * T * d) where C is number of constraints
- **Solver workspace**: O(n²) for interior point methods

## Advantages of TrajOpt
1. **Fast convergence** due to second-order optimization methods
2. **Handles complex constraints** through differentiable approximations  
3. **Deterministic behavior** unlike sampling-based methods
4. **Leverages mature convex solvers** with strong theoretical guarantees
5. **Scales well** to high-dimensional robot systems

## Limitations
1. **Requires good initialization** - poor initial guess can lead to local minima
2. **Constraint linearization accuracy** - approximations may not capture true constraint geometry
3. **Trust region tuning** - requires careful parameter selection for reliable convergence
4. **Memory intensive** for long horizons due to dense constraint matrices
5. **Sensitive to penalty weights** - requires balancing constraint satisfaction vs objective optimization