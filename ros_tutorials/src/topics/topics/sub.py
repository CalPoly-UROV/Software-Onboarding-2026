import rclpy
from rclpy.node import Node

class Sub(Node):
    def __init__(self):
        super().__init__('sub')

if __name__ == '__main__':
    rclpy.init()
    node = Sub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()