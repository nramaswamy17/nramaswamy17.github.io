---
layout: archive
title: "MPC Demo"
permalink: /mpc-demo/
author_profile: true
---

{% include base_path %}

# Model Predictive Control (MPC) Demos
1. Lane Keeping Assist System
2. Lane Changing Assist System

---

<div style="text-align: center; margin: 20px 0;">
  <iframe src="{{ base_path }}/_pages/mpc_lanekeep.html" 
          width="100%" 
          height="800px" 
          frameborder="0"
          style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </iframe>
</div>

---

### Cost Function
$$\text{Cost} = \min \sum_{k=0}^{N-1} \left[Q_1(y_k - y_{\text{ref}})^2 + Q_2\theta_k^2 + R_1\delta_k^2 + R_2(\delta_k - \delta_{k-1})^2\right]$$

Where:
- **$$y_k$$**: Lateral position at step k
- **$$y_{\text{ref}}$$**: Reference lane center position
- **$$\theta_k$$**: Vehicle heading angle
- **$$\delta_k$$**: Steering angle command
- **$$\delta_{k-1}$$**: Previous steering angle command
- **$$Q_1$$**: Lateral position tracking weight
- **$$Q_2$$**: Heading angle weight
- **$$R_1$$**: Steering angle weight
- **$$R_2$$**: Steering rate weight (smoothness)
- **$$N$$**: Prediction horizon length

### Dynamics
The controller uses a bicycle model for vehicle dynamics.

### Optimization
- Solves the optimization problem at each control step using a grid search approach.  
- Splits the steering state space into 41 options from -30 to +30 degrees and picks the lowest cost approach. 
- This was a simpler first approach - future posts will use partial derivatives and numerical optimization to find a true minimum, with eventual projects centering on Neural MPC


---

<div style="text-align: center; margin: 20px 0;">
  <iframe src="{{ base_path }}/_pages/mpc_lanechange.html" 
          width="100%" 
          height="1100px" 
          frameborder="0"
          style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </iframe>
</div>

---
### Cost function
$$\text{Cost} = \sum_{k=0}^{N-1} \left[
\begin{align}
w_k \cdot Q_1(y_k - y_{\text{ref},k})^2 + \
w_k \cdot Q_{2}(s_k)(\theta_k - \theta_{\text{desired}}(e_{y,k}))^2 +
R_1(\delta_{\text{input}} \cdot e^{-\alpha k})^2 + \newline
R_2(\delta_{\text{input}}(e^{-\alpha k} - e^{-\alpha (k-1)}))^2 + \
Q_v(v_k - v_{\text{ref}})^2 + \
P_{\text{heading}}(s_k, \theta_k)
\end{align}
\right]$$

Where:
- **$$w_k = 1 + 0.1k$$**: Time-weighted importance factor
- **$$Q_{2,\text{adaptive}}$$**: Varies by the state of lane change
- **$$\theta_{\text{desired},k}$$**: Can be non-zero during lane changes
- **$$\alpha = 0.05$$**: Adaptive heading weight parameter
- **$$Q_v = 0.1$$**: Velocity tracking weight
- **$$R_2 = 2.0$$**: Steering smoothness weight
- **$$P_{\text{heading}}(s,\theta)$$**: Quadratic barrier penalty if lane changing AND $$\\|\theta\\| > 1.5 \\cdot \theta_{\max}$$

### Dynamics
This also uses the bicycle model

### Optimization
- Solves the optimization problem at each control step using a grid search approach.  
- Splits the steering state space into 501 options from -30 to +30 degrees and picks the lowest cost approach. 

---

<div style="text-align: center; margin: 20px 0;">
  <iframe src="{{ base_path }}/_pages/mpc_obsavoidance.html" 
          width="100%" 
          height="1100px" 
          frameborder="0"
          style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </iframe>
</div>

---

*Note: This demo is best viewed on desktop devices with a web browser that supports HTML5 Canvas.*
