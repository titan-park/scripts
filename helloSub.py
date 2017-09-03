#!/usr/bin/python

import rospy
import time
from std_msgs.msg import String

def callback(data):
	print(data.data)

def test():

	rospy.init_node('helloSub', anonymous=True)
	rospy.Subscriber("chatter", String, callback)

	rate = rospy.Rate(2)

	rospy.spin();

if __name__ == '__main__':
	try:
		test()
	except rospy.ROSInterruptException:
		pass
