import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

import serial

serialPort = serial.Serial(port = '/dev/ttyACM0', baudrate=115200,
                            bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

class ArduinoTOF1Publisher(Node):
    
    def __init__(self): 
        super().__init__(node_name = 'tof_pub')
        self.publisher_ = self.create_publisher(String,'arduino1',10)

        # Timer
        timer_period=0.000001
        self.timer = self.create_timer(timer_period, self.publish_data)
        
        # open serialport 
        #serialPort.open()
        

        #if self.conn:
         #   self.get_logger().info(f"Listening on {self.addr}")
        #return
    

    def publish_data(self):
        msg = String()
        try:
            # msg.data = float(self.conn.recv(10).decode().rstrip())
            line = serialPort.readline() 
            string = line.decode()
            newstring = string.split(';')
            try:
                msg.data = newstring[1]
            except: 
                msg.data = string
                
            #msg.data = float(string)
        except ValueError as e:
            print(f"{e}: Could not convert msg type to float.")

        self.publisher_.publish(msg)
        self.get_logger().info(f"TOF reading: {msg.data}")
        
    


def main(args=None):
    rclpy.init(args=args)

    arduino_publisher_1 = ArduinoTOF1Publisher()

    rclpy.spin(arduino_publisher_1)

    rclpy.shutdown()

    


if __name__ == '__main__':
    main()