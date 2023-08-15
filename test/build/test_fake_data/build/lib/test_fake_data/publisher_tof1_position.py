import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class tof1_position_pub(Node):

    def __init__(self): 
        super().__init__('tof1_position')
        self.publisher_ = self.create_publisher(Int64, 'tof1_pos', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.publish_data)
        self.i = 5

    def publish_data(self):
        msg = Int64()
        msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Published: "%d"' % msg.data)
        self.i += 5


def main(args=None):
    rclpy.init(args=args)

    tof1_pos = tof1_position_pub()

    rclpy.spin(tof1_pos)

    rclpy.shutdown()


if __name__ == '__main__':
    main()