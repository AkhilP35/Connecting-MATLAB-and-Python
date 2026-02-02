import matlab.engine
import os
#import numpy as np

eng = matlab.engine.start_matlab("-nodisplay")
print("MATLAB started")


eng.addpath("/Users/akhilpatel/Desktop/Dissertation/WFSim-master")
print("Path added")

yaw_angles = 20
#yaw_angles = matlab.double(yaw_angles)
#eng.workspace['yaw_angles'] = matlab.double(yaw_angles)
#eng.turbInputSet.phi = matlab.double(yaw_angles)

total_avg_power = eng.WFSim_simulation_use(yaw_angles)
print("WFSim demo completed")

eng.quit
print("MATLAB closed")

print(total_avg_power)