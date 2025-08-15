---
title: "Control Barrier Function Quadratic Programming (CBF-QP)"
date: 2025-08-13
published: false
permalink: /posts/2025/08/cbf-qp-explained/
categories: motion-planning
tags:
  - algorithms
  - safety-control
  - robotics
  - control-barriers
  - optimization
  - computer-science
---


## Article Goal
Explain CBF-QP (Control Barrier Function Quadratic Programming) for safety-critical control systems

## What is CBF-QP?
**CBF-QP** is a control methodology that unifies Control Barrier Functions (CBFs) with Control Lyapunov Functions (CLFs) through quadratic programming (QP) to ensure safety while achieving performance objectives. CBF-QP provides formal safety guarantees by constraining control inputs to maintain forward invariance of safe sets, while simultaneously optimizing for desired system performance.

**[CBF-QP: Written Walkthrough (In Progress)](/files/CBF-QP.pdf)**

## Core Concepts
1. **Forward Set Invariance** - Ensures the system remains within a safe set for all future time
2. **Barrier Function Certificates** - Uses CBFs to provide mathematical proofs of safety
3. **Quadratic Program Formulation** - Combines safety constraints and performance objectives in a QP
4. **Real-Time Optimization** - Solves the QP at each time step for online control

## The Math

### Safe Set Definition
Define a safe set $$\mathcal{C}$$ as:
$$\mathcal{C} = \{x \in \mathbb{R}^n : h(x) \geq 0\}$$

Where $$h(x)$$ is a continuously differentiable function defining the boundary of the safe region.

### Control Barrier Function
A function $$h(x)$$ is a Control Barrier Function if there exists a class $$\mathcal{K}$$ function $\alpha$ such that:
$$\sup_{u \in U} \left[ L_f h(x) + L_g h(x) u \right] \geq -\alpha(h(x))$$

Where:
- $$L_f h(x) = \nabla h(x) \cdot f(x)$$ is the Lie derivative of $h$ along $f$
- $$L_g h(x) = \nabla h(x) \cdot g(x)$$ is the Lie derivative of $h$ along $g$
- $$\dot{x} = f(x) + g(x)u$$ is the control-affine system

### Control Lyapunov Function
A function $$V(x)$$ is a Control Lyapunov Function if there exists class $$\mathcal{K}$$ functions $$\alpha_1, \alpha_2, \alpha_3$$ such that:
$$\alpha_1(\|x\|) \leq V(x) \leq \alpha_2(\|x\|)$$

And for all $x \neq 0$:
$$\inf_{u \in U} \left[ L_f V(x) + L_g V(x) u \right] \leq -\alpha_3(\|x\|)$$

### CBF-QP Formulation
The standard CBF-QP is formulated as:
$$\begin{align}
u^* = \arg\min_{u,\delta} \quad & \|u - u_{\text{des}}(x)\|^2 + p\delta^2 \\
\text{subject to} \quad & L_f h(x) + L_g h(x) u \geq -\alpha(h(x)) \quad \text{(CBF)} \\
& L_f V(x) + L_g V(x) u \leq -\gamma(V(x)) + \delta \quad \text{(CLF)} \\
& u \in U
\end{align}$$

Where:
- $$u_{\text{des}}(x)$$ is the desired control input
- $$\delta$$ is a relaxation variable for CLF constraint
- $$p > 0$$ is a penalty weight
- $$\gamma$$ is a class $$\mathcal{K}$$ function

### Safety Guarantee
If $$h(x_0) \geq 0$$ and the CBF constraint is satisfied, then:
$$h(x(t)) \geq 0 \quad \forall t \geq 0$$

This ensures the system remains in the safe set $\mathcal{C}$ for all time.

### Higher-Order CBFs
For relative degree $r > 1$, use Higher-Order CBFs:
$$\psi_0(x) = h(x), \quad \psi_i(x) = \dot{\psi}_{i-1}(x) + \alpha_i(\psi_{i-1}(x))$$

The constraint becomes:
$$L_f \psi_{r-1}(x) + L_g \psi_{r-1}(x) u \geq -\alpha_r(\psi_{r-1}(x))$$

## Algorithm Steps
1. **Define Safe Set** - Specify safety constraints through function $$h(x) \geq 0$$
2. **Construct CBF** - Verify $$h(x)$$ satisfies CBF conditions or design appropriate $$h(x)$$
3. **Design CLF** - Choose Lyapunov function $$V(x)$$ for desired performance objective
4. **Formulate QP** - Set up quadratic program with CBF and CLF constraints
5. **Solve Online** - At each time step, solve QP to get optimal control $$u^*$$
6. **Apply Control** - Execute computed control input $$u^*$$
7. **Update State** - Measure new state and repeat
8. **Monitor Safety** - Verify $$h(x) \geq 0$$ is maintained throughout execution



## Advantages of CBF-QP
1. **Formal Safety Guarantees** - Mathematical certificates of safety under specified conditions
2. **Real-Time Capability** - Fast QP solvers enable real-time implementation
3. **Flexible Framework** - Can handle multiple constraints and objectives simultaneously
4. **Performance Integration** - Unifies safety and performance in single optimization
5. **Proven Stability** - Maintains asymptotic stability when constraints are inactive
6. **Modular Design** - Easy to add new safety constraints or modify existing ones

## Limitations
1. **Model Dependency** - Requires accurate system model for Lie derivative computation
2. **CBF Construction** - Designing appropriate barrier functions can be challenging
3. **Local Validity** - Safety guarantees only valid within domain where CBF conditions hold
4. **Conservative Behavior** - May be overly conservative near constraint boundaries
5. **Parameter Tuning** - Performance depends on proper choice of class $\mathcal{K}$ functions
6. **Computational Requirements** - Requires real-time QP solver capability
