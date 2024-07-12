#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Received message: %s", data.data)
    rospy.loginfo("Saying bye...")
    rospy.signal_shutdown("Received message, shutting down")

def subscriber_node():
    rospy.init_node('subscriber_node', anonymous=True)
    rospy.Subscriber('your_topic_name', String, callback)
    
    rospy.loginfo("Subscriber node is running and saying hi...")

    while not rospy.is_shutdown():
        rospy.loginfo("hi")
        rospy.sleep(1)  # Print "hi" every 1 second

    rospy.loginfo("Subscriber node is shutting down.")

if __name__ == '__main__':
    try:
        subscriber_node()
    except rospy.ROSInterruptException:
        pass
