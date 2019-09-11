#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" main script """

import math
import vrepInterface

class Agent(object):
    def __init__(self):
        import sys
        if sys.version_info[0] < 3:
            sys.exit("Sorry, Python 3 required")
        self.r = 0.05


    def run(self):
        vrepInterface.connect()
        vrepInterface.setup_devices()

        forwBackVel = 0
        leftRightVel = 0
        rotVel = 0

        while True:
            pos = vrepInterface.get_goal_pose()
            print(pos)

            forwBackVel =  0.06*pos[2]
            leftRightVel = 0.06*pos[1]
            angle = math.atan(pos[1]/pos[2])
            rotVel = 0.1*angle

            v_fl = (-forwBackVel-leftRightVel-0.38655*rotVel)/self.r
            v_rl = (-forwBackVel+leftRightVel-0.38655*rotVel)/self.r
            v_rr = (-forwBackVel-leftRightVel+0.38655*rotVel)/self.r
            v_fr = (-forwBackVel+leftRightVel+0.38655*rotVel)/self.r
            vrepInterface.move_wheels(v_fl, v_rl, v_rr, v_fr)

            continue




if __name__ == '__main__':
    agent = Agent()
    agent.run()
