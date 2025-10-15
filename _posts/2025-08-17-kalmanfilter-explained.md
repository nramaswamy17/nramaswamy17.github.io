---
title: "Kalman Filter"
date: 2025-08-17
permalink: /posts/2025/08/kalmanfilter-explained/
categories: motion-planning
tags:
  - state-estimation
  - kalman-filter
  - optimal-filtering
  - robotics
  - sensor-fusion
  - engineering
---


## Article Goal
Explain the Kalman Filter algorithm for optimal state estimation in "noisy" dynamic systems

## What is the Kalman Filter?
The **Kalman Filter** is an optimal recursive algorithm that estimates the true state of a dynamic system from a series of noisy measurements. It operates by continuously predicting the system state forward in time, then updating these predictions as new measurements become available.

The key insight is that optimal estimation requires balancing two sources of information: predictions based on system models and observations from sensors. The filter automatically weighs these sources based on their respective uncertainties, trusting more reliable information more heavily. This approach provides the mathematically optimal estimate under assumptions of linear dynamics and Gaussian noise.

**[Kalman Filter: Written Walkthrough](/files/Kalman_Filter.pdf)**

## Core Concepts
1. **State Vector (x)** - Contains all variables we want to estimate (position, velocity, etc.)
2. **Prediction Step** - Uses system model to forecast next state and its uncertainty
3. **Update Step** - Incorporates new measurements to refine state estimate
4. **Covariance Matrix (P)** - Quantifies uncertainty in state estimates
5. **Kalman Gain (K)** - Optimal weighting factor between prediction and measurement

## The Math

### State Space Model
The system dynamics and measurements are modeled as:

$$x_k = F_{k-1} x_{k-1} + w_{k-1}$$

$$z_k = H_k x_k + v_k$$

Where:
- $$x_k$$ is the state vector at time $$k$$
- $$F_{k-1}$$ is the state transition model
- $$w_{k-1}$$ is process noise $$\sim N(0, Q_{k-1})$$
- $$z_k$$ is the measurement vector
- $$H_k$$ is the observation model
- $$v_k$$ is measurement noise $$\sim N(0, R_k)$$

### Prediction Equations
The predict step forecasts the state and its uncertainty:

$$\hat{x}_{k|k-1} = F_{k-1} \hat{x}_{k-1|k-1}$$

$$P_{k|k-1} = F_{k-1} P_{k-1|k-1} F_{k-1}^T + Q_{k-1}$$

Where:
- $$\hat{x}_{k\\|k-1}$$ is the predicted state estimate
- $$P_{k\\|k-1}$$ is the predicted covariance matrix

### Update Equations
The update step incorporates new measurements:

$$y_k = z_k - H_k \hat{x}_{k|k-1}$$

$$S_k = H_k P_{k|k-1} H_k^T + R_k$$

$$K_k = P_{k|k-1} H_k^T S_k^{-1}$$

$$\hat{x}_{k|k} = \hat{x}_{k|k-1} + K_k y_k$$

$$P_{k|k} = (I - K_k H_k) P_{k|k-1}$$

Where:
- $$y_k$$ is the innovation (measurement residual)
- $$S_k$$ is the innovation covariance
- $$K_k$$ is the Kalman gain
- $$\hat{x}_{k\\|k}$$ is the updated state estimate
- $$P_{k\\|k}$$ is the updated covariance matrix

### Optimality
The Kalman filter minimizes the mean squared error between the true state and estimated state:

$$K_k = \arg\min_K E[||x_k - \hat{x}_{k|k}||^2]$$

#### Assumptions
1. System contains linear relationships
2. Noise follows a Gaussian Distribution

## Algorithm Steps
1. **Initialize State** - Set initial state estimate $$\hat{x}_{0\\|0}$$ and covariance $$P_{0\\|0}$$
2. **Predict State** - Compute predicted state: $$\hat{x}_{k\\|k-1} = F_{k-1} \hat{x}_{k-1\\|k-1}$$
3. **Predict Covariance** - Compute predicted uncertainty: $$P_{k\\|k-1} = F_{k-1} P_{k-1\\|k-1} F_{k-1}^T + Q_{k-1}$$
4. **Get Measurement** - Obtain new sensor measurement $$z_k$$
5. **Calculate Innovation** - Compute measurement residual: $$y_k = z_k - H_k \hat{x}_{k\\|k-1}$$
6. **Innovation Covariance** - Calculate: $$S_k = H_k P_{k\\|k-1} H_k^T + R_k$$
7. **Kalman Gain** - Compute optimal gain: $$K_k = P_{k\\|k-1} H_k^T S_k^{-1}$$
8. **Update State** - Refine estimate: $$\hat{x}_{k\\|k} = \hat{x}_{k\\|k-1} + K_k y_k$$
9. **Update Covariance** - Reduce uncertainty: $$P_{k\\|k} = (I - K_k H_k) P_{k\\|k-1}$$
10. **Increment Time** - Set $$k = k + 1$$ and return to step 2
