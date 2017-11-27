#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import sys, select, termios, tty

def getKey():

    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def control_pub():
    pub = rospy.Publisher('control',String,queue_size=10)
    rospy.init_node('control_pub',anonymous=False)

    while not rospy.is_shutdown():
        control_order=getKey()
        pub.publish(control_order)
        rospy.loginfo(control_order)

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    try:
        control_pub()
    except rospy.ROSInterruptException:
        pass
