# This experiment will be done in a lab setting with two boxes.
# We will get the starting position and end position as the 6 angles of the robot arm's joints.
# We then will run our GOMP algorithm to get the best solution in the form of waypoints.
import sys
sys.path.append('../')
sys.path.append('../../OSQP-Solver/debug/tests/')
from experiments_init import create_two_bin_lab_world, move_by_waypoints
from solver import GOMP
import gomp

# INITIAL SETUP ---------------------------------------------------------------------
N_DIM = 6
Q_MIN = -6.283185307179586232
Q_MAX = 6.283185307179586232
M_PI = 3.14159265358979323846
INF = 1.00000000000000002e+30

time_step = 0.1
waypoints_count = 40 + 2

position_constraints = ([Q_MIN] * N_DIM, [Q_MAX] * N_DIM)
velocity_constraints = ([-M_PI] * N_DIM, [M_PI] * N_DIM)
acceleration_constraints = ([-M_PI * 800 / 180] * N_DIM, [M_PI * 800 / 180] * N_DIM)
#------------------------------------------------------------------------------------


# start_pos = [1.1109414100646973, -1.7925297222533167, -1.8433074951171875, -1.07748635232959, 1.5788192749023438, 2.88077712059021]
# start_pos = [36.88, -128.12, -97.43, -41.94, 87.60, 38.65]
# for i in range(len(start_pos)):
#     start_pos[i] = start_pos[i] * M_PI / 180
# print(start_pos)

start_pos = [1.1106168031692505, -1.9419242344298304, -1.959261417388916, -0.8121242088130494, 1.577633261680603, 2.8825175762176514]
end_pos = [-0.16207582155336553, -2.0053416691222132, -1.8414853811264038, -0.8576411169818421, 1.5140776634216309, -0.08804780641664678]
# end_pos = [-0.013442818318502248, -1.2449665826610108, -1.8534693717956543, -1.6163512669005335, 1.5796295404434204, 0.054004184901714325]

world_obstacles = create_two_bin_lab_world()

gomp_solver = GOMP(time_step, waypoints_count, position_constraints, velocity_constraints, acceleration_constraints)
for obstacle in world_obstacles:
    gomp_solver.add_obstacle(obstacle)

print("Obstacles:")
gomp_solver.print_obstacles()

print("RUN")
(code, waypoints) = gomp_solver.run(start_pos, end_pos, 0.1)
waypoints = waypoints[:(len(waypoints)//2)]

if (code == gomp.OsqpExitCode.kOptimal):
    print(len(waypoints[:(len(waypoints))])//6)
    print("Obstacles:")
    gomp_solver.print_obstacles()

    path = []
    for i in range(0, len(waypoints), 6):
        next_joint_pos = waypoints[i:i+6]
        path.append(next_joint_pos)

    # next_joint_pos = waypoints[-6:-1]
    # path.append(next_joint_pos)
    for el in path:
        print(el)

    # move_by_waypoints(start_pos=start_pos, waypoints=path)
else:
    print("ERROR!")
    print("No solution found")
    print(code)