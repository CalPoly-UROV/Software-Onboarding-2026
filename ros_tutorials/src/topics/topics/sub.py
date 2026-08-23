# Assignment: Write a Simple ROS 2 Publisher and Subscriber
# In this tutorial, you will create a minimal ROS 2 node that subscribes to
# a topic named "topic" and receives messages published by a matching node.
# The goal is to practice the core pub/sub communication pattern used in ROS:
# a publisher sends data, a subscriber receives it, and both nodes are part
# of the same ROS graph.
#
# The exercise introduces the basic ROS 2 Python structure:
# - create a custom node class that inherits from rclpy.node.Node
# - initialize the node with a unique name, such as "sub"
# - create a subscription for a message type like std_msgs.msg.String
# - define a callback function that runs whenever a new message arrives
# - run the node with rclpy.spin() so it stays alive and processes callbacks
#
# This file is the subscriber half of the exercise. It listens for messages
# on the same topic as the publisher and prints the received data. Together,
# these two nodes demonstrate how ROS 2 topics allow asynchronous message
# exchange between independent processes.

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# ROS 2 boilerplate pattern:
# 1. Import rclpy and the base Node class.
# 2. Create a custom node class that inherits from Node.
# 3. In __init__, call super().__init__("node_name") to register the node.
# 4. Add publishers, subscribers, timers, and other ROS interfaces in __init__.
# 5. In main(), initialize rclpy, create the node, then spin it.
#    Finally destroy the node and shutdown ROS.
#
# This pattern is the standard starting point for most ROS 2 Python nodes.


class Sub(Node):
    def __init__(self):
        super().__init__('sub')

        # TODO: Create a subscription to String messages on the "topic" topic
        # TODO: Use self.listener_callback as the callback function
        # TODO: Set the queue size to 10

        # create_subscription:
        #   Creates a subscriber that listens on a topic and calls a callback when
        #   a message is received.
        #   Usage: self.create_subscription(MessageType, 'topic_name', callback, qos)
        #   - MessageType: the ROS message class, e.g. String
        #   - 'topic_name': name of the ROS topic to subscribe to
        #   - callback: function that handles incoming messages
        #   - qos: quality of service depth for the subscription queue
        #   Typical use: receive sensor updates, commands, or status messages.

    # Create a callback function that prints the received message.
    # The callback should accept a String message and log the data.
    def listener_callback(self, msg):
        # TODO: Log the incoming message data

        # self.get_logger():
        #   Returns the node's ROS logger, which is used for logging messages to
        #   the terminal and ROS logs.
        #   Usage: self.get_logger().info('message')
        #   - info(): logs informational output
        #   - warn(): logs warnings
        #   - error(): logs errors
        #   - debug(): logs debug-level messages when enabled
        #   Typical use: print received topic data and node status messages.
        
        pass


if __name__ == '__main__':
    rclpy.init()
    node = Sub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()