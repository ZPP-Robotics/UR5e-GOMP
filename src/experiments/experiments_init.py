from obstacles import Obstacle, BoxParallelXYZ, HorizontalLine
import rtde_control

def create_two_bin_lab_world():
    box1 = BoxParallelXYZ((271.07, 507.62, 212.65), 51, 51, 25)
    box2 = BoxParallelXYZ((271.07, 0.94, 212.65), 51, 51, 25)

    return [box1, box2]

def move_by_waypoints(start_pos, 
                      waypoints,
                      velocity = 0.5,
                      acceleration = 0.5,
                      dt = 1.0/500,
                      lookahead_time = 0.1,
                      gain = 300):
    
    rtde_c = rtde_control.RTDEControlInterface("127.0.0.1")

    # Move to starting position
    rtde_c.moveJ(start_pos)
    for q_pos in waypoints:
        rtde_c.servoJ(q_pos, velocity, acceleration, dt, lookahead_time, gain)

    rtde_c.servoStop()
    rtde_c.stopScript()