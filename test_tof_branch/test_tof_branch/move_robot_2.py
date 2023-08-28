import rclpy

from rclpy.node import Node

from std_msgs.msg import String, Float32

from example_interfaces.msg import Int64

from geometry_msgs.msg import TwistStamped, Vector3

import time 

class RobMove(Node):

    def __init__(self): 
        super().__init__('move')
        self.pub = self.create_publisher(TwistStamped, '/servo_node/delta_twist_cmds', 10)
        self.pub_timer = self.create_timer(1/10, self.publish_twist)
        self.subscriber_ = self.create_subscription(Float32,'arduino1avg',self.avg_callback, 10)
        self.subscriber_ = self.create_subscription(Float32,'arduino2avg',self.avg_callback_2, 10)
        self.subscriptions 
        self.avg1 = 0.0
        self.avg2 = 0.0
        self.dif1 = 0.0
        self.dif2 = 0.0
        self.flag = 0 
        self.step = [False, False, False, False]
        self.step_tracker = 1
        self.i1 = 0
        self.i2 = 0

    def publish_twist(self):
        my_twist_linear = [0.0, 0.0, 0.0] 
        my_twist_angular = [0.0, 0.0, 0.0]

        # positive y makes it go down 
        # negative y makes it go up

        # set twist messages to send
        if(self.step_tracker == 1): 
            
            if (self.step[0]== True): 
                
                my_twist_linear = [0.0, 0.05, 0.0]
                my_twist_angular = [0.0, 0.0, 0.0]
                
            elif (self.step[0]== False): 
                
                my_twist_linear = [0.0, 0.0, 0.0]
                my_twist_angular = [0.0, 0.0, 0.0]

        elif (self.step_tracker == 2):
            if (self.step[1] == True): 
                
                my_twist_linear = [0.0, 0.0, 0.0]
                if (self.flag == 1): 
                    my_twist_angular = [0.0, 0.0, 0.5]
                elif (self.flag == 2):
                     my_twist_angular = [0.0, 0.0, -0.5]
                
            elif (self.step[1] == False): 
                
                my_twist_linear = [0.0, 0.0, 0.0]
                my_twist_angular = [0.0, 0.0, 0.0]
        
        elif (self.step_tracker == 3): 
            if (self.step[2] == True): 
                
                my_twist_linear = [0.0, 0.0, 0.0]
                my_twist_angular = [0.0, 0.5, 0.0]
                
            elif (self.step[2] == False): 
                
                my_twist_linear = [0.0, 0.0, 0.0]
                my_twist_angular = [0.0, 0.0, 0.0]
        
        elif (self.step_tracker == 4):

            if (self.step[3] == True): 
            
                my_twist_linear = [0.0, 0.0, 0.05]
                my_twist_angular = [0.0, 0.0, 0.0]

            elif (self.step[3] == False): 
            
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
        
        if (self.i1 == 0):
            self.avg1 = msg.data
            self.i1 = 1
            self.step[0] = True
            
        else:
            self.dif1 = abs(self.avg1 - msg.data)
            self.avg1 = msg.data
            self.move()

    def avg_callback_2(self,msg):

        if(self.i2 == 0 ):
            self.avg2 = msg.data
            self.i2 = 1
            self.step[0] = True
        
        else:
            self.dif2 = abs(self.avg2 - msg.data)
            self.avg2 = msg.data
            print(f"reading: {msg.data}, avg: {self.avg2}, dif: {self.dif2}")
           
            
    def step1 (self):
        print(f"dif1: {self.dif1} dif2: {self.dif2}")
        if (self.dif1 > 20 and self.dif2 > 20 ):
            self.change_step(1,2)

        elif (self.dif1 > 20 or self.dif2 > 20): 
            if (self.dif1 > 20):
                self.flag = 1
            if(self.dif2 > 20):
                self.flag = 2
            self.change_step(1, 1)
    
    def step2 (self):
        
        if (self.flag == 1):
            print(f"dif2: {self.dif2}")
            if(self.dif2 > 20): 
                self.change_step(2, 1)
              
        elif(self.flag == 2):
            print(f"dif1: {self.dif1}")
            if(self.dif1 > 20):
                self.change_step(2,1)
    
    def step3 (self):
        print(f"avg1: {self.avg1}, avg2: {self.avg2}, dif: {abs(self.avg1 - self.avg2)}")
        if (abs(self.avg1 - self.avg2) < 5):
            self.change_step(3, 1)
    
    def step4 (self):
        print(f"avg1: {self.avg1}, avg2: {self.avg2}")
        if (self.avg1 < 80 and self.avg2 < 80):
            print("here")
            self.step[3] = False 

    def move (self): 
        print(f"step_tracker = {self.step_tracker}")
        if (self.step_tracker == 1): 
            self.step1()
        elif (self.step_tracker == 2):
            self.step2()
        elif (self.step_tracker == 3): 
            self.step3()
        elif (self.step_tracker == 4): 
            self.step4()

    def change_step (self, cur, val):
        self.step[cur - 1] = False
        self.step_tracker = self.step_tracker + val
        time.sleep(5)
        self.step[cur + val - 1] = True 


def main(args=None):
    rclpy.init(args=args)
    
    move = RobMove()
    
    rclpy.spin(move)
    
    rclpy.shutdown()


if __name__ == '__main__':
    main()