#!/usr/bin/env python

## Simple program that listens to std_msgs/Strings published 
## to the 'paramdump' topic.  Upon receiving one that says "dump waypoints", it executes 
## the rosparam command to dump the waypoint parameters. This allows them to be persistent.

import rospy
import subprocess
from std_msgs.msg import String
from os.path import expanduser


def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + ' I heard %s', data.data)

    if data.data == "dump waypoints":
        home = expanduser("~")
        subprocess.call(["rosparam", "dump", home + "/waypoints.yaml", "/waypoint"])
	# parameter -v after "dump" will give verbose output

def paramdump():

    # rospy.loginfo(rospy.get_caller_id() + 'paramdump is running')

    rospy.init_node('paramdump')

    rospy.Subscriber('paramdump', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    paramdump()

