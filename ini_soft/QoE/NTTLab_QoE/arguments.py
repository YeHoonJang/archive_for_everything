#!/usr/bin/python
# Last updated: May 29 2018
import sys

######### arguments #########
def arguments(argvs, argc, jsonPath):

    for p in range(0, argc):
        if(argvs[p]) == "-h":
            print '-h: help'
            print '\t qoe.py -c (json path)'
            sys.exit()
        elif(argvs[p]) == "-c":
            jsonPath = argvs[p + 1]

    return jsonPath
######### arguments end #########

