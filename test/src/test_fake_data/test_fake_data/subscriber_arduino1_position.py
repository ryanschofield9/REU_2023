import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from example_interfaces.msg import Int64, String

class arduino1_sub(Node):

    def __init__(self):
        super().__init__('arduino1')
        self.subscriber_ = self.create_subscription(String, 'arduino1', self.callback_data, 10)
        self.subscriptions 

    def callback_data(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        print("HERE")
        self.get_logger().info('I heard: "%s"' %msg.data)

def main(args=None):
    rclpy.init(args=args)

    sub = arduino1_sub()
    print("here")
    rclpy.spin(sub)
    print("here")
    rclpy.shutdown()
    


if __name__ == '__main__':
    main()