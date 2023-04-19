# This experiment will be done in a lab setting with two boxes.
# We will get the starting position and end position as the 6 angles of the robot arm's joints.
# We then will run our GOMP algorithm to get the best solution in the form of waypoints.
import sys
sys.path.append('../')
sys.path.append('../../OSQP-Solver/debug/tests/')
from experiments_init import create_two_bin_lab_world, move_by_waypoints
from solver import GOMP
import pandas as pd
import rtde_control

N_DIM = 6
Q_MIN = -6.283185307179586232
Q_MAX = 6.283185307179586232
M_PI = 3.14159265358979323846
INF = 1.00000000000000002e+30

time_step = 0.1
waypoints_count = 40 + 2

start_pos = [0] * N_DIM
end_pos = [M_PI//2] + [0] * (N_DIM - 1)

position_constraints = ([Q_MIN] * N_DIM, [Q_MAX] * N_DIM)
velocity_constraints = ([-M_PI] * N_DIM, [M_PI] * N_DIM)
acceleration_constraints = ([-M_PI * 800 / 180] * N_DIM, [M_PI * 800 / 180] * N_DIM)

world_obstacles = create_two_bin_lab_world()
# (line, a, b) = world_obstacles[0].convert()
# print(line)
# print(a)
# print(b)

gomp_solver = GOMP(time_step, waypoints_count, position_constraints, velocity_constraints, acceleration_constraints)
for obstacle in world_obstacles:
    gomp_solver.add_obstacle(obstacle)

print("Obstacles:")
gomp_solver.print_obstacles()

print("RUN")
waypoints = gomp_solver.run(start_pos, end_pos)
# df = pd.read_csv('output_trajectory.csv', delim_whitespace=True)
# path = df.values

# print(path[::3])

print(len(waypoints[:(len(waypoints)//2)])//6)

waypoints = waypoints[:(len(waypoints)//2)]

path = []
for i in range(0, len(waypoints), 6):
    path.append(waypoints[i:i+6])

print(path)

#  = waypoints
# df['velo'] = 1
# df['acc'] = 1
# df['blend'] = 0.5

# TODO - implement obtainindf['velo'] = 1
# df['acc'] = 1
# df['blend'] = 0.5g start pos
start_pos = [0, 0, 0, 0 ,0 ,0]
# start_pos = [-7.143, -7.435, 7.20, -7.001, 7.12, 7.04]
# start_pos = [1.1109414100646973, -1.7925297222533167, -1.8433074951171875, -1.07748635232959, 1.5788192749023438, 2.88077712059021]
#
print("connecting")

ROBOT = rtde_control.RTDEControlInterface("10.0.0.219")

ROBOT.moveJ(start_pos)
print("start")
ROBOT.moveJ(path)
print("done")
# print(path)
# move_by_waypoints(start_pos=start_pos, waypoints=waypoints)