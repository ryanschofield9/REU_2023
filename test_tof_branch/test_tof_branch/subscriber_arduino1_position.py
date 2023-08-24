import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32, String


class arduino1_sub(Node):

    def __init__(self):
        super().__init__(node_name = 'tof_sub')
        self.subscriber_ = self.create_subscription(String, 'arduino1', self.callback_data, 10)
        self.subscriptions 

    def callback_data(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        self.get_logger().info('I heard: "%s"' %msg.data)

def main(args=None):
    rclpy.init(args=args)

    sub = arduino1_sub()

    rclpy.spin(sub)
   
    rclpy.shutdown()
    


if __name__ == '__main__':
    main()