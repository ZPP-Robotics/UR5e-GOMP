# This experiment will be done in a lab setting with two boxes.
# We will get the starting position and end position as the 6 angles of the robot arm's joints.
# We then will run our GOMP algorithm to get the best solution in the form of waypoints.
import sys
sys.path.append('../')
from experiments_init import create_two_bin_lab_world, move_by_waypoints
from gomp import GOMP
import pandas as pd
import rtde_control

world_obstacles = create_two_bin_lab_world()
(line, a, b) = world_obstacles.convert()
print(line)
print(a)
print(b)

# gomp_solver = GOMP()
# for obstacle in world_obstacles:
#     gomp_solver.add_obstacle(obstacle)

# waypoints = gomp_solver.run()
df = pd.read_csv('output3.csv', delim_whitespace=True)
path = df.values

df['velo'] = 1
df['acc'] = 1
df['blend'] = 0.5

# TODO - implement obtaining start pos
# start_pos = [-7.143, -7.435, 7.20, -7.001, 7.12, 7.04]
start_pos = [1.1109414100646973, -1.7925297222533167, -1.8433074951171875, -1.07748635232959, 1.5788192749023438, 2.88077712059021]

print("connecting")

ROBOT = rtde_control.RTDEControlInterface("10.0.0.219")

ROBOT.moveJ(start_pos)
print("start")
ROBOT.moveJ(df.values[::3])
print("done")
# move_by_waypoints(start_pos=start_pos, waypoints=df.values)