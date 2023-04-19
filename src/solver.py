from math import inf
# import sys
# sys.path.append('../../OSQP-Solver/debug/tests/')
import gomp

class GOMP:
    def __init__(self, time_step, waypoints_count, position_constraints, velocity_constraints, acceleration_constraints):
        self.obstacles = []
        self.time_step = time_step
        self.waypoints_count = waypoints_count

        self.position_constraints = position_constraints
        self.velocity_constraints = velocity_constraints
        self.acceleration_constraints = acceleration_constraints
                

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def convert_obstacles(self):
        obstacle_constraints = []
        
        (minx, miny, minz) = (-inf, -inf, -inf)
        (maxx, maxy, maxz) = (inf, inf, inf)

        for obstacle in self.obstacles:
            (obstacle_from_lines, min_constraints, max_constraints) = obstacle.convert()
            for line in obstacle_from_lines:
                obstacle_constraints.append(line)

            (minx, miny, minz) = (max(minx, min_constraints[0]), max(miny, min_constraints[1]), max(minz, min_constraints[2]))
            (maxx, maxy, maxz) = (min(maxx, max_constraints[0]), min(maxy, max_constraints[1]), min(maxz, max_constraints[2]))

        return (obstacle_constraints, ((minx, miny, minz), (maxx, maxy, maxz)))
    
    def print_obstacles(self):
        (obstacle_constraints, ((minx, miny, minz), (maxx, maxy, maxz))) = self.convert_obstacles()
        print(obstacle_constraints)
        print(minx, miny, minz)
        print(maxx, maxy, maxz)


    def run_solver(self, start_pos_joints, end_pos_joints,
                   line_constraints_c, constraints3d: tuple[tuple[float, float, float], tuple[float, float, float]]):

        obstacles = line_constraints_c

        (_, res) = gomp.solve_1(start_pos_joints, end_pos_joints, 
                                self.time_step, self.waypoints_count, 
                                self.velocity_constraints, self.acceleration_constraints, self.position_constraints, 
                                constraints3d, obstacles)
        return res

    def run(self, start_pos, end_pos):
        (line_constraints_c, constraints3d) = self.convert_obstacles()
        gomp_solutions = self.run_solver(start_pos, end_pos, line_constraints_c, constraints3d)

        return gomp_solutions

