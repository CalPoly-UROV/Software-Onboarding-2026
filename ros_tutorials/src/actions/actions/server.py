# Assignment: Create a ROS 2 Action That Sleeps for a Given Amount of Time
# In this exercise, you will build a simple action-based node that receives a
# goal specifying how long to sleep. The server then sleeps for that duration,
# provides feedback while it is running, and returns a result when finished.
#
# The goal is to practice the action communication pattern used in ROS:
# a client sends a goal, the server processes it asynchronously, and the server
# periodically reports progress before returning the final result.
#
# The exercise introduces the basic ROS 2 action server pattern:
# - create a custom node class that inherits from rclpy.node.Node
# - initialize the node with a unique name, such as "sleep_action_server"
# - define a custom action type with goal, result, and feedback fields
# - create an action server with self.create_server(...)
# - implement a callback that sleeps for the requested duration and returns a result
# - publish feedback during execution and process the action until completion
#
# This file is the server half of the exercise. A matching client node sends a
# goal with a sleep duration and waits for the action to finish. Together, these
# nodes demonstrate how ROS 2 actions provide long-running request/response flow
# with progress updates.

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


class ActionServer(Node):
    def __init__(self):
        super().__init__('action_server')

        # TODO: Create an action server for the SleepFor action type.
        # TODO: Use an execute_callback that handles the goal.
        # TODO: Publish feedback while sleeping.

        # create_server:
        #   Creates an action server that receives goals and manages execution.
        #   Usage: self.create_server(ActionType, 'action_name', execute_callback)
        #   - ActionType: the ROS action class you define in an .action file
        #   - 'action_name': unique name for the action, e.g. 'sleep_for'
        #   - execute_callback: function that handles the action goal
        #   Typical use: long-running tasks such as moving a robot, waiting, or processing work.
        #
        # self.get_logger():
        #   Returns the node's ROS logger, used for logging status updates.
        #   Usage: self.get_logger().info('message')

    # Create an action callback that sleeps for the requested duration.
    # The callback should read the goal, send feedback periodically, and return a result.
    def execute_callback(self, goal_handle):
        # TODO: Read goal_handle.request.seconds
        # TODO: Sleep for the requested duration
        # TODO: Send feedback with remaining time
        # TODO: Set the result and return it
        return None


if __name__ == '__main__':
    rclpy.init()
    node = ActionServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()