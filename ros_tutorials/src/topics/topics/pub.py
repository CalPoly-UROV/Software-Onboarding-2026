# Assignment: Write a Simple ROS 2 Publisher and Subscriber
# In this tutorial, you will create a minimal ROS 2 node that publishes
# a simple string message to a topic named "topic" at a fixed rate.
# The goal is to practice the core pub/sub communication pattern used in ROS:
# a publisher sends data, a subscriber receives it, and both nodes are part
# of the same ROS graph.
#
# The exercise introduces the basic ROS 2 Python structure:
# - create a custom node class that inherits from rclpy.node.Node
# - initialize the node with a unique name, such as "pub"
# - create a publisher for a message type like std_msgs.msg.String
# - use a timer to periodically publish messages to the topic
# - run the node with rclpy.spin() so it stays alive and processes callbacks
#
# This file is the publisher half of the exercise. A matching subscriber node
# listens to the same topic and prints the incoming message data. Together,
# they demonstrate how ROS 2 nodes communicate asynchronously using topics.

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


class Pub(Node):
    def __init__(self):
        super().__init__('pub')

        # TODO: Create a publisher for String messages on the "topic" topic with a queue size of 10
        # TODO: Create a timer that calls self.timer_callback every 1 second (1.0)

        # create_timer:
        #   Creates a repeating callback based on a time interval.
        #   Usage: self.create_timer(period_sec, callback)
        #   - period_sec: float, time between callback invocations in seconds
        #   - callback: function to run each period
        #   Typical use: publish periodic sensor or status messages.
        #
        # create_publisher:
        #   Creates a publisher for a specific message type and topic.
        #   Usage: self.create_publisher(MessageType, 'topic_name', queue_size)
        #   - MessageType: the ROS message class, e.g. String
        #   - 'topic_name': name of the ROS topic to publish to
        #   - queue_size: outgoing message queue size
        #   Typical use: send data to subscribers on the topic.

    # Create a timer callback that publishes a message every second.
    # The callback should create a String message, set its data to "Message {i}!", 
    # where i is an incremented intenger, and publish it to the topic.
    def timer_callback(self):
        # TODO: Create message object of type String
        # TODO: Set its data attribute to "Message {i}!" where i is an incremented integer
        # TODO: Publish the message using the publisher created in __init__
        pass


if __name__ == '__main__':
    rclpy.init()
    node = Pub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()