from obstacles import Obstacle, BoxParallelXYZ, HorizontalLine

def create_two_bin_lab_world():
    box1 = BoxParallelXYZ((271.07, 507.62, 212.65), 51, 51, 25)
    box2 = BoxParallelXYZ((271.07, 0.94, 212.65), 51, 51, 25)

    return [box1, box2]