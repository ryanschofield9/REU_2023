import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Float32

from example_interfaces.msg import Int64

from geometry_msgs.msg import TwistStamped, Vector3

class rob_move_down(Node):

    def __init__(self): 
        super().__init__('move_down')
        self.pub = self.create_publisher(TwistStamped, '/servo_node/delta_twist_cmds', 10)
        self.pub_timer = self.create_timer(1/10, self.publish_twist)
        self.subscriber_ = self.create_subscription(Float32,'arduino1avg',self.avg_callback, 10)
        self.subscriptions 
        self.i = 0
        self.avg = 0.0; 
        self.looking = True 
        self.stop = False

    
    def publish_twist(self):
        my_twist_linear = [0.0, 0.0, 0.0] 
        my_twist_angular = [0.0, 0.0, 0.0]

        # positive y makes it go down 
        #negative y makes it go up
        if (self.looking == True): 
            
            my_twist_linear = [0.0, 0.05, 0.0]
            my_twist_angular = [0.0, 0.0, 0.0]
            
            #self.get_logger().info(f"looking")
        elif (self.looking == False): 
            
            my_twist_linear = [0.0, 0.0, 0.0]
            my_twist_angular = [0.0, 0.0, 0.0]
            
            #self.get_logger().info(f"found")

        cmd = TwistStamped()
        cmd.header.frame_id = 'tool0'
        cmd.header.stamp = self.get_clock().now().to_msg()
        cmd.twist.linear = Vector3(x=my_twist_linear[0], y=my_twist_linear[1], z=my_twist_linear[2])
        cmd.twist.angular = Vector3(x=my_twist_angular[0], y=my_twist_angular[1], z=my_twist_angular[2])
        #self.get_logger().info(f"Sending: linear: {cmd.twist.linear} angular: {cmd.twist.angular}")

        self.pub.publish(cmd)
    
    def avg_callback(self, msg):
        if self.i == 0: 
            self.avg = msg.data
            self.i = self.i + 1; 
        
        if (self.stop == False):
            if (abs(self.avg - msg.data) < 20.0):
                #self.get_logger().info(f"Sending: {abs(self.avg-msg.data)}")
                self.avg = msg.data
                self.looing = True
            else:
                #self.get_logger().info(f"Here: {abs(self.avg-msg.data)}")
                self.avg = msg.data
                self.looking = False 
                self.stop = True
    """
    def moving (self): 
        if(avg_callback(self)):
            my_twist_linear = [0.0, 0.05, 0.0]
            my_twist_angular = [0.0, 0.0, 0.0]
            publish_twist(self, my_twist_linear, my_twisit_angular)
        else if (avg_callback == false): 
            my_twist_linear = [0.0, 0.0, 0.0]
            my_twist_angular = [0.0, 0.0, 0.0]
            publish_twist(self, my_twist_linear, my_twisit_angular)
    """

def main(args=None):
    rclpy.init(args=args)
    
    down = rob_move_down()
    
    rclpy.spin(down)
    
    rclpy.shutdown()


if __name__ == '__main__':
    main()