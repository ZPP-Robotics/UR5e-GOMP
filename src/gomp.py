from math import inf
import sys
sys.path.append('../OSQP-Solver/debug/tests/')
import gomp

class GOMP:
    def __init__(self):
        self.obstacles = []

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def convert_obstacles(self):
        obstacle_constraints = []
        
        (minx, miny, minz) = (-inf, -inf, -inf)
        (maxx, maxy, maxz) = (inf, inf, inf)

        for obstacle in self.obstacles:
            (obstacle_from_lines, x_constraints, y_constraints, z_constraints) = obstacle.convert()
            for line in obstacle_from_lines:
                obstacle_constraints.append(line)

            (minx, miny, minz) = (max(minx, x_constraints[0]), max(miny, y_constraints[0]), max(minz, z_constraints[0]))
            (maxx, maxy, maxz) = (min(maxx, x_constraints[1]), min(maxy, y_constraints[1]), min(maxz, z_constraints[1]))

        return (obstacle_constraints, ((minx, miny, minz), (maxx, maxy, maxz)))

    def run_solver(self, start_pos_joints, end_pos_joints, time_step, waypoints_count, 
                   velocity_constraints, acceleration_constraints, position_constraints, 
                   line_constraints_c, constraints3d: tuple[tuple[float, float, float], tuple[float, float, float]]):
        N_DIM = 6
        Q_MIN = -6.283185307179586232
        Q_MAX = 6.283185307179586232
        M_PI = 3.14159265358979323846
        INF = 1.00000000000000002e+30

        obstacles = line_constraints_c

        (_, res) = gomp.solve_1(start_pos_joints, end_pos_joints, time_step, waypoints_count, 
                                velocity_constraints, acceleration_constraints, position_constraints, 
                                constraints3d, obstacles)
        return res

    def run(self):
        (line_constraints_c, constraints3d) = self.convert_obstacles()
        gomp_solutions = self.run_solver(line_constraints_c, constraints3d)

        return gomp_solutions

