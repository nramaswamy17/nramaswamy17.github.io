---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
---

{% include base_path %}

Projects
======
* **Path Planning Algorithms: Theory & Implementation**
  * Implemented and analyzed multiple path planning algorithms: ([View Motion Planning Projects](/motion-planning/))
    * Learning-Based Methods
      * Diffusion Policy
    * Safety-Constrained Control
      * Control Barrier Function - Quadratic Programming (CBF-QP)
    * Model Predictive Control
      * Model Predictive Path Integral (MPPI)
    * Trajectory Optimization
      * Stochastic Trajectory Optimization for Motion Planning (STOMP), Covariant Hamiltonian Optimization for Motion Planning (CHOMP), Trajectory Optimization (TrajOpt), Differential Dynamic Programming (DDP)
    * Sampling-Based Planning
      * Rapidly-exploring Random Trees (RRT/ RRT\*), Fast Marching Trees (FMT\*), Neural RRT\* 
    * Graph-Based Search
      * Dijkstra, A\*, Dynamic A\* (D\*)
  * Created detailed mathematical analyses and explanations for each algorithm, documenting theoretical foundations and practical implementations 
* **Gunshot Classification Device**
  * Developed and trained classification CNN models using Pytorch – Tested LeNet5, ResNet50, and multiple custom models based on varying input shapes (1D vs 2D vector) and input styles (flattened raw audio vs Mel-Frequency Cepstral Coefficients); resulted in 99% accuracy in "ideal" test conditions, and ~20-25% accuracy in noise-heavy conditions (state-of-the-art in noise-heavy conditions is 14% accuracy)
  * Created Python program to label audio files with the location of the signal and to chop the audio file with random quantity of noise leading and lagging the signal, improving model robustness during testing by preventing memorization of signal location in the input array

Skills
======
* **Programming Languages**: Python, Go, SQL, Julia, C
* **Frameworks & Tools**: Pytorch, Kubernetes, Tableau, Keyence, Minitab, Excel, AutoCAD, Revit
* **Machine Learning**: CNN models, LSTM models, audio classification, statistical analysis
* **Data Engineering**: ETL processes, MySQL, data analysis, forecasting models
* **Manufacturing**: Statistical Process Control (SPC), Gage R&R studies, OEE metrics, Computer Vision
* **Life**: Dog Petting 

Education
======
* M.S. Computer Science & Engineering, University of Nevada, Reno, GPA 4.00 (Expected May 2026)
* B.S. Industrial and Systems Engineering, Rensselaer Polytechnic Institute, GPA 3.56 (Dec 2021)

Work Experience
======

**TESLA INC.**  
*Software Engineering Intern*  \| *Jan 2025 – May 2025*

  * Deployed a containerized, testable install script for Tesla PLM software using mdrip, ensuring repeatable installations on a complex system
  * Developed a tool & design doc to diagnose TLS connection errors in distributed Java systems, slashing RCA time from hours/days to seconds

**TESLA INC.**  
*Data Analyst Intern*  \| *May 2024 – Aug 2024*

  * Implemented ETL to store Manufacturing Variance data across all of GFNV, coordinated with engineering and finance teams to validate estimated costs and realized waste; reduced analysis time by 99% for a given part and raised awareness of unseen factory waste
  * Drove investigation into large scale waste using variance ETL and found inverter line process gap, resulted in 7-figure annualized savings

**TESLA INC.**  
*Associate Process Engineer*  \| *Dec 2022 – Dec 2023*

  * Built and deployed Extract, Transform, Load (ETL) processes using containerized Python and SQL applications – resulting MySQL tables permitted more advanced data analyses and creation of much faster Tableau dashboards
  * Made improvements to and troubleshot production Computer Vision software, resulting in 4% yield increase / line on highest utilized station
  * Established OLE, Utilization, and OEE metrics on production lines as well as respective targets for Yield, Availability, and Performance; bottleneck analysis pointed out potential to improve throughput capacity by 28% through targeted OEE improvements
  * Performed Gage R&R Study, identifying high electrical tester variance as source of yield loss and driving investigation into equipment
  * Lead project to improve cooling system on manufacturing line, worked with facilities design, construction, manufacturing engineering, and design engineering to develop design, expected to improve line throughput capacity by 41%
  * Established Statistical Process Control (SPC) standards with proper alarms, supporting line monitoring to process technicians for line capability

**TESLA INC.**  
*Associate Reliability Engineer*  \| *Sept 2021 – Dec 2022*

  * Utilized Python and SQL to track irregular asset failures and flag them, improving the Reliability team's Preventative Maintenance efforts
  * Developed and established asset tree data structure for facilities electrical equipment to optimize maintenance planning during downtime
  * Troubleshot electrical and mechanical facilities equipment failures, implemented data acquisition methods, and spearheaded design improvements using P&ID or CAD markups; using collected data and statistical analysis to justify and illustrate effectiveness of design changes
  * Led Root Cause Analysis meetings with various facilities teams to understand engineering / procedural cause issues and drive implementation of corrective actions through coordination with internal departments or third-party contractors, mitigating repeat failure modes

**TESLA INC.**  
*Reliability Engineering Intern*  \| *Jan 2021 – Sept 2021*

  * Implemented Python software to predict and flag potential stockouts based on usage data and recommend reorder points using Holt's model
  * Designed Python software to import unstructured data from contractors and validate the entries against the company database to catch data entry mistakes and change the format so the software team's programs could seamlessly integrate the new data
  * Revamped Gigafactory 1's facility warehouse system by implementing primary keys, date stamps, request stages, etc. to provide structure for future data analysis and by establishing a priority system to improve important request flow; led to >50% improvement in priority request flow

**BIOGEN INC.**  
*Human Performance / EHS Data Scientist Co-op*  \| *Jul 2020 – Dec 2020*

  * Produced LSTM models in Amazon Sagemaker to enhance accuracy of previous SES models to forecast future company product demand
  * Developed a Tableau heatmap for manufacturing processes with drill-down options to communicate deviation locations and improve production throughput, permitting faster resolution of production downtime while also improving stakeholder experience
  * Digitalized information dashboards in Tableau and Power BI to update with live data and developed new databases to create product tracking across the production line
  * Created forecasts using Python and SQL for future deviations and designed human performance metrics on root cause investigations to track resource effectiveness, driving process changes to improve efficiency


