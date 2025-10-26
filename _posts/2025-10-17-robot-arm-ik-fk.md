---
title: "Robot Arm Forward / Inverse Kinematics"
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

# Single Joint Robot Arm

A single joint is defined, where rotation along one axis is defined. 

All movement is governed by a PID controller. 

## Forward Kinematics

![Robot Arm Forward Kinematics](/post_data/robot-arm-fk-ik/single-arm-fk.png)

### Question Answered
Where will the system be located at, given I rotate my arm by some known quantity?

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

<video muted playsinline loop preload="none" poster="/post_data/robot-arm-fk-ik/single-arm-ik.png" data-src="/post_data/robot-arm-fk-ik/single-arm-ik.mp4"></video>

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

### Question Answered
How should I rotate my arm so that my system ends up at some specified location?

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