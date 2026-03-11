import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class MagnetSubscriber(Node):
    def __init__(self):
        super().__init__('magnet_subscriber')
        self.subscription = self.create_subscription(
            Bool,
            '/magnet_present',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info('Magnet present: %s' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    magnet_subscriber = MagnetSubscriber()

    rclpy.spin(magnet_subscriber)

    magnet_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
