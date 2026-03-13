#!/bin/bash
# Launch ROS2 Humble magnet publisher and subscriber in separate terminals

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PUBLISHER="$SCRIPT_DIR/magnet_sensor/magnet_publisher.py"
SUBSCRIBER="$SCRIPT_DIR/magnet_sensor/magnet_subscriber.py"

ROS_SETUP="source /opt/ros/humble/setup.bash"

# Open publisher in a new terminal
osascript -e "
tell application \"Terminal\"
    activate
    do script \"$ROS_SETUP && python3 '$PUBLISHER'; exec bash\"
    set custom title of front window to \"Magnet Publisher\"
end tell
"

# Open subscriber in a new terminal
osascript -e "
tell application \"Terminal\"
    activate
    do script \"$ROS_SETUP && python3 '$SUBSCRIBER'; exec bash\"
    set custom title of front window to \"Magnet Subscriber\"
end tell
"

echo "Launched magnet publisher and subscriber in separate terminals."
