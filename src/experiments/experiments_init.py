import sys
sys.path.append('../')

from obstacles import Obstacle, BoxParallelXYZ, HorizontalLine , TwoBoxSetup
import rtde_control

def create_two_bin_lab_world():
    # box1 = BoxParallelXYZ((271.07, 507.62, 212.65), 51, 51, 25)
    # box2 = BoxParallelXYZ((271.07, 0.94, 212.65), 51, 51, 25)

    # return [box1, box2]
    setup = TwoBoxSetup((271.07, 507.62, 212.65), 51, 51, 25,
                        (271.07, 0.94, 212.65), 51, 51, 25)
    return [setup]



def move_by_waypoints(start_pos, 
                      waypoints,
                      velocity = 0.5,
                      acceleration = 0.5,
                      dt = 1.0/500,
                      lookahead_time = 0.1,
                      gain = 300):
    
    rtde_c = rtde_control.RTDEControlInterface("10.0.0.219")

    # Move to starting position
    rtde_c.moveJ(start_pos)
    for q_pos in waypoints:
        # t_start = rtde_c.initPeriod()
        rtde_c.servoJ(q_pos, velocity, acceleration, dt, lookahead_time, gain)
        # rtde_c.waitPeriod(t_start)

    # rtde_c.servoStop()
    # rtde_c.stopScript()