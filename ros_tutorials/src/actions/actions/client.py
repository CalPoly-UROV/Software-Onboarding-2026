# Assignment: Create a ROS 2 Action That Sleeps for a Given Amount of Time
# In this exercise, you will build a client node that sends a goal to the sleep
# action server. The client requests a duration to wait, then receives periodic
# feedback while the server is sleeping and a final result once the task is done.
#
# The exercise introduces the basic ROS 2 action client pattern:
# - create a custom node class that inherits from rclpy.node.Node
# - initialize the node with a unique name, such as "sleep_action_client"
# - create an action client with self.create_client(...)
# - send a goal containing the requested duration
# - wait for feedback and the final result
# - log the result and status updates
#
# This file is the client half of the exercise. It sends a goal to the action
# server and processes the returned feedback/result. Together, these two nodes
# demonstrate how ROS 2 actions support long-running tasks with progress updates.

import rclpy
from rclpy.node import Node

# Example action design:
#   Goal: duration (seconds)
#   Result: success (bool)
#   Feedback: remaining (duration)
# Replace this with the action type you define in your custom interface package,
# for example: from my_interfaces.action import SleepFor

# ROS 2 boilerplate pattern:
# 1. Import rclpy and the base Node class.
# 2. Create a custom node class that inherits from Node.
# 3. In __init__, call super().__init__("node_name") to register the node.
# 4. Add action servers, publishers, subscribers, timers, and other ROS interfaces in __init__.
# 5. In main(), initialize rclpy, create the node, then spin it.
#    Finally destroy the node and shutdown ROS.
#
# This pattern is the standard starting point for most ROS 2 Python nodes.


class ActionClient(Node):
    def __init__(self):
        super().__init__('action_client')

        # TODO: Create an action client for the SleepFor action type.
        # TODO: Wait until the action server is available.
        # TODO: Construct a goal with a duration value.

        # create_client:
        #   Creates an action client used to send goals to a ROS action server.
        #   Usage: self.create_client(ActionType, 'action_name')
        #   - ActionType: the ROS action class you defined in an .action file
        #   - 'action_name': name of the action server to call
        #   Typical use: request a long-running task such as movement or timed work.
        #
        # self.get_logger():
        #   Returns the node's ROS logger, used to print progress and results.

    # Create a method that sends the action goal.
    def send_goal(self):
        # TODO: Build a goal request with a sleep duration.
        # TODO: Send the goal to the action server.
        # TODO: Handle feedback and wait for the final result.
        pass


if __name__ == '__main__':
    rclpy.init()
    node = ActionClient()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()