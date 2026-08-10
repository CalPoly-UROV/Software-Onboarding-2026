import rclpy
from rclpy.node import Node

class ActionClient(Node):
    def __init__(self):
        super().__init__('action_client')

if __name__ == '__main__':
    rclpy.init()
    node = ActionClient()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()