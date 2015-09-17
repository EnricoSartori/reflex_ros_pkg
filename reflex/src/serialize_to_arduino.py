#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from reflex_msgs.msg import Hand

def callback(hand):
	# hand contiene tutti i dati inviati al topic /reflex_hand dalla mano
	# vogliamo estrarre i dati relativi alle pressioni e pubblicarli tramite topic ad arduino
	# i valori da passati non hanno bisogno di ulteriori calcoli da parte di arduino
    
    pub.publish(values_to_token(phalanx_values(hand)))



def values_to_token(values):
    token = 'B '
    for i in values:
        #token += str(int(i)) 
        token += '{:03}'.format(int(i))
        token += ' '
    token += 'E'
    return token

def phalanx_values(hand):
    result = [0,0,0,0,0,0]
    for i in range(0,3):
        # i-esimo dito
        finger = hand.finger[i].pressure
        result[i*2] = abs(mymin(finger[:5]))
        result[i*2+1] = abs(mymin(finger[5:9]))
    return result

def mymin(list):
    ret = 0
    for i in list:
        if i > 100 or i < -255: 
            return -255
    return min(list)
	
if __name__ == '__main__':
    try:
        rospy.init_node('handListener')
        rospy.Rate(10)
        pub = rospy.Publisher('/hand_to_arduino', String, queue_size=10)
        rospy.Subscriber('/reflex_hand', Hand, callback)
        
        while not rospy.is_shutdown():
            rospy.spin()

    except rospy.ROSInterruptException:
        pass
