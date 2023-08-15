import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from example_interfaces.msg import Int64

class tof1_position_sub(Node):

    branch_low = 200
    branch_high = 250

    def __init__(self):
        super().__init__('tof1_position')
        self.subscriber_ = self.create_subscription(String, 'tof1_real_pos', self.callback_data, 10)
        self.subscriptions 

    def callback_data(self, msg):
        self.get_logger().info('I heard: "%s' %msg.data)


def main(args=None):
    rclpy.init(args=args)

    tof1_pos_sub = tof1_position_sub()

    rclpy.spin(tof1_pos_sub)

    rclpy.shutdown()


if __name__ == '__main__':
    main()