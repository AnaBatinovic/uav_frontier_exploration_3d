#!/usr/bin/env python3
import rospy
import tf2_ros
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped

class OdomToTF:
    def __init__(self):
        rospy.init_node('odom_to_tf')

        odom_topic = rospy.get_param('~odom_topic', '/minithex/odometry')

        self.br = tf2_ros.TransformBroadcaster()

        rospy.Subscriber(odom_topic, Odometry, self.odom_callback)

    def odom_callback(self, msg):
        t = TransformStamped()

        t.header.stamp = msg.header.stamp
        t.header.frame_id = msg.header.frame_id
        t.child_frame_id = msg.child_frame_id 

        t.transform.translation.x = msg.pose.pose.position.x
        t.transform.translation.y = msg.pose.pose.position.y
        t.transform.translation.z = msg.pose.pose.position.z

        t.transform.rotation = msg.pose.pose.orientation

        self.br.sendTransform(t)

if __name__ == '__main__':
    try:
        OdomToTF()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
