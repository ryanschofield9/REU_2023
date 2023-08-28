import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from example_interfaces.msg import Int64

from geometry_msgs.msg import TwistStamped, Vector3

class RobCartPublisher(Node):

    def __init__(self): 
        super().__init__('rob_cart_pub')
        self.pub = self.create_publisher(TwistStamped, '/servo_node/delta_twist_cmds', 10)
        self.pub_timer = self.create_timer(1/10, self.publish_twist)

    
    def publish_twist(self):
        my_twist = [0.0, -0.1, 0.0] 

        # linear 

        # positive y makes it go down 
        # negative y makes it go up

        # angular 

        # z would rotate the tool 

        cmd = TwistStamped()
        cmd.header.frame_id = 'tool0'
        cmd.header.stamp = self.get_clock().now().to_msg()
        cmd.twist.linear = Vector3(x=my_twist[0], y=my_twist[1], z=my_twist[2])
        cmd.twist.angular = Vector3(x=0.0, y=0.0, z=-0.0)
        self.get_logger().info(f"Sending: {cmd.twist.linear}")

        self.pub.publish(cmd)
        


def main(args=None):
    rclpy.init(args=args)

    rob_cart = RobCartPublisher()

    rclpy.spin(rob_cart)

    rclpy.shutdown()


if __name__ == '__main__':
    main()