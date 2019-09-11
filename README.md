# Robot Farm
The robot simulator V-REP is easy and convenient. 
This repository is built for anyone who is interested in robot simulation.

# 机器人农场
 目标是让机器人找到红色物体并报告它们的位置，识别蓝色物体并将它们收集到绿色区域。

![image](https://github.com/WoDingshengli/Robot-Farm/blob/master/Farmpicture.png)

关于进展请见MyWorkProgress.md

## Task and Mark distribution:
An increasing number of would-be farmers are deciding to opt for life in cities. This is leaving a shortage of appropriately trained farmers to support the agriculture industry. To deal with this problem farmers are looking to robotics to undertake tasks such as crop monitoring and harvesting. 
You need to develop a robot able to remain within the boundaries of the farm while being able to locate, identify and respond to types of specified hazards that might occur on the farm. When identified, the first type of hazard must be reported back to the farmer so that workers can be sent out to resolve the problem. The second type of hazard, once detected, needs to be collected by the robot autonomously and taken back to a central location for further processing. Other specifications and restrictions required for this task can be found on the following pages.

This assignment is split into several aspects, everyone must design their own system and discuss the justification of their design and why they made the decisions they did. The main areas for consideration are:

## Robots:
You can pick any type of robot from the V-REP library or build your own. You design and work must be unique to you, collaboration with peers is not allowed. Justify any decisions that you make with regards to the type of robot used, the positioning of the sensors, the weighting of sensors, etc. Once you can get the system working with one robot, you can try increasing the number of robots. 

## Farm Area
The playing area will be black, with a white boundary line around the edge of the farm;
There will be a grid representing paddocks on the farm where the objects will be located;
Each paddock will be represented by a white square. There will be a distance adjacent  between the paddocks and with three of the farm boundaries (except the right hand boundary);
The drop-off zone is signified by a green square.

![image](https://github.com/WoDingshengli/Robot-Farm/blob/master/Farm.png)

## Proof-of-concept Competition
The robot must start in the drop-off zone and the entirety of the robot must be in this zone;
The two different types of hazards will be represented by red and blue. The cubes will be on display from the beginning of the simulation and their positions will be randomised.
There will be multiple types of each hazard/object scattered around the paddocks;
The robot must identify the red objects/hazards and report their location back to a base station;
The robot must collect the blue objects and place them in the drop off zone. The objects may be placed in the drop off zone one at a time or all at once. You have to design a navigation algorithm that can complete this task in the most efficient way. 
The robot must never leave the farm area. The robot may go onto the boundary line, but no part of the robot should cross the boundary line.
The robot must never cross over a paddock. 
