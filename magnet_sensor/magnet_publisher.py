import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import serial

class MagnetPublisher(Node):
    def __init__(self):
        super().__init__('magnet_publisher')

        self.publisher = self.create_publisher(Bool, '/magnet_present', 10)

        self.ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
        print("Serial name:", self.ser.name)

        self.timer = self.create_timer(0.5, self.poll_serial)
	

    def poll_serial(self):
        waiting = self.ser.in_waiting
        if waiting == 0:
            return
        data = self.ser.read(waiting).decode('utf-8')
        print("Data:", data)

        msg = Bool()
        msg.data = "1" in data

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
