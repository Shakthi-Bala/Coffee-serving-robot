#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
from std_msgs.msg import String
from rto_msgs.msg import DigitalReadings

button_pressed = False

def button_callback(data):
    global button_pressed
    button = data.values[4]
    if button:
     rospy.loginfo("Button Pressed")
     button_pressed = True

#this method will make the robot move to the goal location
def move_to_goal(xGoal,yGoal,ox,oy,oz,ow):
   global button_pressed

   #define a client for to send goal requests to the move_base server through a SimpleActionClient
   ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

   #wait for the action server to come up
   while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
           rospy.loginfo("Waiting for the move_base action server to come up")

   goal = MoveBaseGoal()
   
   
   #set up the frame parameters
   goal.target_pose.header.frame_id = "map"
   goal.target_pose.header.stamp = rospy.Time.now()

   # moving towards the goal*/

   goal.target_pose.pose.position =  Point(xGoal,yGoal,0)
   goal.target_pose.pose.orientation.x = 0
   goal.target_pose.pose.orientation.y = 0
   goal.target_pose.pose.orientation.z = 0
   goal.target_pose.pose.orientation.w = 1

   rospy.loginfo("Sending goal location ...")
   ac.send_goal(goal)

   ac.wait_for_result(rospy.Duration(60))

   if(ac.get_state() ==  GoalStatus.SUCCEEDED):
           rospy.loginfo("You have reached the destination")
           return True

   else:
           rospy.loginfo("The robot failed to reach the destination")
           return False

def navigate(destination):
     notification_flag = False
     notification_pub = rospy.Publisher('notification_command', String, queue_size=10)
     global button_pressed
     if destination.data:
          goal = destination.data
          
     if goal == "home":
          move_to_goal(home[0],home[1],home[3],home[4],home[5],home[6])

     elif goal == "make":
          move_to_goal(make[0],make[1],make[3],make[4],make[5],make[6])

     elif goal == "1":
          move_to_goal(make[0],make[1],make[3],make[4],make[5],make[6])
          notification_pub.publish('2')
          print("Navigating to Make Space...")
          while not rospy.is_shutdown() and not button_pressed:
               if not notification_flag:
                    notification_pub.publish('3')
                    notification_flag = True
               rospy.loginfo("Waiting for Button Press")
               rospy.sleep(10)  # Print "Waiting for Button Press" every 1 second
          button_pressed = False
          notification_flag = False
          move_to_goal(table1[0],table1[1],table1[3],table1[4],table1[5],table1[6])
          notification_pub.publish('4')
          print("Navigating to Table 1...")
          while not rospy.is_shutdown() and not button_pressed:
               if not notification_flag:
                    notification_pub.publish('5')
                    notification_flag = True
               rospy.loginfo("Waiting for Button Press")
               rospy.sleep(10)  # Print "Waiting for Button Press" every 1 second
          button_pressed = False
          notification_flag = False
          move_to_goal(home[0],home[1],home[3],home[4],home[5],home[6])
          print("Navigating to Home...")
          notification_pub.publish('6')


     elif goal == "2":
          move_to_goal(make[0],make[1],make[3],make[4],make[5],make[6])
          notification_pub.publish('2')
          print("Navigating to Make Space...")
          while not rospy.is_shutdown() and not button_pressed:
               if not notification_flag:
                    notification_pub.publish('3')
                    notification_flag = True
               rospy.loginfo("Waiting for Button Press")
               rospy.sleep(10)  # Print "Waiting for Button Press" every 1 second
          button_pressed = False
          notification_flag = False
          move_to_goal(table2[0],table2[1],table2[3],table2[4],table2[5],table2[6])
          notification_pub.publish('4')
          print("Navigating to Table 2...")
          while not rospy.is_shutdown() and not button_pressed:
               if not notification_flag:
                    notification_pub.publish('5')
                    notification_flag = True
               rospy.loginfo("Waiting for Button Press")
               rospy.sleep(10)  # Print "Waiting for Button Press" every 1 second
          button_pressed = False
          notification_flag = False
          move_to_goal(home[0],home[1],home[3],home[4],home[5],home[6])
          print("Navigating to Home...")
          notification_pub.publish('6')
     
     elif goal == '3':
          move_to_goal(make[0],make[1],make[3],make[4],make[5],make[6])
          notification_pub.publish('2')
          print("Navigating to Make Space...")
          while not rospy.is_shutdown() and not button_pressed:
               if not notification_flag:
                    notification_pub.publish('3')
                    notification_flag = True
               rospy.loginfo("Waiting for Button Press")
               rospy.sleep(10)  # Print "Waiting for Button Press" every 1 second
          button_pressed = False
          notification_flag = False
          move_to_goal(table3[0],table3[1],table3[3],table3[4],table3[5],table3[6])
          notification_pub.publish('4')
          print("Navigating to Table 3...")
          while not rospy.is_shutdown() and not button_pressed:
               if not notification_flag:
                    notification_pub.publish('5')
                    notification_flag = True
               rospy.loginfo("Waiting for Button Press")
               rospy.sleep(10)  # Print "Waiting for Button Press" every 1 second
          button_pressed = False
          notification_flag = False
          move_to_goal(home[0],home[1],home[3],home[4],home[5],home[6])
          print("Navigating to Home...")
          notification_pub.publish('6')


     else:
          print("Waiting for goal")

if __name__ == '__main__':
   rospy.init_node('goal_serve', anonymous=False)
   sub = rospy.Subscriber("destination", String, navigate)
   sub_button = rospy.Subscriber('digital_readings', DigitalReadings, button_callback)
   home = rospy.get_param("home_location", [1.0860443542729903, -1.3517242715112059, 0.0, 0.0, 0.0, -0.4185880906854077, 0.9081762000494975])
   make = rospy.get_param("make_location", [1.0860443542729903, -1.3517242715112059, 0.0, 0.0, 0.0, -0.4185880906854077, 0.9081762000494975])
   table1 = rospy.get_param("table1_location", [-1.0725319526371795,-0.06612544718045643,0.0,0.0,0.0,0.9736069433042448,0.22823128608883797])
   table2 = rospy.get_param("table2_location", [-0.6379369076711914,1.6220685166101694,0.0,0.0,0.0,0.6514660740494724,0.758677767146611])
   table3 = rospy.get_param("table3_location", [1.1158281279510207,1.0453224100637535,0.0,0.0,0.0,0.4756874458332325,0.8796143779387963])

   #home = [1.0860443542729903, -1.3517242715112059, 0.0, 0.0, 0.0, -0.4185880906854077, 0.9081762000494975]
   #table1 = [-1.0725319526371795,-0.06612544718045643,0.0,0.0,0.0,0.9736069433042448,0.22823128608883797]
   #table2 = [-0.6379369076711914,1.6220685166101694,0.0,0.0,0.0,0.6514660740494724,0.758677767146611]
   #table3 = [1.1158281279510207,1.0453224100637535,0.0,0.0,0.0,0.4756874458332325,0.8796143779387963]

   rospy.spin()
