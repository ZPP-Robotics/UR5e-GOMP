import old_version_paths as ovp
from experiments_init import old_version_moveL
import time

M_PI = 3.14159265358979323846

paths = [ovp.path1, ovp.path2, ovp.path3, ovp.path4, ovp.path5, ovp.path6, 
         ovp.path7, ovp.path8, ovp.path9, ovp.path10, ovp.path11, ovp.path12]

# path = [[-0.013373676930562794, -1.2448429626277466, -1.8534636497497559, -1.616500040093893, 1.579637050628662, -3.5253079573260706],
# [-0.25514108339418584, -1.538846207117178, -1.669351577758789, -1.5068596315434952, 1.57954740524292, -3.5253124872790735],
# [-0.013544384633199513, -1.244895951156952, -1.8533998727798462, -1.6163064442076625, 1.5796618461608887, -3.5252824465381067]]

# path = [[0.6095210313796997, -1.7074171505370082, -1.6451969146728516, -1.3629313272288819, 1.5796432495117188, 2.8807694911956787],
#         [0.27833008766174316, -1.1971212488463898, -1.7543336153030396, -1.7633730373778285, 1.5797981023788452, 2.880809783935547],
#         [-0.013442818318502248, -1.2449665826610108, -1.8534693717956543, -1.6163512669005335, 1.5796295404434204, 0.054004184901714325]]

path = [[0.6095210313796997, -1.7074171505370082, -1.6451969146728516, -1.3629313272288819, 1.5796432495117188, 2.8807694911956787],
        [0.27833008766174316, -1.1971212488463898, -1.7543336153030396, -1.7633730373778285, 1.5797981023788452, 2.880809783935547]]

def convert_joint_pos(joint_pos):
    pos = joint_pos
    for i in range(len(pos)):
        pos[i] = float(pos[i]) * M_PI / 180
    return pos

def run_experiment():
    print("start")
    print("Which path do you want to run?")
    path_id = int(input())
    print(paths[path_id-1])

    seconds_start = time.time()
    old_version_moveL(paths[path_id-1])
    seconds_end = time.time()

    print("done")
    print("Reverse movement?[y/n]")
    reverse = input()

    if reverse == "y":
        print("start")
        old_version_moveL(paths[path_id-1][::-1])
        print("done")

    print("Time:")
    print(seconds_end - seconds_start)

def run_experiment_custom_starts():
    print("start")
    print("Which path do you want to run? (give joints)")
    
    # START JOINTS
    start = []
    print("Start joints:")
    for i in range(6):
        start.append(float(input()))
    start = convert_joint_pos(start)

    if len(start) != 6:
        print("ERROR: Wrong number of joints")
        return
    
    waypoints = [start]
    for i in range(len(path)):
        pos = path[i]
        pos[5] = start[5]
        waypoints.append(pos)

    # END JOINTS
    end  = [-14, -112, -107, -50, 89, -3]
    end = convert_joint_pos(end)
    waypoints.append(end)

    seconds_start = time.time()
    old_version_moveL(waypoints)
    seconds_end = time.time()

    print("done")
    print("Reverse movement?[y/n]")
    reverse = input()

    if reverse == "y":
        print("start")
        old_version_moveL(waypoints[::-1])
        print("done")

    print("Time:")
    print(seconds_end - seconds_start)

def run():
    print("Do you want to enter your own start joint positions?[y/n]")

    if input() == "y":
        run_experiment_custom_starts()
    else:
        run_experiment()

run()