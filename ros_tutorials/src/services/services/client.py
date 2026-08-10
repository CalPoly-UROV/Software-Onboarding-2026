import rclpy
from rclpy.node import Node

class ServiceClient(Node):
    def __init__(self):
        super().__init__('service_client')

if __name__ == '__main__':
    rclpy.init()
    node = ServiceClient()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()