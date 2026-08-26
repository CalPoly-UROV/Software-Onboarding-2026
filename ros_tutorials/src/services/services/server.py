# Assignment: Create a ROS 2 Service That Generates a Random Number
# In this exercise, you will build a simple service-based node that responds
# to requests for a random integer between a minimum and maximum value.
# The goal is to practice the request/response communication pattern used in ROS:
# a client sends a request, the server processes it, and the server returns a
# result to the client.
#
# The exercise introduces the basic ROS 2 service server pattern:
# - create a custom node class that inherits from rclpy.node.Node
# - initialize the node with a unique name, such as "random_number_server"
# - define a custom service type (for example, a request with min and max values,
#   and a response with a generated number)
# - create a service with self.create_service(...)
# - implement a callback that computes the result and returns it
# - run the node with rclpy.spin() so it remains active and handles requests
#
# This file is the server half of the exercise. A matching client node sends a
# request to the service and prints the random value it receives. Together, these
# nodes demonstrate how ROS 2 services provide synchronous request/response
# communication between nodes.

import rclpy
from rclpy.node import Node

# Service design:
#   Request: min_value, max_value
#   Response: random_number
#
# Here, import RandomNumber from the interfaces.srv module
# RandomNumber is the custom Service type.

# ROS 2 boilerplate pattern:
# 1. Import rclpy and the base Node class.
# 2. Create a custom node class that inherits from Node.
# 3. In __init__, call super().__init__("node_name") to register the node.
# 4. Add services, publishers, subscribers, timers, and other ROS interfaces in __init__.
# 5. In main(), initialize rclpy, create the node, then spin it.
#    Finally destroy the node and shutdown ROS.
#
# This pattern is the standard starting point for most ROS 2 Python nodes.


class ServiceServer(Node):
    def __init__(self):
        super().__init__('service_server')

        # TODO: Create a service for the random-number request/response type.
        # TODO: Use a callback method such as self.generate_random_number
        # TODO: Register the service under a topic name like 'generate_random_number'

        # create_service:
        #   Creates a service server that waits for requests and invokes a callback.
        #   Usage: self.create_service(ServiceType, 'service_name', callback)
        #   - ServiceType: the ROS service class you define in an .srv file
        #   - 'service_name': unique name for the service, e.g. 'generate_random_number'
        #   - callback: function that receives request and returns a response
        #   Typical use: handle operations such as calculations, data generation,
        #   or device control requests.
        #
        # self.get_logger():
        #   Returns the node's ROS logger, used for printing status and debug output.
        #   Usage: self.get_logger().info('message')
        #   - info(): log informational messages
        #   - warn(): log warnings
        #   - error(): log errors

    # Create a service callback that generates a random number.
    # The callback should read the request values, generate a value between min and max (inclusive),
    # and return a response containing the generated number.
    def generate_random_number(self, request, response):
        # TODO: Read request.min and request.max
        # TODO: Generate a random integer in the requested range
        # TODO: Set response.random_number to the generated value
        # TODO: Return response
        return response


if __name__ == '__main__':
    rclpy.init()
    node = ServiceServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()