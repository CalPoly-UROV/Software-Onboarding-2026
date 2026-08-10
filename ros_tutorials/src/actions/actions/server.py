import rclpy
from rclpy.node import Node

class ActionServer(Node):
    def __init__(self):
        super().__init__('action_server')

if __name__ == '__main__':
    rclpy.init()
    node = ActionServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()