import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import serial
from std_msgs.msg import Bool

class MagnetPublisher(Node):
    def __init__(self):
        super().__init__('magnet_publisher')

        self.publisher = self.create_publisher(Bool, '/magnet_present', 10)

        self.ser = serial.Serial('/dev/ttyACM0')
        self.ser.baudrate = 9600
        print("Serial name:", self.ser.name)

        self.timer = self.create_timer(0.01, self.poll_serial)


    def poll_serial(self):
        line = str(self.ser.readline())
        print("Line:", line)

        if "D:" in line:
            parts = line.split(':')
            d = parts[1][:-2]
            print("D:", d)

            msg = Bool()
            msg.data = d == "1"

            self.publisher.publish(msg)
            print("Published msg:", msg)




def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MagnetPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()