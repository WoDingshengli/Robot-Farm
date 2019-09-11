#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" vrep interface script that connects to vrep, reads and sets data to objects through vrep remote API  """

import time
import numpy as np
import vrep
import math

# V-REP data transmission modes:
WAIT = vrep.simx_opmode_oneshot_wait
ONESHOT = vrep.simx_opmode_oneshot
STREAMING = vrep.simx_opmode_streaming
BUFFER = vrep.simx_opmode_buffer
BLOCKING = vrep.simx_opmode_blocking

time_step = 0.005

wait_response = False

if wait_response:
    MODE_INI = WAIT
    MODE = WAIT
else:
    MODE_INI = STREAMING
    MODE = BUFFER

robotID = -1
left_motorID = -1
right_motorID = -1
clientID = -1

def show_msg(message):
    """ send a message for printing in V-REP """
    vrep.simxAddStatusbarMessage(clientID, message, WAIT)
    return


def connect():
    """ Connect to the simulator"""
    ip = '127.0.0.1'
    port = 19999
    vrep.simxFinish(-1)  # just in case, close all opened connections
    global clientID
    clientID = vrep.simxStart(ip, port, True, True, 3000, 5)
    # Connect to V-REP
    if clientID == -1:
        import sys
        sys.exit('\nV-REP remote API server connection failed (' + ip + ':' +
                 str(port) + '). Is V-REP running?')
    print('Connected to Remote API Server')  # show in the terminal
    show_msg('Python: Hello')    # show in the VREP
    time.sleep(0.5)
    return


def disconnect():
    """ Disconnect from the simulator"""
    # Make sure that the last command sent has arrived
    vrep.simxGetPingTime(clientID)
    show_msg('ROBOT: Bye')
    # Now close the connection to V-REP:
    vrep.simxFinish(clientID)
    time.sleep(0.5)
    return


def start():
    """ Start the simulation (force stop and setup)"""
    stop()
    setup_devices()
    vrep.simxStartSimulation(clientID, ONESHOT)
    time.sleep(0.5)
    # Solve a rare bug in the simulator by repeating:
    setup_devices()
    vrep.simxStartSimulation(clientID, ONESHOT)
    time.sleep(0.5)
    return


def stop():
    """ Stop the simulation """
    vrep.simxStopSimulation(clientID, ONESHOT)
    time.sleep(0.5)


def setup_devices():
    """ Assign the devices from the simulator to specific IDs """
    global robotID, motorfl, motorrl,  motorrr, motorfr, goalID
    # res: result (1(OK), -1(error), 0(not called))
    # robot
    res, robotID = vrep.simxGetObjectHandle(clientID, 'youBot', WAIT)
    # motors
    res, motorfl = vrep.simxGetObjectHandle(clientID, 'rollingJoint_fl', WAIT)
    res, motorrl = vrep.simxGetObjectHandle(clientID, 'rollingJoint_rl', WAIT)
    res, motorrr = vrep.simxGetObjectHandle(clientID, 'rollingJoint_rr', WAIT)
    res, motorfr = vrep.simxGetObjectHandle(clientID, 'rollingJoint_fr', WAIT)

    # goal reference object
    res, goalID = vrep.simxGetObjectHandle(clientID, 'Target', WAIT)

    # wheels
    vrep.simxSetJointTargetVelocity(clientID, motorfl, 0, STREAMING)
    vrep.simxSetJointTargetVelocity(clientID, motorrl, 0, STREAMING)
    vrep.simxSetJointTargetVelocity(clientID, motorrr, 0, STREAMING)
    vrep.simxSetJointTargetVelocity(clientID, motorfr, 0, STREAMING)
    # pose
    vrep.simxGetObjectPosition(clientID,goalID, robotID, STREAMING)
    vrep.simxGetObjectOrientation(clientID,goalID, robotID,STREAMING)

    return


def get_goal_pose():
    """ return the pose of the robot:  [ x(m), y(m), Theta(rad) ] """
    global pos
    res, pos = vrep.simxGetObjectPosition(clientID,goalID, robotID, MODE)
    res, ori = vrep.simxGetObjectOrientation(clientID,goalID, robotID, MODE)
    pos = np.array([pos[0], pos[1], pos[2]])
    return pos

"""
def set_robot_pose2d(pose):
    *set the pose of the robot:  [ x(m), y(m), Theta(rad) ] 
    vrep.simxSetObjectPosition(clientID, robotID, goalID, [pose[0], pose[1], 0], MODE)
    vrep.simxSetObjectOrientation(clientID, robotID, goalID, [0, 0, pose[2]], MODE)
"""





def move_wheels(v_fl, v_rl, v_rr, v_fr):
    """ move the wheels. Input: Angular velocities in rad/s """
    vrep.simxSetJointTargetVelocity(clientID, motorfl, v_fl, STREAMING)
    vrep.simxSetJointTargetVelocity(clientID, motorrl, v_rl,STREAMING)
    vrep.simxSetJointTargetVelocity(clientID, motorrr, v_rr, STREAMING)
    vrep.simxSetJointTargetVelocity(clientID, motorfr, v_fr,STREAMING)
    time.sleep(time_step)
    return




def stop_motion():
    """ stop the base wheels """
    vrep.simxSetJointTargetVelocity(clientID, motorfl, 0, STREAMING)
    vrep.simxSetJointTargetVelocity(clientID, motorrl, 0,STREAMING)
    vrep.simxSetJointTargetVelocity(clientID, motorrr, 0, STREAMING)
    vrep.simxSetJointTargetVelocity(clientID, motorfr, 0,STREAMING)
    return




