#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from mavros_msgs.msg import OverrideRCIn
from rclpy.qos import QoSProfile, QoSHistoryPolicy, QoSReliabilityPolicy, QoSDurabilityPolicy

import random

class TutorialPublisher(Node):
    def __init__(self):
        super().__init__("tutorial_publisher")
        qos_profile = QoSProfile(
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10,
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            durability=QoSDurabilityPolicy.VOLATILE
        )
        self.publisher = self.create_publisher(
            OverrideRCIn,
            "/mavros/rc/override",
            10
        )
        self.publisher_timer = self.create_timer(
            1.0, self.run_node
        )
        self.get_logger().info("starting publisher node")

    def run_node(self):
        msg = OverrideRCIn()
        msg.channels[0] = 1500
        msg.channels[1] = 1500
        msg.channels[2] = 1500
        msg.channels[3] = 1500
        msg.channels[4] = 2000
        msg.channels[5] = 1500
        msg.channels[6] = 1500
        msg.channels[7] = 1500
        self.publisher.publish(msg)
        for i in range(8, 18):
            msg.channels[i] = 0

def main(args=None):
    rclpy.init(args=args)
    node = TutorialPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received, shutting down...")
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__=="__main__":
    main()