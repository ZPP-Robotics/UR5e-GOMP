class GOMP:
    def __init__(self):
        self.obstacles = []

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def convert_obstacles(self):
        obstacle_constraints = []
        for obstacle in self.obstacles:
            obstacle_constraints.append(obstacle.convert())

        return obstacle_constraints

    def run_solver(self):
        pass

    def run(self):
        line_constraints_c = self.convert_obstacles()
        gomp_solutions = self.run_solver(line_constraints_c)

        return gomp_solutions

