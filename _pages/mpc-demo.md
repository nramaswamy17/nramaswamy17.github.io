---
layout: archive
title: "MPC Demo"
permalink: /mpc-demo/
author_profile: true
---

{% include base_path %}

# Model Predictive Control (MPC) Lane Keeping Demo

This interactive demonstration showcases a Model Predictive Control (MPC) system for autonomous vehicle lane keeping. The simulation visualizes how MPC optimizes steering commands over a prediction horizon to maintain the vehicle within lane boundaries while following a curved road.

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

<div style="text-align: center; margin: 20px 0;">
  <iframe src="{{ base_path }}/_pages/mpc_lanechange.html" 
          width="100%" 
          height="1100px" 
          frameborder="0"
          style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
  </iframe>
</div>

---

## Technical Details

### Cost Function
$$\text{Cost} = \min \sum_{k=0}^{N-1} \left[Q_1(y_k - y_{\text{ref}})^2 + Q_2\theta_k^2 + R_1\delta_k^2 + R_2(\delta_k - \delta_{k-1})^2\right]$$

Where:
- **$$y_k$$**: Lateral position at step k
- **$$y_{\text{ref}}$$**: Reference lane center position
- **$$\theta_k$$**: Vehicle heading angle
- **$$\delta_k$$**: Steering angle command
- **$$N$$**: Prediction horizon length

### Dynamics
The controller uses a bicycle model for vehicle dynamics.

### Optimization
- Solves the optimization problem at each control step using a grid search approach.  
- Splits the steering state space into 50 options from -30 to +30 degrees and picks the lowest cost approach. 
- This was a simpler first approach - future posts will use partial derivatives and numerical optimization to find a true minimum, with eventual projects centering on Neural MPC

*Note: This demo is best viewed on desktop devices with a web browser that supports HTML5 Canvas.*
