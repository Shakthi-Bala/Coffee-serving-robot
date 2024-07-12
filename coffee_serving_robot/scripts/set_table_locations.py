#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from std_msgs.msg import String
import yaml
import os
from rospkg import RosPack

class PoseStorageNode:
    def __init__(self):
        rospy.init_node('pose_storage_node')
        
        # Initialize a dictionary to store pose data for multiple tables
        self.table_data = {}
        
        # Subscribe to /amcl_pose topic
        self.pose_sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.pose_callback)
        
        # Subscribe to /set_table topic
        self.set_table_sub = rospy.Subscriber('/set_table', String, self.set_table_callback)

    def pose_callback(self, data):
        # Update position and orientation data
        self.location = [data.pose.pose.position.x, data.pose.pose.position.y, data.pose.pose.position.z, data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w]
        #self.orientation = [data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w]

    def set_table_callback(self, data):
        table_number = data.data
        
        if table_number == 'home':
            table_location = 'home_location'
        elif table_number == 'make':
            table_location = 'make_location'
        else:
            table_location = "table"+table_number+"_location"
        # Ensure there's a dictionary entry for the table
        if table_number not in self.table_data:
            self.table_data[table_number] = {
                table_location: []
            }
        
        # Update the position and orientation data for the specified table
        self.table_data[table_number][table_location] = self.location
        print("Location set for", table_location)
        
        
        # Store the combined data in a YAML file
        self.save_to_yaml(f'table_locations.yaml', self.table_data[table_number])
        print(self.table_data[table_number])

    def save_to_yaml(self, filename, data):
        # Get the path to the package using RosPack
        rospack = RosPack()
        package_path = rospack.get_path("coffee_serving_robot")  # Replace "coffee_serving_robot" with your ROS package name

        # Construct the full file path with the package path and the "config" folder
        full_file_path = os.path.join(package_path, "config", filename)

        # Check if the file already exists
        if os.path.isfile(full_file_path):
            # If the file exists, read the existing data from it
            with open(full_file_path, 'r') as file:
                existing_data = yaml.safe_load(file)
        else:
            # If the file doesn't exist, create an empty dictionary
            existing_data = {}

        # Merge the existing data with the new data
        existing_data.update(data)

        # Write the combined data back to the file
        with open(full_file_path, 'w') as file:
            yaml.dump(existing_data, file, default_flow_style=False)
            rospy.loginfo(f'Saved data to {full_file_path}')

if __name__ == '__main__':
    try:
        node = PoseStorageNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
