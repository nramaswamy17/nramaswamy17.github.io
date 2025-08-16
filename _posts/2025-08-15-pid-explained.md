---
title: "Proportional-Integral-Derivative (PID) Control"
date: 2025-08-15
permalink: /posts/2025/08/pid-explained/
categories: controls
tags:
  - control-theory
  - feedback-control
  - pid-controller
  - robotics
  - automation
  - engineering
---

## Article Goal
Explain PID Control algorithm for feedback control systems in robotics and automation

## What is PID Control?
**PID Control** (Proportional-Integral-Derivative) is a feedback control algorithm that continuously calculates an error value as the difference between a desired setpoint and a measured process variable. The controller attempts to minimize this error by adjusting a control input based on proportional, integral, and derivative terms.

The key insight is that effective control requires responding to current error (proportional), accumulated past error (integral), and predicted future error (derivative). This three-term combination provides robust control for a wide variety of systems while remaining computationally simple and intuitive to tune.

## Core Concepts
1. **Proportional Control (P)** - Responds proportionally to the current error magnitude
2. **Integral Control (I)** - Eliminates steady-state error by accumulating past errors
3. **Derivative Control (D)** - Provides predictive control by responding to error rate of change
4. **Feedback Loop** - Continuously measures output and adjusts input to minimize error

## The Math

### Error Calculation
The error signal is the difference between setpoint and process variable:
$$e(t) = SP(t) - PV(t)$$

Where:
- $e(t)$ is the error at time $$t$$
- $SP(t)$ is the setpoint (desired value)
- $PV(t)$ is the process variable (measured value)

### PID Control Equation
The control output combines three terms:
$$u(t) = K_p e(t) + K_i \int_0^t e(\tau) d\tau + K_d \frac{de(t)}{dt}$$

Where:
- $u(t)$ is the control output
- $K_p$ is the proportional gain
- $K_i$ is the integral gain  
- $K_d$ is the derivative gain

### Discrete-Time Implementation
For digital systems, the continuous equation becomes:
$$u[n] = K_p e[n] + K_i \sum_{k=0}^{n} e[k] \Delta t + K_d \frac{e[n] - e[n-1]}{\Delta t}$$

Where:
- $n$ is the current sample
- $\Delta t$ is the sampling period

### Transfer Function
In the Laplace domain, the PID controller has the transfer function:
$$C(s) = K_p + \frac{K_i}{s} + K_d s$$

### Tuning Parameters
Each gain affects system behavior:
- **$$K_p$$**: Higher values increase responsiveness but may cause overshoot
- **$$K_i$$**: Higher values eliminate steady-state error faster but may cause oscillation
- **$$K_d$$**: Higher values improve stability but amplify noise

## Algorithm Steps
1. **Initialize Parameters** - Set initial values for $$K_p$$, $$K_i$$, $$K_d$$ and reset integral sum
2. **Measure Process Variable** - Read current system output $$PV(t)$$
3. **Calculate Error** - Compute $$e(t) = SP(t) - PV(t)$$
4. **Proportional Term** - Calculate $$P = K_p \cdot e(t)$$
5. **Integral Term** - Update integral sum and calculate $$I = K_i \cdot \sum e(t) \Delta t$$
6. **Derivative Term** - Calculate $$D = K_d \cdot \frac{de(t)}{dt}$$
7. **Control Output** - Combine terms: $$u(t) = P + I + D$$
8. **Apply Control** - Send control signal $$u(t)$$ to actuators
9. **Wait** - Wait for next sampling period $$\Delta t$$
10. **Repeat** - Return to step 2 until setpoint achieved or system stopped

## Advantages of PID Control
1. **Simplicity** - Easy to understand and implement with minimal computational requirements
2. **Versatility** - Works well for many types of systems and processes
3. **No Model Required** - Doesn't need detailed mathematical model of the system
4. **Real-Time Performance** - Fast computation suitable for real-time control applications
5. **Proven Robustness** - Decades of successful industrial applications
6. **Intuitive Tuning** - Each parameter has clear physical meaning and effect
7. **Hardware Efficiency** - Can be implemented on simple microcontrollers

## Limitations
1. **Linear Assumption** - Assumes linear system behavior, struggles with highly nonlinear systems
2. **Single Input/Output** - Designed for SISO systems, requires extensions for MIMO control
3. **Tuning Challenges** - Optimal parameter tuning can be difficult and time-consuming
4. **Derivative Noise** - Derivative term amplifies measurement noise
5. **Integral Windup** - Integral term can accumulate to problematic levels during saturation
6. **Poor Disturbance Rejection** - May respond slowly to external disturbances
7. **No Feedforward** - Cannot anticipate known disturbances or setpoint changes
8. **Limited Adaptability** - Fixed parameters don't adapt to changing system dynamics