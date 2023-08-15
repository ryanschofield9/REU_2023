import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from example_interfaces.msg import Int64

# import random

class tof1_position_real(Node):

    def __init__(self):
        super().__init__('tof1_position')
        #self.publisher_ = self.create_publisher(Int64, 'tof1_pos_real', 10)
        self.subscriber_ = self.create_subscription(Int64, 'tof1_pos', self.callback_data, 10)
        self.subscriptions 

    def callback_data(self, msg):
        #holder = msg.data
        #rand_num = rand.uniform(holder-5, holder+5)
        #new_msg=Int64()
        #new_msg.data = rand_num
        self.get_logger().info('I heard: "%d"' %msg.data)
                                #+ ', Published: ' + str(rand_num))
        #self.publisher_.publish(new_msg)


def main(args=None):
    rclpy.init(args=args)

    tof1_pos_real = tof1_position_real()

    rclpy.spin(tof1_pos_real)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
