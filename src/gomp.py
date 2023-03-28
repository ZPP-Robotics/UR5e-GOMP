class GOMP:
    def __init__(self):
        self.obstacles = []

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def convert_obstacles(self):
        obstacle_constraints = []
        
        minx = inf
        maxx = -inf

        miny = inf
        maxy = -inf
        
        minz = inf
        maxz = -inf

        for obstacle in self.obstacles:
            (obstacle_from_lines, x_constraints, y_constraints, z_constraints) = obstacle.convert()
            for line in obstacle_from_lines:
                obstacle_constraints.append(line)

            (minx, maxx) = (min(minx, x_constraints[0]), max(maxx, x_constraints[1]))
            (miny, maxy) = (min(miny, y_constraints[0]), max(maxy, y_constraints[1]))
            (minz, maxz) = (min(minz, z_constraints[0]), max(maxz, z_constraints[1]))

        return (obstacle_constraints, (minx, maxx), (miny, maxy), (minz, maxz))

    def run_solver(self, line_constraints_c, x_constraints, y_constraints, z_constraints):
        pass

    def run(self):
        (line_constraints_c, x_constraints, y_constraints, z_constraints) = self.convert_obstacles()
        gomp_solutions = self.run_solver(line_constraints_c, x_constraints, y_constraints, z_constraints)

        return gomp_solutions

