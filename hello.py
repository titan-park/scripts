#!/usr/bin/python

import rospy
import time

def test():

	rospy.init_node('test', anonymous=False)
	rate = rospy.Rate(2)
	while not rospy.is_shutdown():

		print("Hello World")
		time.sleep(1)
#	rospy.spin();

if __name__ == '__main__':
	try:
		test()
	except rospy.ROSInterruptException:
		pass
