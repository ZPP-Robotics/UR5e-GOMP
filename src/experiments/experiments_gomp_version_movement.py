import old_version_start_end as ovs
from experiments_init import experiment_joints, write_to_file
import time


# INITIAL SETUP ---------------------------------------------------------------------
N_DIM = 6
Q_MIN = -6.283185307179586232
Q_MAX = 6.283185307179586232
M_PI = 3.14159265358979323846
INF = 1.00000000000000002e+30

time_step = 0.1
waypoints_count = 40 + 2

position_constraints = ([Q_MIN] * N_DIM, [Q_MAX] * N_DIM)
velocity_constraints = ([-M_PI] * N_DIM, [M_PI] * N_DIM)
acceleration_constraints = ([-M_PI * 800 / 180] * N_DIM, [M_PI * 800 / 180] * N_DIM)

radiuses = [0.03, 0.05, 0.01, 0.05, 0.05, 0.10]
#------------------------------------------------------------------------------------

starts = [ovs.start1, ovs.start2, ovs.start3, ovs.start4, ovs.start5, ovs.start6, 
          ovs.start7, ovs.start8, ovs.start9, ovs.start10, ovs.start11, ovs.start12]
ends = [ovs.end1, ovs.end2, ovs.end3, ovs.end4, ovs.end5, ovs.end6, 
        ovs.end7, ovs.end8, ovs.end9, ovs.end10, ovs.end11, ovs.end12]

def convert_joint_pos(joint_pos):
    pos = joint_pos
    for i in range(len(pos)):
        pos[i] = float(pos[i]) * M_PI / 180
    return pos
    

def run_experiment_default_starts():
    print("start")
    print("Which path do you want to run? (give id)")
    start_id = int(input())
    end_id = start_id
    print("Start:")
    print(starts[start_id-1])
    print("End:")
    print(ends[end_id-1])

    seconds_start = time.time()
    experiment_joints(starts[start_id-1], ends[end_id-1], radiuses,
                  time_step, waypoints_count, position_constraints, 
                  velocity_constraints, acceleration_constraints)
    seconds_end = time.time()

    print("done")
    print("Reverse movement?[y/n]")
    reverse = input()

    if reverse == "y":
        print("start")
        experiment_joints(ends[end_id-1], starts[start_id-1], radiuses,
                  time_step, waypoints_count, position_constraints, 
                  velocity_constraints, acceleration_constraints)
        print("done")

    print("Time:")
    print(seconds_end - seconds_start)
    # write_to_file(seconds_end - seconds_start, start_id, True)

def run_experiment_custom_starts():
    print("start")
    print("Which path do you want to run? (give joints)")
    
    #START JOINTS
    start = []
    print("Start joints:")
    for i in range(6):
        start.append(float(input()))
    start = convert_joint_pos(start)

    if len(start) != 6:
        print("ERROR: Wrong number of joints")
        return
    
    # END JOINTS
    # end = [-0.013544384633199513, -1.244895951156952, -1.8533998727798462, -1.6163064442076625, 1.5796618461608887, -3.5252824465381067]
    end  = [-14, -112, -107, -50, 89, -3]
    end = convert_joint_pos(end)

    seconds_start = time.time()
    experiment_joints(start, end, radiuses,
                  time_step, waypoints_count, position_constraints, 
                  velocity_constraints, acceleration_constraints)
    seconds_end = time.time()

    print("done")
    print("Reverse movement?[y/n]")
    reverse = input()

    if reverse == "y":
        print("start")
        experiment_joints(end, start, radiuses,
                  time_step, waypoints_count, position_constraints, 
                  velocity_constraints, acceleration_constraints)
        print("done")

    print("Time:")
    print(seconds_end - seconds_start)
    # write_to_file(seconds_end - seconds_start, start, True)

def run_experiment_custom_starts_ends():
    print("start")
    print("Which path do you want to run? (give joints)")
    
    #START JOINTS
    start = []
    print("Start joints:")
    for i in range(6):
        start.append(float(input()))
    start = convert_joint_pos(start)

    if len(start) != 6:
        print("ERROR: Wrong number of joints")
        return
    
    # END JOINTS
    end = []
    print("End joints:")
    for i in range(6):
        end.append(float(input()))
    end = convert_joint_pos(end)

    if len(end) != 6:
        print("ERROR: Wrong number of joints")
        return

    seconds_start = time.time()
    experiment_joints(start, end, radiuses,
                  time_step, waypoints_count, position_constraints, 
                  velocity_constraints, acceleration_constraints)
    seconds_end = time.time()

    print("done")
    print("Reverse movement?[y/n]")
    reverse = input()

    if reverse == "y":
        print("start")
        experiment_joints(end, start, radiuses,
                  time_step, waypoints_count, position_constraints, 
                  velocity_constraints, acceleration_constraints)
        print("done")

    print("Time:")
    print(seconds_end - seconds_start)

def run():
    print("Do you want to enter your own start and end joint positions?[y/n]")

    if input() == "y":
        run_experiment_custom_starts()
    else:
        run_experiment_default_starts()

run()