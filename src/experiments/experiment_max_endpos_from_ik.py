# This experiment will be done in a lab setting with two boxes.
# We will get the starting position as the 6 angles of the robot arm's joints, 
# and the end position by choosing the inverse kinematics solution with the greatest,
# angle in the second joint (the elbow joint).
# We then will run our GOMP algorithm to get the best solution in the form of waypoints.

# Finally - not run or finished

from experiments_init import create_two_bin_lab_world, move_by_waypoints
from gomp import GOMP

world_obstacles = create_two_bin_lab_world()

gomp_solver = GOMP()
for obstacle in world_obstacles:
    gomp_solver.add_obstacle(obstacle)

# TODO - after new run function is implemented update it here
waypoints = gomp_solver.run()

# TODO - implement obtaining start_pos
start_pos = [0, 0, 0, 0, 0, 0]
move_by_waypoints(start_pos=start_pos, waypoints=waypoints)

# This experiment will be done in a lab setting with two boxes.
# We will get the starting position as the 6 angles of the robot arm's joints, 
# and the end position by choosing the best inverse kinematics solution with the 
# fastest path returned by the GOMP algorithm.

# Finally - not run or finished