#!/usr/bin/python

import rospy
import time
from std_msgs.msg import String
from ros_2nd.msg import Num

def callback(data):
	print "Received Data: "
	print data.x, data.y
#	print data
def numSub():

	rospy.init_node('numSub', anonymous=True)
	rospy.Subscriber("chatter", Num, callback)

	rate = rospy.Rate(2)

	rospy.spin();

if __name__ == '__main__':
	try:
		numSub()
	except rospy.ROSInterruptException:
		pass
