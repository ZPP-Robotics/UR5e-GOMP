import sys
sys.path.append('../')
from colorama import Fore, Back, Style

from obstacles import TwoBoxSetup
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
    # rtde_c = rtde_control.RTDEControlInterface(robot_ip)

    # Move to starting position
    # print("moving to start position")
    # rtde_c.moveJ(start_pos)
    # print("starting movement")
    # for q_pos in waypoints:
    #     t_start = rtde_c.initPeriod()
    #     rtde_c.servoJ(q_pos, velocity, acceleration, dt, lookahead_time, gain)
    #     rtde_c.waitPeriod(t_start)

    # rtde_c.servoStop()
    # rtde_c.stopScript()
    print("end")

def move_by_waypoints_moveJ(waypoints, start_pos):
    robot_ip = "192.168.1.20"
    velo = 1
    acc = 1
    blend = 0.1

    path = []
    for i in range(0, len(waypoints), 6):
        next_joint_pos = []
        next_joint_pos = waypoints[i:i+6]
        next_joint_pos.append(velo)
        next_joint_pos.append(acc)
        next_joint_pos.append(blend)
        print(next_joint_pos)
        path.append(next_joint_pos)

    # next_joint_pos = waypoints[-6:-1]
    # next_joint_pos.append(velo)
    # next_joint_pos.append(acc)
    # next_joint_pos.append(blend)
    # path.append(next_joint_pos)

    # print(path[::3])

    # print("connecting")
    # ROBOT = rtde_control.RTDEControlInterface(robot_ip)

    # ROBOT.moveJ(start_pos)
    # print("start")
    # ROBOT.moveJ(path[::3])
    # print("done")