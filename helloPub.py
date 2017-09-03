#!/usr/bin/python

import rospy
import time
from std_msgs.msg import String

def test():

	pub = rospy.Publisher("chatter", String, queue_size=0)
	rospy.init_node('helloPub', anonymous=True)
	rate = rospy.Rate(2)
	while not rospy.is_shutdown():
		pub.publish("Hello World")
		print("Hello World")
		time.sleep(1)
#	rospy.spin();

if __name__ == '__main__':
	try:
		test()
	except rospy.ROSInterruptException:
		pass
