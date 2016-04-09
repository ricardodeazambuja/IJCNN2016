# Experiments used for the paper submitted to IJCNN2016
# Diverse, Noisy and Parallel: a New Spiking Neural Network Approach for Humanoid Robot Control

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


OBS:  

BEE SNN simulator:  
https://github.com/ricardodeazambuja/LiquidStateMachine-Python

Python scripts in general:  
https://github.com/ricardodeazambuja/Python-UTILS

V-REP simulator:  
http://www.coppeliarobotics.com/downloads.html




