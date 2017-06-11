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
        """for i in range(0, len(L)):
            if L[i] == 1:
                l.append(i+1)
        print(l)
        if len(l) != 0:"""
        if L[0] == 1 :
            print ("Launching node 1")
            subscribe_name = "optoforce_1"
            subscribe_name_liste.append(subscribe_name)
            print(subscribe_name + " se lance")
            rospy.Subscriber(subscribe_name, WrenchStamped, callback = lambda data: self.callback_name_1(data, subscribe_name))
            print("A souscrit a " + subscribe_name)
        
        if L[1] == 1 :
            print ("Launching node 2")
            subscribe_name = "optoforce_2"
            subscribe_name_liste.append(subscribe_name)
            print(subscribe_name + " se lance")
            rospy.Subscriber(subscribe_name, WrenchStamped, callback = lambda data: self.callback_name_2(data, subscribe_name))
            print("A souscrit a " + subscribe_name)
        
        if L[2] == 1 :
            print ("Launching node 3")
            subscribe_name = "optoforce_3"
            subscribe_name_liste.append(subscribe_name)
            print(subscribe_name + " se lance")
            rospy.Subscriber(subscribe_name, WrenchStamped, callback = lambda data: self.callback_name_3(data, subscribe_name))
            print("A souscrit a " + subscribe_name)
        
        if L[3] == 1 :
            print ("Launching node 4")
            subscribe_name = "optoforce_4"
            subscribe_name_liste.append(subscribe_name)
            print(subscribe_name + " se lance")
            rospy.Subscriber(subscribe_name, WrenchStamped, callback = lambda data: self.callback_name_4(data, subscribe_name))
            print("A souscrit a " + subscribe_name)
        
        if L[4] == 1 :
            print ("Launching node 5")
            subscribe_name = "optoforce_5"
            subscribe_name_liste.append(subscribe_name)
            print(subscribe_name + " se lance")
            rospy.Subscriber(subscribe_name, WrenchStamped, callback = lambda data: self.callback_name_5(data, subscribe_name))
            print("A souscrit a " + subscribe_name)
        
        if L[5] == 1 :
            print ("Launching node 6")
            subscribe_name = "optoforce_6"
            subscribe_name_liste.append(subscribe_name)
            print(subscribe_name + " se lance")
            rospy.Subscriber(subscribe_name, WrenchStamped, callback = lambda data: self.callback_name_6(data, subscribe_name))
            print("A souscrit a " + subscribe_name)
        
           #for i in range(0,len(l)):"""
                #print ("Launching node " + str(l[i]))
                #subscribe_name = "optoforce_"+str(l[i])
                #subscribe_name_liste.append(subscribe_name)
                #print(subscribe_name + " se lance")
                #rospy.Subscriber(subscribe_name, WrenchStamped, callback = lambda data: self.callback_name(data, subscribe_name))
                #print("A souscrit a " + subscribe_name)"""
    
    def callback_name_1(self, data, subscribe_name):
    
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
    def callback_name_2(self, data, subscribe_name):
    
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
                
    def callback_name_3(self, data, subscribe_name):
    
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
    
    def callback_name_4(self, data, subscribe_name):
    
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
    
    def callback_name_5(self, data, subscribe_name):
    
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
    
    def callback_name_6(self, data, subscribe_name):
    
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
