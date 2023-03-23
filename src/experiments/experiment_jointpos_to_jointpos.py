# This experiment will be done in a lab setting with two boxes.
# We will get the starting position and end position as the 6 angles of the robot arm's joints.
# We then will run our GOMP algorithm to get the best solution in the form of waypoints.

from experiments_init import create_two_bin_lab_world, move_by_waypoints
from gomp import GOMP

world_obstacles = create_two_bin_lab_world()

gomp_solver = GOMP()
for obstacle in world_obstacles:
    gomp_solver.add_obstacle(obstacle)

waypoints = gomp_solver.run()

# TODO - implement obtaining start pos
start_pos = [0, 0, 0, 0, 0, 0]
move_by_waypoints(start_pos=start_pos, waypoints=waypoints)