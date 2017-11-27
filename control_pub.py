#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def control_pub():
    pub = rospy.Publisher('control',String,queue_size=10)
    rospy.init_node('control_pub',anonymous=False)

    while not rospy.is_shutdown():
        control_order=raw_input()
        pub.publish(control_order)
        rospy.loginfo(control_order)
if __name__ == '__main__':
    try:
        control_pub()
    except rospy.ROSInterruptException:
        pass
