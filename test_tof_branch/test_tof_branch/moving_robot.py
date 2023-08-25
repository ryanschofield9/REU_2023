import rclpy

from rclpy.node import Node

from std_msgs.msg import String, Float32

from example_interfaces.msg import Int64

from geometry_msgs.msg import TwistStamped, Vector3

import time 

class rob_move(Node):

    def __init__(self): 
        super().__init__('move')
        self.pub = self.create_publisher(TwistStamped, '/servo_node/delta_twist_cmds', 10)
        self.pub_timer = self.create_timer(1/10, self.publish_twist)
        self.subscriber_ = self.create_subscription(Float32,'arduino1avg',self.avg_callback, 10)
        self.subscriptions 
        self.i = 0
        self.avg = 0.0; 
        self.step1 = True 
        self.step2 = False 
        self.step3 = False
        self.step4 = False
        self.step_tracker = 1
        self.stop = False 
        self.waiting = False 

    
    def publish_twist(self):
        my_twist_linear = [0.0, 0.0, 0.0] 
        my_twist_angular = [0.0, 0.0, 0.0]

        # positive y makes it go down 
        # negative y makes it go up

        # set twist messages to send
        if(self.step_tracker == 1): 
            
            if (self.step1 == True): 
                
                my_twist_linear = [0.0, 0.05, 0.0]
                my_twist_angular = [0.0, 0.0, 0.0]
                
            elif (self.step1 == False): 
                
                my_twist_linear = [0.0, 0.0, 0.0]
                my_twist_angular = [0.0, 0.0, 0.0]

        elif (self.step_tracker == 2):
            if (self.step2 == True): 
                
                my_twist_linear = [0.0, 0.0, 0.0]
                my_twist_angular = [0.0, 0.0, 0.5]
                
            elif (self.step2 == False): 
                
                my_twist_linear = [0.0, 0.0, 0.0]
                my_twist_angular = [0.0, 0.0, 0.0]
        
        elif (self.step_tracker == 3): 
            if (self.step3 == True): 
                
                my_twist_linear = [0.0, 0.0, 0.0]
                my_twist_angular = [0.0, 0.5, 0.0]
                
            elif (self.step3 == False): 
                
                my_twist_linear = [0.0, 0.0, 0.0]
                my_twist_angular = [0.0, 0.0, 0.0]
        
        elif (self.step_tracker == 4):

            if (self.step4 == True): 
            
                my_twist_linear = [0.0, 0.0, 0.05]
                my_twist_angular = [0.0, 0.0, 0.0]

            elif (self.step4 == False): 
            
                my_twist_linear = [0.0, 0.0, 0.0]
                my_twist_angular = [0.0, 0.0, 0.0]
            
        cmd = TwistStamped()
        cmd.header.frame_id = 'tool0'
        cmd.header.stamp = self.get_clock().now().to_msg()
        cmd.twist.linear = Vector3(x=my_twist_linear[0], y=my_twist_linear[1], z=my_twist_linear[2])
        cmd.twist.angular = Vector3(x=my_twist_angular[0], y=my_twist_angular[1], z=my_twist_angular[2])
        #self.get_logger().info(f"Sending: linear: {cmd.twist.linear} angular: {cmd.twist.angular}")

        self.pub.publish(cmd)
    
    def avg_callback(self, msg):
        if (self.waiting == False):     
            if self.i == 0: 
                self.avg = msg.data
                self.i = self.i + 1; 
            
            if (self.stop == False):
                if (abs(self.avg - msg.data) < 20.0):
                    #self.get_logger().info(f"Sending: {abs(self.avg-msg.data)}")
                    self.avg = msg.data
                    
                else:
                    #self.get_logger().info(f"Here: {abs(self.avg-msg.data)}")
                    
                    if (self.step_tracker == 1):
                        self.step1 = False
                        self.step2 = True

                    if (self.step_tracker == 2):
                        self.step2 = False
                        self.step3 = True
                    
                    if (self.step_tracker == 3):
                        self.step3 = False
                        self.step4 = True
                    
                    if (self.step_tracker == 4):
                        self.step4 = False

                    if (self.step_tracker == 5): 
                        self.stop = True
                    
                    self.step_tracker = self.step_tracker + 1
                    time.sleep(5)
                    self.waiting = True
        else:  
            self.avg = msg.data 
            self.waiting = False

def main(args=None):
    rclpy.init(args=args)
    
    move = rob_move()
    
    rclpy.spin(move)
    
    rclpy.shutdown()


if __name__ == '__main__':
    main()