---
title: "Robot Arm 2D Forward / Inverse Kinematics"
date: 2025-10-17
permalink: /posts/2025/10/robot-arm-fk-ik/
categories: projects
tags:
  - Kinematics
  - Inverse Kinematics
redirect_from:
excerpt: "Demonstrations of deterministic robot arm movements using FK / IK"
---

# Overview

Both Forward Kinematics (FK) and Inverse Kinematics (IK) will be computed and simulated for the following scenarios in 2D.
- Single Joint Robot Arm 
- Two-joint Robot Arm 
- Multi-joint Robot Arm

Forward Kinematics: Where will the system be located at, given I rotate my arm by some known quantity?

Inverse Kinematics: How should I rotate my arm so that my system ends up at some specified location?

View Code Repository: [Robot Arm Repository](https://github.com/nramaswamy17/C-Simulations/tree/main/ik_fk_review)

# Double Joint Robot Arm

Two joints are defined, where rotatation for both is along the same axis. 

The Forward Kinematics are super straightforward, though the Inverse Kinematics become more complicated. 

![Robot Arm Forward Kinematics](/post_data/robot-arm-fk-ik/robot-arm-2j.png)

## Forward Kinematics


### Equations
Elbow Position:
1. $$elbow_x = L_1 * cos(\theta _1)$$
2. $$elbow_y = L_1 * sin(\theta _1)$$

End Effector Position:
1. $$end_x = elbow_x + L_2 * cos(\theta _1 + \theta _2)$$
1. $$end_y = elbow_y + L_2 * sin(\theta _1 + \theta _2)$$

## Inverse Kinematics

<video controls muted playsinline loop preload="metadata" poster="/post_data/robot-arm-fk-ik/robot-arm-2j-cover.png" src="/post_data/robot-arm-fk-ik/robot-arm-2j.mp4" data-src="/post_data/robot-arm-fk-ik/robot-arm-2j.mp4"></video>

<script>
  const v = document.querySelector('video[data-src]');
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        if (!v.src) v.src = v.dataset.src;            // start loading
        v.play().catch(()=>{});                       // play if allowed
      } else {
        v.pause();
      }
    });
  }, {threshold: 0.5});
  io.observe(v);
</script>

The problem setup is defined in order to solve the inverse kinematics. 

![Robot Arm Inverse Kinematics Setup](/post_data/robot-arm-fk-ik/robot-arm-2j-ik.png)

## Derivation

Calculate the straight line distance from the base joint $$(0,0)$$ to the target $$(x,y)$$:

$$d = \sqrt{x^2 + y^2}$$

Recall the law of cosines:

$$c^2 = a^2 + b^2 - 2ab\cos(C)$$

$$d^2 = L_1^2 + L_2^2 + 2L_1L_2\cos(\theta_2)$$

Solve for $$\theta_2$$:

$$2L_1L_2\cos(\theta_2) = d^2 - L_1^2 - L_2^2$$

$$\cos(\theta_2) = \frac{d^2 - L_1^2 - L_2^2}{2L_1L_2}$$

$$\theta_2 = \arccos\left(\frac{d^2 - L_1^2 - L_2^2}{2L_1L_2}\right)$$

Now solve for $$\theta_1$$. Start with the forward kinematics:

$$x = L_1\cos(\theta_1) + L_2\cos(\theta_1+\theta_2)$$

$$y = L_1\sin(\theta_1) + L_2\sin(\theta_1 + \theta_2)$$

Expand using angle addition formulas:

$$x = L_1\cos(\theta_1) + L_2(\cos(\theta_1)\cos(\theta_2) - \sin(\theta_1)\sin(\theta_2))$$

$$y = L_1\sin(\theta_1) + L_2(\sin(\theta_1)\cos(\theta_2) + \cos(\theta_1)\sin(\theta_2))$$

Group by $$\cos(\theta_1)$$ and $$\sin(\theta_1)$$:

$$x = \cos(\theta_1)[L_1 + L_2\cos(\theta_2)] - \sin(\theta_1)[L_2\sin(\theta_2)]$$

$$y = \sin(\theta_1)[L_1 + L_2\cos(\theta_2)] + \cos(\theta_1)[L_2\sin(\theta_2)]$$

Define constants $$k_1$$, $$k_2$$ to simplify the expression since $$\theta_2$$ is known:

$$k_1 = L_1 + L_2\cos(\theta_2)$$

$$k_2 = L_2\sin(\theta_2)$$

So,

$$x = k_1\cos(\theta_1) - k_2\sin(\theta_1)$$

$$y = k_1\sin(\theta_1) + k_2\cos(\theta_1)$$

We have two equations, two unknowns.

Find $$\cos(\theta_1)$$ by multiplying both equations by constants: $$k_1 \cdot x$$, $$k_2 \cdot y$$:

$$k_1x = k_1^2\cos(\theta_1) - k_1k_2\sin(\theta_1)$$

$$k_2y = k_1k_2\sin(\theta_1) + k_2^2\cos(\theta_1)$$

Adding the equations gives:

$$\cos(\theta_1) = \frac{k_1x + k_2y}{k_1^2 + k_2^2}$$

Subtracting the first equation from the second gives:

$$\sin(\theta_1) = \frac{k_1y - k_2x}{k_1^2 + k_2^2}$$

Now we can solve for $$\theta_1$$ directly:

$$\theta_1 = \text{atan2}(\sin(\theta_1), \cos(\theta_1))$$

$$\theta_1 = \text{atan2}\left(\frac{k_1y - k_2x}{k_1^2 + k_2^2}, \frac{k_1x + k_2y}{k_1^2 + k_2^2}\right)$$

Simplifying (common denominator cancels):

$$\theta_1 = \text{atan2}(k_1y - k_2x, k_1x + k_2y)$$

By properties of atan2:

$$\theta_1 = \text{atan2}(y,x) - \text{atan2}(k_2, k_1)$$

---

## Final Solution

Given a target position $$(x,y)$$:

$$\theta_2 = \arccos\left(\frac{d^2 - L_1^2 - L_2^2}{2L_1L_2}\right)$$

$$\theta_1 = \text{atan2}(y,x) - \text{atan2}(k_2, k_1)$$

where:

$$k_1 = L_1 + L_2\cos(\theta_2)$$

$$k_2 = L_2\sin(\theta_2)$$

$$d = \sqrt{x^2 + y^2}$$

## Code
[Double Joint Robot Simulation Code](https://github.com/nramaswamy17/C-Simulations/tree/main/ik_fk_review/Double_Joint)

# Single Joint Robot Arm

A single joint is defined, where rotation along one axis is defined. 

All movement is governed by a PID controller. 

## Forward Kinematics

![Robot Arm Forward Kinematics](/post_data/robot-arm-fk-ik/single-arm-fk.png)

### Equations
Solve for $$x_f$$ and $$y_f$$
1. $$x_f = L \cos(\theta)$$  
2. $$y_f = L \sin(\theta)$$  

### Toy Example
- L = 3
- $$\theta$$ = 60 deg
- $$x_f = Lcos(\theta)$$ = 3 * cos(60) = 1.5
- $$y_f = Lsin(\theta)$$ = 3 * sin(60) = 2.598

## Inverse Kinematics

<video controls muted playsinline loop preload="metadata" poster="/post_data/robot-arm-fk-ik/single-arm-ik.png" src="/post_data/robot-arm-fk-ik/single-arm-ik.mp4" data-src="/post_data/robot-arm-fk-ik/single-arm-ik.mp4"></video>

<script>
  const v = document.querySelector('video[data-src]');
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        if (!v.src) v.src = v.dataset.src;            // start loading
        v.play().catch(()=>{});                       // play if allowed
      } else {
        v.pause();
      }
    });
  }, {threshold: 0.5});
  io.observe(v);
</script>

## Code
[Single Joint Robot Simulation Code](https://github.com/nramaswamy17/C-Simulations/tree/main/ik_fk_review/Single_Joint)

### Equations
Solve for $$\theta$$
1. $$\theta = arctan(y_f/x_f)$$

### Toy Example
- L = 3
- $$(x_f, y_f)$$ = (1.5, 2.598)
- $$tan(\theta) = y/x$$ _
- $$\theta = arctan(y/x) = arctan(2.598/1.5)$$ _
- $$\theta$$ = 60 deg

This can be gut-checked against our FK calculations.