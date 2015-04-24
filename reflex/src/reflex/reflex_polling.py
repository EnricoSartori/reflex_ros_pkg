#!/usr/bin/env python

import rospy
from reflex_msgs.msg import HandCommand
from time import sleep

from reflex_base_services import *

class ReFlex_Polling(ReFlex):

    def __init__(self):
        super(ReFlex_Polling, self).__init__()
        

        def callback(data):
    	    # data is a HandCommand variable
            for i in range(0, len(data.angles)):
                self.move_finger(i, data.angles[i])
        
        rospy.Subscriber("reflex_commander", HandCommand, callback)
        # spin: this function generate the polling
        rospy.spin()

if __name__ == '__main__':
	rospy.init_node('ReflexPollingNode')
	reflex_hand = ReFlex_Polling()
