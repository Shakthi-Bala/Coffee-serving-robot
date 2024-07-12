#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import socket



def notification_callback(message):
    ip_address = "100.11.10.112" 
    port = 1990
    number = message.data

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    number_bytes = str(number).encode()

    udp_socket.sendto(number_bytes, (ip_address, port))

    udp_socket.close()
    #get_caller_id(): Get fully resolved name of local node
    rospy.loginfo(rospy.get_caller_id() + "Received notification command %s", message.data)
    
def notification_caller():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('sub_display', anonymous=True)

    rospy.Subscriber("notification_command", String, notification_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    notification_caller()
