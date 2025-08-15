---
title: "Stochastic Trajectory Optimization for Motion Planning (STOMP)"
date: 2025-08-13
permalink: /posts/2025/08/stomp-explained/
categories: motion-planning
tags:
  - algorithms
  - trajectory-optimization
  - robotics
  - optimization
  - computer-science
---

## Article Goal
Explain STOMP (Stochastic Trajectory Optimization for Motion Planning)

## What is STOMP?
**STOMP** is a trajectory optimization algorithm that uses stochastic optimization to find smooth, collision-free paths for robotic systems. STOMP generates multiple noisy trajectory candidates and combines them using weighted averaging.

STOMP starts with an initial trajectory (usually straight line) and generates several noisy variations of the initial trajectory. It evaluates the cost of each rollout, and then combines all the variations, giving higher weight to lower cost options. It then iteratively repeats this process to converge to a smooth and short path. 

**[STOMP: Written Walkthrough](/files/STOMP.pdf)**

## Core Concepts
1. **Trajectory Representation** - STOMP represents trajectories as a sequence of waypoints, using stochastic exploration of the trajectory to find a path.
2. **Trajectory Generation** - The central, key idea is generating multiple noisy trajectory candidates by adding controlled noise to the current trajectory estimate.
3. **Probability-Weighted Updates** - STOMP uses the relative costs of generated trajectories to compute the probability weights, which are then used to generate the next path. 
4. **Policy Improvement** - The algorithm strategy improves the trajectory policy from the cost distribution of sampled rollouts. 

## The Math

### Cost Function
$$S(τ_i) = S_{obs}(τ_i) + S_{smooth}(τ_i) + S_{goal}(τ_i)$$

Where:
- $$S_{obs}(τ_i)$$ is the obstacle/collision cost
- $$S_{smooth}(τ_i)$$ is the smoothness cost (penalizes jerky motion)
- $$S_{goal}(τ_i)$$ is the goal reaching cost

### Noisy Trajectory Generation
$$τ_i = \theta_k + \epsilon_i$$

Where $$\epsilon_i$$ is typically sampled from a multivariate Gaussian distribution:

$$\epsilon_i \sim \mathcal{N}(0, \Sigma)$$

With $$\Sigma$$ being the covariance matrix that controls the noise characteristics.

### Core Update Equation
$$\theta_{k+1} = \theta_k + \sum_{i=1}^{K} P(τ_i) \epsilon_i$$

Where:
- $$\theta_k$$ is the current trajectory parameters at iteration $$k$$
- $$\theta_{k+1}$$ is the updated trajectory parameters
- $$K$$ is the number of rollouts
- $$τ_i$$ are the rollout trajectories
- $$\epsilon_i$$ are the noise perturbations added to generate rollout $$i$$
- $$P(τ_i)$$ are probability weights based on trajectory costs

### Probability Weight Computation
$$P(τ_i) = \frac{\exp(-h \cdot S(τ_i))}{\sum_{j=1}^{K} \exp(-h \cdot S(τ_j))}$$

Where:
- $$S(τ_i)$$ is the total cost of rollout trajectory $$i$$
- $$h$$ is a temperature parameter controlling exploration vs exploitation
- Higher $$h$$ values lead to more exploitation (focus on low-cost rollouts)
- Lower $$h$$ values lead to more exploration (more uniform weighting)

## Algorithm Steps
1. **Initialize** - Start with initial trajectory
2. **Generate Noisy Trajectories** - Create noisy variations of initial trajectory
3. **Evaluate Costs** - Compute the cost for each rollout 
4. **Compute Weights** Calculate the probability weights based on the relative cost
5. **Update Trajectory** - Combine noisy trajectories using probability-weighted averaging
6. **Repeat** - Repeat until convergence / max iterations reached



## Advantages of STOMP
1. More resilient to local minima through random noisy injections
2. Can parallelize the trajectory generation for faster computation time

## Limitations
1. Requires evaluating k noisy trajectories for each iteration
2. Storing k noisy trajectories takes up memory
3. Random noisy trajectories may take a while to result in good path