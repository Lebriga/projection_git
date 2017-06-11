#!/usr/bin/env python

import sys
import rospy
from projection.srv import *

def manage_nodes_client(n1,n2, n3, n4, n5, n6):
    rospy.wait_for_service('nodes_manager')
    try:
       manage_nodes = rospy.ServiceProxy('nodes_manager', service)
       manage_nodes(n1,n2, n3, n4, n5, n6)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    print("Execution usage()")
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 7:
        print("ok1")
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])
        n3 = int(sys.argv[3])
        n4 = int(sys.argv[4])
        n5 = int(sys.argv[5])
        n6 = int(sys.argv[6])
        print "Requesting"
        manage_nodes_client(n1,n2, n3, n4, n5, n6)
    else:
        print usage()
        print("stop")
        sys.exit(1)
