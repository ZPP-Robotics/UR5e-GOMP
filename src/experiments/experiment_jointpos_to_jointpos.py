# This experiment will be done in a lab setting with two boxes.
# We will get the starting position and end position as the 6 angles of the robot arm's joints.
# We then will run our GOMP algorithm to get the best solution in the form of waypoints.

import sys
sys.path.append('../')
sys.path.append('../../OSQP-Solver/debug/tests/')
from colorama import Fore, Back, Style

from experiments_init import experiment_joints

# INITIAL SETUP ---------------------------------------------------------------------
N_DIM = 6
Q_MIN = -6.283185307179586232
Q_MAX = 6.283185307179586232
M_PI = 3.14159265358979323846
INF = 1.00000000000000002e+30

time_step = 0.1
waypoints_count = 40 + 2

position_constraints = ([Q_MIN] * N_DIM, [Q_MAX] * N_DIM)
velocity_constraints = ([-M_PI / 10] * N_DIM, [M_PI / 10] * N_DIM)
acceleration_constraints = ([-M_PI * 800 / 180] * N_DIM, [M_PI * 800 / 180] * N_DIM)
#------------------------------------------------------------------------------------
# radiuses = [0.05, 0.05, 0.05, 0.05, 0.15]

# # start_pos = [1.1109414100646973, -1.7925297222533167, -1.8433074951171875, -1.07748635232959, 1.5788192749023438, 2.88077712059021]
# start_pos = [36.88, -128.12, -97.43, -41.94, 87.60, 38.65]
# for i in range(len(start_pos)):
#     start_pos[i] = start_pos[i] * M_PI / 180
# print(start_pos)

# # start_pos = [1.1106168031692505, -1.9419242344298304, -1.959261417388916, -0.8121242088130494, 1.577633261680603, 2.8825175762176514]
# end_pos = [-0.16207582155336553, -2.0053416691222132, -1.8414853811264038, -0.8576411169818421, 1.5140776634216309, -0.08804780641664678]
# # end_pos = [-0.013442818318502248, -1.2449665826610108, -1.8534693717956543, -1.6163512669005335, 1.5796295404434204, 0.054004184901714325]


# experiment(start_pos, end_pos, radiuses)

# ------------------------------------------------------------------------------------
radiuses = [0.03, 0.05, 0.01, 0.05, 0.05, 0.10]

# start_pos = [1.1109414100646973, -1.7925297222533167, -1.8433074951171875, -1.07748635232959, 1.5788192749023438, 2.88077712059021]
# start_pos = [36.88, -128.12, -97.43, -41.94, 87.60, 38.65]
# start_pos = [45, -128, -89, -59, 87, 49]
start_pos = [34, -114, -104, -52, 86, 37]
for i in range(len(start_pos)):
    start_pos[i] = start_pos[i] * M_PI / 180
print(start_pos)

# start_pos = [1.1106168031692505, -1.9419242344298304, -1.959261417388916, -0.8121242088130494, 1.577633261680603, 2.8825175762176514]
# end_pos = [-0.16207582155336553, -2.0053416691222132, -1.8414853811264038, -0.8576411169818421, 1.5140776634216309, -0.08804780641664678]
# end_pos = [-0.013442818318502248, -1.2449665826610108, -1.8534693717956543, -1.6163512669005335, 1.5796295404434204, 0.054004184901714325]

# Testing GOMP waypoint count for final experiment start positions and fixed end position
# end_pos = [-0.2443, -1.9547, -1.8675, -0.8726, 1.5533, -0.0523]
# start_pos = [0.4014, -2.0420, -1.4137, -1.2217, 1.5533, 0.5934]
# start_pos =    [0.5235, -1.9547, -1.5533, -1.1693, 1.5707, 0.7330]
# start_pos = [0.5885, -1.7104, -1.8849, -1.0995, 1.5707, 0.7853]
# start_pos =  [0.6108, -1.4311, -2.1642, -1.0995, 1.5533, 0.8203]
# start_pos =  [0.6632, -2.0071, -1.4660, -1.2042, 1.5707, 0.8552]
# start_pos = [0.6806, -1.4835, -2.1118, -1.0821, 1.5707, 0.8901]
# start_pos =  [0.7155, -1.9024, -1.6406, -1.1519, 1.5707, 0.9250]
# start_pos =  [0.7853, -1.7976, -1.7802, -1.1170, 1.5707, 0.9773]
# start_pos =  [0.8203, -1.5707, -2.0420, -1.0821, 1.5707, 1.0122]
# start_pos = [0.8377, -1.8151, -1.7453, -1.1170, 1.5707, 1.0297]
# start_pos =  [0.8552, -1.7104, -1.8849, -1.0995, 1.5707, 1.0471]
# start_pos =  [1.0122, -1.6406, -1.9547, -1.0995, 1.5707, 1.2217]

end_pos = [-23, -106, -117, -43, 87, -20]
for i in range(len(end_pos)):
    end_pos[i] = end_pos[i] * M_PI / 180
print(end_pos)

experiment_joints(start_pos, end_pos, radiuses,
                  time_step, waypoints_count, position_constraints, velocity_constraints, acceleration_constraints)

# experiment_joints(end_pos, start_pos, radiuses,
#                   time_step, waypoints_count, position_constraints, velocity_constraints, acceleration_constraints)