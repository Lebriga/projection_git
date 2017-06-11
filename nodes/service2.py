#!/usr/bin/env python

from projection.srv import *
import rospy
import roslib
roslib.load_manifest('projection')
import math
import tf
import geometry_msgs.msg
import tests_affichages
from geometry_msgs.msg import WrenchStamped


class Manager_node():
        
    def __init__(self):
        rospy.init_node('nodes_manager')
        s = rospy.Service('nodes_manager', service, self.handle_node_manager)
        self.listener_tf = tf.TransformListener()
        print ("Ready to manage nodes!!! :D")
        rospy.spin()
    
    def handle_node_manager(self, req):
        n1 = req.a
        n2 = req.b
        n3 = req.c
        n4 = req.d
        n5 = req.e
        n6 = req.f
        L = [n1, n2, n3, n4, n5, n6]
        l = []
        subscribe_name_liste = []
        for i in range(0, len(L)):
            if L[i] == 1:
                l.append(i+1)
        print(l)
        if len(l) != 0:
            for i in range(0,len(l)):
                print ("Launching node " + str(l[i]))
                subscribe_name = "optoforce_"+str(l[i])
                subscribe_name_liste.append(subscribe_name)
                print(subscribe_name + " se lance")
                rospy.Subscriber(subscribe_name, WrenchStamped, callback = lambda data: self.callback_name(data, subscribe_name))
                print("A souscrit a " + subscribe_name)
    
    def callback_name(self, data, subscribe_name):
    
            last_force = [data.wrench.force.x, data.wrench.force.y, data.wrench.force.z]
            time = data.header.stamp
            try:
                if self.listener_tf.frameExists('/'+subscribe_name):
                    print(subscribe_name+" existe")
                    t = self.listener_tf.getLatestCommonTime("/"+subscribe_name, "/world")
                    (trans,rot) = self.listener_tf.lookupTransform(subscribe_name, '/world', t) #le temps de ce noeud bug ac le ros bag...
                    #print("Position")
                    #x =tests_affichages.fois_dix(trans[0])
                    #print(trans[0],x)
                    print(subscribe_name+" Force")
                    print(last_force)
                    print(subscribe_name+" Position")
                    print(trans)
                    print(subscribe_name+" Time")
                    print(time)
                    
                else:
                    print(subscribe_name + " NotExist")
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                print("Exception")


if __name__ == "__main__":
    Manager_node()
