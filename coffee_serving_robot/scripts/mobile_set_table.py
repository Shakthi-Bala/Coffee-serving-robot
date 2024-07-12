#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
goal = String()


def home_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    pub = rospy.Publisher("set_table", String, queue_size=10)
    goal.data = 'home'
    pub.publish(goal)

def make_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    pub = rospy.Publisher("set_table", String, queue_size=10)
    goal.data = 'make'
    pub.publish(goal)

def table1_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    pub = rospy.Publisher("set_table", String, queue_size=10)
    goal.data = '1'
    pub.publish(goal)

def table2_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    pub = rospy.Publisher("set_table", String, queue_size=10)
    goal.data = '2'
    pub.publish(goal)

def table3_callback(message):
    #get_caller_id(): Get fully resolved name of local node
    pub = rospy.Publisher("set_table", String, queue_size=10)
    goal.data = '3'
    pub.publish(goal)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('mobile_set_table', anonymous=True)
    
    sub_home = rospy.Subscriber("set_home", Bool, home_callback)
    sub_make = rospy.Subscriber("set_make", Bool, make_callback)
    sub_table1 = rospy.Subscriber("set_table1", Bool, table1_callback)
    sub_table2 = rospy.Subscriber("set_table2", Bool, table2_callback)
    sub_table3 = rospy.Subscriber("set_table3", Bool, table3_callback)
    

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
