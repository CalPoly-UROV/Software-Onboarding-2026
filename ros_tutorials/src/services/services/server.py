import rclpy
from rclpy.node import Node

class ServiceServer(Node):
    def __init__(self):
        super().__init__('service_server')

if __name__ == '__main__':
    rclpy.init()
    node = ServiceServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()