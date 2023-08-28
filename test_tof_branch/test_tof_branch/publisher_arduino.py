import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

import serial

import time 

from collections import deque

serialPort = serial.Serial(port = '/dev/ttyACM0', baudrate=115200,
                            bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

class ArduinoTOF1Publisher(Node):
    
    def __init__(self): 
        super().__init__(node_name = 'tof_pub')
        self.i = 0
        self.avg = deque([0.0])
        self.avg2 = deque([0.0])
        self.publisher_ = self.create_publisher(Float32,'arduino1avg',10)
        self.publisher_2 = self.create_publisher(Float32, 'arduino2avg', 10)
        time.sleep(3)

        # Timer
        timer_period=0.000001
        self.timer = self.create_timer(timer_period, self.publish_data)
        
        # open serialport 
        #serialPort.open()
        

        #if self.conn:
         #   self.get_logger().info(f"Listening on {self.addr}")
        #return
    

    def publish_data(self):
        msg = Float32()
        msg_2 = Float32()
        try:
            # msg.data = float(self.conn.recv(10).decode().rstrip())
            line = serialPort.readline() 
            string = line.decode()
            newstring = string.split(';')
            try:
                holder1 = float(newstring[1])
                holder2 = float(newstring[3])
                
                if self.i == 0: 
                    self.avg.append(holder1)
                    self.avg2.append(holder2)
                    self.i = self.i + 1
                    self.avg.popleft()
                    self.avg2.popleft()
                    val = sum(self.avg)/len(self.avg)
                    val2 = sum(self.avg2)/len(self.avg2)
                elif self.i < 5: 
                    self.avg.append(holder1)
                    self.avg2.append(holder2)
                    self.i = self.i + 1
                    val = sum(self.avg)/len(self.avg)
                    val2 = sum(self.avg2)/len(self.avg2)
                else: 
                    self.avg.append(holder1)
                    self.avg2.append(holder2)
                    self.avg.popleft()
                    self.avg2.popleft()
                    val = sum(self.avg)/len(self.avg)
                    val2 = sum(self.avg2)/len(self.avg2)
                    
            except: 
                val = sum(self.avg)/len(self.avg)
                val2 = sum(self.avg2)/len(self.avg2)
                
        except ValueError as e:
            print(f"{e}: Could not convert msg type to float.")

        msg.data = val
        msg_2.data = val2
        self.publisher_.publish(msg)
        self.publisher_2.publish(msg_2)
        try: 
            self.get_logger().info(f"TOF reading: {newstring[1]}, {newstring[3]}, Publishing: {msg.data}, {msg_2.data}")
        except: 
            self.get_logger().info("No Reading")

        
    


def main(args=None):
    rclpy.init(args=args)

    arduino_publisher_1 = ArduinoTOF1Publisher()

    rclpy.spin(arduino_publisher_1)

    rclpy.shutdown()

    


if __name__ == '__main__':
    main()