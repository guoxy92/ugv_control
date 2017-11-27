#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("%s", data.data)

def control_sub():
    rospy.init_node('control_sub', anonymous=False)

    rospy.Subscriber("control", String, callback)

    rospy.spin()

if __name__ == '__main__':
    control_sub()