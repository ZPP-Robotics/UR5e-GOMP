class GOMP:
    def __init__(self):
        self.obstacles = []

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def convert_obstacles(self):
        pass

    def run_solver(self):
        pass

    def run():
        line_constraints_c = self.convert_obstacles()
        gomp_solutions = self.run_solver(line_constraints_c)

        return gomp_solutions

