#!/user/bin/env python
# -*- coding:utf-8 -*-
# Author:   5-Fishes
# Created on:
###### Sun Oct 10 17:23:05 PDT 2021           
# Last modify on:
###### Sun Oct 10 17:23:22 PDT 2021
# Purpose:
# This is an entrance of the simulator of MDP for Course 209AS
# It will read a config file from current floder to load following data to initials an system
# S -- State Space
# A -- Action Space
# R -- Reward
# P -- Transition Probability
# O -- Observation (No sure the propuse of this function, HARDCODED for now)
# gamma -- discount factor

import json
from system import System
from robot import Robot

if __name__ == "__main__":
    with open("./generator/A.json", "r") as f:
        A = json.load(f)
    
    with open("./generator/P.json", "r") as f:
        P = json.load(f)

    with open("./generator/S.json", "r") as f:
        S = json.load(f)

    with open("./generator/R.json", "r") as f:
        R = json.load(f)

    # build an initial P
    M = int(input("please input the colum number: "))
    N = int(input("please input the row number: "))
    
    system = System(S, A, R, P, 0.8, N, M)


    robot = Robot(system)
    robot.PI()
    