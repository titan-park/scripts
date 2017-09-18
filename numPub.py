#!/usr/bin/python

import rospy
import time
from std_msgs.msg import String
from ros_2nd.msg import Num

def numPub():
	num = Num()

	pub = rospy.Publisher("chatter", Num, queue_size=10)
	rospy.init_node('numPub', anonymous=True)
	rate = rospy.Rate(2)
	while not rospy.is_shutdown():

		num.x = 1.0
		num.y = 2 
		print num.x, num.y
		pub.publish(num)
		time.sleep(1)

if __name__ == '__main__':
	try:
		numPub()
	except rospy.ROSInterruptException:
		pass
