# This experiment will be done in a lab setting with two boxes.
# We will get the starting position and end position as the 6 angles of the robot arm's joints.
# We then will run our GOMP algorithm to get the best solution in the form of waypoints.

from experiments_init import create_two_bin_lab_world
from gomp import GOMP

world_obstacles = create_two_bin_lab_world()

gomp_solver = GOMP()
for obstacle in world_obstacles:
    gomp_solver.add_obstacle(obstacle)

waypoints = gomp_solver.run()

# TODO - move ur5e arm through obtained waypoints.
