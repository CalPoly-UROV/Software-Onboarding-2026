import rclpy
from rclpy.node import Node

class Pub(Node):
    def __init__(self):
        super().__init__('pub')

if __name__ == '__main__':
    rclpy.init()
    node = Pub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()