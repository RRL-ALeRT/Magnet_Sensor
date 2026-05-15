import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import serial

class MagnetPublisher(Node):
    def __init__(self):
        super().__init__('magnet_publisher')

        self.publisher = self.create_publisher(Bool, '/magnet_present', 10)

        self.ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=0.1)
        print("Serial name:", self.ser.name)

        self.timer = self.create_timer(0.1, self.poll_serial)

    def poll_serial(self):
        # Drain any pending lines to avoid getting stuck on a single read.
        while self.ser.in_waiting:
            raw = self.ser.readline()
            if not raw:
                break

            line = raw.decode('utf-8', errors='ignore').strip()
            if not line:
                continue

            try:
                digital_val = int(line.split()[0])
            except (ValueError, IndexError):
                continue

            magnet_detected = (digital_val != 0)

            print(f"Magnet detected: {magnet_detected}")

            msg = Bool()
            msg.data = magnet_detected
            self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MagnetPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
