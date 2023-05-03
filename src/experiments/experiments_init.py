import sys
sys.path.append('../')
from colorama import Fore, Back, Style

from obstacles import TwoBoxSetup
from solver import GOMP
import gomp
import rtde_control

def create_two_bin_lab_world():
    setup = TwoBoxSetup((0.27107, 0.50762, 0.21265), 0.51, 0.51, 0.25,
                        (0.27107, 0.094, 0.21265), 0.51, 0.51, 0.25)
    return [setup]

def move_by_waypoints(start_pos, 
                      waypoints,
                      velocity = 0.5,
                      acceleration = 0.5,
                      dt = 1.0/500,
                      lookahead_time = 0.1,
                      gain = 300):
    path = []
    for i in range(0, len(waypoints), 6):
        next_joint_pos = waypoints[i:i+6]
        path.append(next_joint_pos)

    print(Style.BRIGHT + "Waypoints:" + Style.RESET_ALL)
    for el in path:
        print(el)

    print("connecting to robot")
    robot_ip = "192.168.1.20"
    # rtde_c = rtde_control.RTDEControlInterface("10.0.0.219")
    rtde_c = rtde_control.RTDEControlInterface(robot_ip)

    # Move to starting position
    print("moving to start position")
    rtde_c.moveJ(start_pos)
    print("starting movement")
    for q_pos in waypoints:
        t_start = rtde_c.initPeriod()
        rtde_c.servoJ(q_pos, velocity, acceleration, dt, lookahead_time, gain)
        rtde_c.waitPeriod(t_start)

    # rtde_c.servoStop()
    # rtde_c.stopScript()
    print("end")

def move_by_waypoints_moveJ(waypoints, start_pos):
    robot_ip = "192.168.1.20"
    velo = 1
    acc = 1
    blend = 0.001

    path = []
    for i in range(0, len(waypoints), 6):
        next_joint_pos = []
        next_joint_pos = waypoints[i:i+6]
        next_joint_pos.append(velo)
        next_joint_pos.append(acc)
        next_joint_pos.append(blend)
        # print(next_joint_pos)
        path.append(next_joint_pos)

    print(Style.BRIGHT + "Waypoints:" + Style.RESET_ALL)
    for el in path:
        print(el)
    # print(path[::3])

    print("connecting to robot")
    ROBOT = rtde_control.RTDEControlInterface(robot_ip)

    ROBOT.moveJ(start_pos)
    print("start")
    ROBOT.moveJ(path[::3])
    print("done")

def experiment_joints(start_pos, end_pos, radiuses,
               time_step, waypoints_count, position_constraints, velocity_constraints, acceleration_constraints):
    world_obstacles = create_two_bin_lab_world()

    gomp_solver = GOMP(time_step, waypoints_count, position_constraints, velocity_constraints, acceleration_constraints)
    for obstacle in world_obstacles:
        gomp_solver.add_obstacle(obstacle)

    print("Obstacles:")
    gomp_solver.print_obstacles()

    print("Radiuses:")
    # radiuses = [0.05, 0.05, 0.05, 0.05, 0.15]
    gomp_solver.set_radiuses(radiuses)

    print("RUN")
    (code, waypoints) = gomp_solver.run(start_pos, end_pos)
    waypoints = waypoints[:(len(waypoints)//2)]

    if (code == gomp.OsqpExitCode.kOptimal):
        print(Fore.GREEN + Style.BRIGHT + "SUCCESS! - Found solution" + Style.RESET_ALL)
        print(Style.BRIGHT + "Obstacles:" + Style.RESET_ALL)
        gomp_solver.print_obstacles()


        print(Style.BRIGHT + "Waypoint count:" + Style.RESET_ALL)
        print(len(waypoints[:(len(waypoints))])//6)

        # move_by_waypoints(start_pos=start_pos, waypoints=waypoints)
        move_by_waypoints_moveJ(start_pos=start_pos, waypoints=waypoints)
    else:
        print(Fore.RED + Style.BRIGHT + "ERROR!" + Style.RESET_ALL)
        print(Style.BRIGHT + "No solution found" + Style.RESET_ALL)
        print(Style.BRIGHT + "Error code:" + Style.RESET_ALL)
        print(code)
