#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import keyboard

def keyboard_publisher():
    rospy.init_node('keyboard_publisher', anonymous=True)
    pub = rospy.Publisher('destination', String, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    key_mapping = {
        '0': 'home',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': 'make'
    }

    while not rospy.is_shutdown():
        key = input("Press a numpad key (0-9) and press Enter: ")

        if key in key_mapping:
            goal = key_mapping[key]
            rospy.loginfo(f'Pressed {key}')
            pub.publish(goal)

if __name__ == '__main__':
    try:
        keyboard_publisher()
    except rospy.ROSInterruptException:
        pass
