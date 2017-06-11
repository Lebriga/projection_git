#!/usr/bin/env python

from projection.srv import *
import rospy
import sys
#sys.path.insert(0, "home/henry/Documents/Projet_Dep_Info/src/projection/nodes")
#print(sys.path)
#import position_force_test


class objet_service:

    def __init__(self):
       self.liste_topic = []
       rospy.init_node('nodes_manager')
       s = rospy.Service('nodes_manager', service, self.handle_node_manager)
       print "Ready to manage nodes!!! :D"
       rospy.spin()

       
    
    def handle_node_manager(req):
        n1 = req.a
        n2 = req.b
        n3 = req.c
        n4 = req.d
        n5 = req.e
        n6 = req.f
        L = [n1, n2, n3, n4, n5, n6]
        l = []
        for i in range(0, len(L)):
            if L[i] == 1:
                l.append(i+1)
        print(l)
        if len(l) != 0:
            for i in range(0,len(l)):
                print ("Launching node " + str(l[i]))
                self.liste_topic.append(position_force_test.myNode(l[i]))

        
if __name__ == "__main__":
    nodes_manager_server()
