#!/usr/bin/env python3
import rospy
from my_chatter.msg import TimestampString

# Import the String message type from the /msg directory of the std_msgs package.

# Define the method which contains the node's main functionality
def talker():
    # Create an instance of the rospy.Publisher object which we can  use to
    # publish messages to a topic. This publisher publishes messages of type
    # std_msgs/String to the topic /chatter_talk
    pub = rospy.Publisher('user_messages', TimestampString, queue_size=10)
    
    # Create a timer object that will sleep long enough to result in a 10Hz
    # publishing rate
    
    r = rospy.Rate(10) # 10hz

    # Loop until the node is killed with Ctrl-C
    while not rospy.is_shutdown():
        # Construct a string that we want to publish (in Python, the "%"
        # operator functions similarly to sprintf in C or MATLAB)
        # message = raw_input('Please enter a line of text and press <Enter>:')
        # timestamp = rospy.get_time()
        Tts = TimestampString()
        Tts.message = input('Please enter a line of text and press <Enter>:')
        Tts.timestamp = rospy.get_time()

        # Publish our string to the 'chatter_talk' topic
        pub.publish(Tts)
        print(Tts)
        # Use our rate object to sleep until it is time to publish again
        r.sleep()
            
# This is Python's syntax for a main() method, which is run by default when
# exectued in the shell
if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called /talker.
    rospy.init_node('talker', anonymous=True)

    # Check if the node has received a signal to shut down. If not, run the
    # talker method.
    try:
        talker()
    except rospy.ROSInterruptException: pass