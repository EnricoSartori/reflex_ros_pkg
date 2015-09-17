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
            self.move_finger(0, data.angles[0])
    	    self.move_finger(1, data.angles[1])
            #self.move_finger(2, data.angles[2])
            
        rospy.Subscriber("reflex_commander", HandCommand, callback)
        # spin: this function generate the polling
        rospy.spin()

if __name__ == '__main__':
	rospy.init_node('ReflexPollingNode')
	reflex_hand = ReFlex_Polling()
