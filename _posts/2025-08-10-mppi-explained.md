---
title: "Model Predictive Path Integral (MPPI)"
date: 2025-08-13
permalink: /posts/2025/08/mppi-explained/
categories: motion-planning
tags:
  - algorithms
  - trajectory-optimization
  - robotics
  - model-predictive-control
  - computer-science
---


## Article Goal
Explain MPPI (Model Predictive Path Integral) algorithm for stochastic optimal control

## What is MPPI?
**MPPI** is a sampling-based model predictive control algorithm that combines path integral formulations from statistical physics with model predictive control. MPPI performs stochastic optimization by sampling thousands of control trajectories, evaluating their costs using forward dynamics models, and then computing control inputs as importance-weighted averages of the samples.

Unlike traditional gradient-based MPC methods, MPPI is derivative-free and can handle non-convex cost functions, making it particularly suitable for complex robotic systems with constraints and obstacles. The algorithm leverages parallel computing (especially GPUs) to evaluate many rollouts simultaneously, enabling real-time performance.

**[MPPI: Written Walkthrough](/files/MPPI.pdf)**

## Core Concepts
1. **Sampling-Based Optimization** - Generates thousands of random control trajectories rather than using gradient-based optimization.
2. **Information-Theoretic Control** - Uses principles from statistical physics, specifically the relationship between free energy and relative entropy.
3. **Importance Sampling** - Weights trajectories based on their cost, giving higher importance to lower-cost rollouts.
4. **Parallel Computation** - Leverages GPU parallelization to evaluate many rollouts simultaneously for real-time performance.

## The Math

### System Dynamics
Consider a discrete-time stochastic system:
$$x_{t+1} = f(x_t, u_t) + w_t$$

Where $$w_t$$ represents system noise or disturbances.

### Cost Function
The total cost for a trajectory is:
$$S(\tau) = \phi(x_T) + \sum_{t=0}^{T-1} q(x_t, u_t)$$

Where:
- $$\phi(x_T)$$ is the terminal cost
- $$q(x_t, u_t)$$ is the running cost
- $$\tau$$ represents a complete trajectory

### Control Perturbations
MPPI generates control sequences by adding noise to a nominal control:
$$u_t^{(i)} = \bar{u}_t + \epsilon_t^{(i)}$$

Where:
- $$\bar{u}_t$$ is the nominal control at time $$t$$
- $$\epsilon_t^{(i)} \sim \mathcal{N}(0, \Sigma)$$ is sampled noise for rollout $$i$$

### Importance Weights
The weight for each trajectory is computed using:
$$w^{(i)} = \frac{\exp(-\frac{1}{\lambda} S(\tau^{(i)}))}{\sum_{j=1}^{K} \exp(-\frac{1}{\lambda} S(\tau^{(j)}))}$$

Where:
- $$\lambda$$ is the temperature parameter controlling exploration vs. exploitation
- $$K$$ is the total number of rollouts
- Lower costs result in higher weights

### Control Update
The optimal control is computed as the weighted average:
$$u_t^* = \bar{u}_t + \sum_{i=1}^{K} w^{(i)} \epsilon_t^{(i)}$$

### Path Integral Formulation
The theoretical foundation comes from the path integral:
$$u_t^* = \bar{u}_t + \frac{\int \epsilon_t \exp(-\frac{1}{\lambda} S(\tau)) d\tau}{\int \exp(-\frac{1}{\lambda} S(\tau)) d\tau}$$

Which MPPI approximates through Monte Carlo sampling.

## Algorithm Steps
1. **Initialize** - Set nominal control sequence $$\bar{u}_0, \bar{u}_1, ..., \bar{u}_{T-1}$$
2. **Sample Rollouts** - Generate $$K$$ control sequences by adding Gaussian noise: $$u_t^{(i)} = \bar{u}_t + \epsilon_t^{(i)}$$
3. **Forward Simulation** - For each rollout, simulate system dynamics to get trajectory $$\tau^{(i)}$$
4. **Cost Evaluation** - Compute cost $$S(\tau^{(i)})$$ for each trajectory
5. **Compute Weights** - Calculate importance weights $$w^{(i)}$$ based on trajectory costs
6. **Update Control** - Compute weighted average: $$u_0^* = \bar{u}_0 + \sum_{i=1}^{K} w^{(i)} \epsilon_0^{(i)}$$
7. **Apply Control** - Execute $$u_0^*$$ and shift time horizon forward
8. **Repeat** - Update nominal sequence and repeat for next time step



## Advantages of MPPI
1. **Derivative-Free** - No need for cost function gradients or dynamics linearization
2. **Handles Non-Convexity** - Can optimize non-convex and discontinuous cost functions
3. **Real-Time Capability** - GPU parallelization enables real-time performance
4. **Constraint Handling** - Easily incorporates hard constraints through cost penalties
5. **Robust to Model Uncertainty** - Stochastic sampling provides natural robustness
6. **Implementation Simplicity** - Straightforward to implement compared to gradient-based methods

## Limitations
1. **Sample Complexity** - Requires many rollouts for good performance, computationally expensive
2. **Hyperparameter Sensitivity** - Performance depends on proper tuning of λ, Σ, and K
3. **Short-Sighted** - Limited by prediction horizon length
4. **Noise Assumptions** - Assumes Gaussian noise, may not suit all applications
5. **Memory Requirements** - Storing thousands of rollouts can be memory-intensive
6. **Local Optima** - Can get stuck in local minima despite stochastic exploration
