import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32, String

from collections import deque

class Arduino1Avg(Node):

    def __init__(self):
        super().__init__(node_name = 'tof_avg')
        self.subscriber_ = self.create_subscription(String, 'arduino1', self.callback_data, 10)
        self.publisher_ = self.create_publisher(Float32,'arduino1avg',10)
        self.subscriptions 
        self.avg = deque([0.0])
        self.i = 0 

    def callback_data(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        #data = float(msg.data.strip())
        new_msg = Float32()
        data = float(msg.data)
        try: 
            if self.i == 0: 
                self.avg.append(data)
                self.i = self.i + 1
                self.avg.popleft()
                holder = sum(self.avg)/len(self.avg)
            elif self.i < 5: 
                self.avg.append(data)
                self.i = self.i + 1
                holder = sum(self.avg)/len(self.avg)
            else: 
                self.avg.append(data)
                self.avg.popleft()
                holder = sum(self.avg)/len(self.avg)
        except:
            holder = sum(self.avg)/len(self.avg)
            
        
        new_msg.data = holder 
        self.publisher_.publish(new_msg)
        self.get_logger().info(f"I heard: {msg.data} Published {new_msg.data}")
        

def main(args=None):
    rclpy.init(args=args)

    avg = Arduino1Avg()

    rclpy.spin(avg)
   
    rclpy.shutdown()
    


if __name__ == '__main__':
    main()