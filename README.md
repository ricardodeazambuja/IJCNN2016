# Experiments used for the paper ~~submitted to~~ presented at [IJCNN2016 / IEEE WCCI 2016](http://www.wcci2016.org/)
# Diverse, Noisy and Parallel: a New Spiking Neural Network Approach for Humanoid Robot Control

## Abstract:
How exactly our brain works is still an open question, but one thing seems to be clear: biological neural systems are computationally powerful, robust and noisy. Using the Reservoir Computing paradigm based on Spiking Neural Networks, also known as Liquid State Machines, we present results from a novel approach where diverse and noisy parallel reservoirs, totalling 3,000 modelled neurons, work together receiving the same averaged feedback. Inspired by the ideas of action learning and embodiment we use the safe and flexible industrial robot BAXTER in our experiments. The robot was taught to draw three different 2D shapes on top of a desk using a total of four joints. Together with the parallel approach, the same basic system was implemented in a serial way to compare it with our new method. The results show our parallel approach enables BAXTER to produce the trajectories to draw the learned shapes more accurately than the traditional serial one.

## The trajectories are always closed shapes (otherwise the initial and final values are different and the signal conditioning must be changed)

1) The trajectories are generated using a simulated BAXTER robot inside V-REP.
- BEE_Simulator_ArmControl_VREP_trajectories-generator_v1-SHAPE_NAME.ipynb
- /VREP_scenes/Baxter_IK_felt_pen_pick-and-place_learning_IJCNN2016.ttt
(cell templates come from BEE_Simulator_ArmControl_VREP_trajectories-generator_v1-TEMPLATES.ipynb)

2) Training data (output spikes) are generated using the notebook:
- BEE_Simulator_ArmControl_VREP_LSM_DATA-GENERATOR.ipynb
(there's also a testing session at the end of the notebook)

3) After the generation of the training data, it is necessary to train the readouts. This is done by:
- BEE_Simulator_ArmControl_VREP_LSM_LINEAR_REGRESSION.ipynb

4) With all the readout weights defined, it's possible to verify the system using only the LSMs:
- BEE_Simulator_ArmControl_VREP_LSM_DATA-TESTER.ipynb


## OBS:  

### BEE SNN simulator:  
https://github.com/ricardodeazambuja/BEE  

### Dynamic Time Warping:  
https://github.com/ricardodeazambuja/DTW

### Python scripts in general:  
https://github.com/ricardodeazambuja/Python-UTILS

### V-REP simulator:  
http://www.coppeliarobotics.com/downloads.html  
  
### Preprint version:  
https://github.com/ricardodeazambuja/IJCNN2016/blob/master/IJCNN2016_preprint.pdf

### Bibtex citation:
https://github.com/ricardodeazambuja/ricardodeazambuja.github.io/raw/master/public/citations/de_azambuja_diverse_2016.bib

### Final IEEE Xplore version:  
http://ieeexplore.ieee.org/document/7727325/

### Related works:  
https://github.com/ricardodeazambuja/ICONIP2016  
https://github.com/ricardodeazambuja/IJCNN2017  
https://github.com/ricardodeazambuja/IJCNN2017-2  
https://github.com/ricardodeazambuja/I2MTC2017-LSMFusion


## Other projects you may like to check:
* [colab_utils](https://github.com/ricardodeazambuja/colab_utils/): Some useful (or not so much) Python stuff for Google Colab notebooks
* [ExecThatCell](https://github.com/ricardodeazambuja/ExecThatCell): (Re)Execute a Jupyter (colab) notebook cell programmatically by searching for its label.
* [Maple-Syrup-Pi-Camera](https://github.com/ricardodeazambuja/Maple-Syrup-Pi-Camera): Low power('ish) AIoT smart camera (3D printed) based on the Raspberry Pi Zero W and Google Coral EdgeTPU
* [The CogniFly Project](https://github.com/thecognifly): Open-source autonomous flying robots robust to collisions and smart enough to do something interesting!
* [Bee](https://github.com/ricardodeazambuja/Bee): The Bee simulator is an open source Spiking Neural Network (SNN) simulator, freely available, specialised in Liquid State Machine (LSM) systems with its core functions fully implemented in C.

http://ricardodeazambuja.com/
