import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from example_interfaces.msg import Int64

import random

class tof1_position_real(Node):

    def __init__(self):
        super().__init__('tof1_position')
        self.subscriber_ = self.create_subscription(Int64, 'tof1_pos', self.callback_data, 10)
        self.publisher_ = self.create_publisher(Int64, 'tof1_pos_real', 10)  

    def callback_data(self, msg):
        rand_num = random.randint(0, 10)
        new_msg=Int64()
        new_msg.data = rand_num
        self.get_logger().info('I heard: ' + str(msg.data) +
                                ', Published: ' + str(new_msg.data))
        self.publisher_.publish(new_msg)


def main(args=None):
    rclpy.init(args=args)

    tof1_pos_real = tof1_position_real()

    rclpy.spin(tof1_pos_real)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
