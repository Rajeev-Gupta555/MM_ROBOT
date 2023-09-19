import sys
import os
import math
package_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(package_directory)


from path_planner import Path_Planner
from drive_class import Diff_drive
import rospy 

mini_bot = None
def shutdown_callback():
    if mini_bot is not None:
        mini_bot.stop()
    
if __name__ == '__main__':
    rospy.init_node('my_tracjectory_follower_node', anonymous=True)
    # mini_bot = Diff_drive(0.287, 0.033)
    mini_bot = Diff_drive(0.574, 0.066)
    mini_bot.namespace = 'mobile_manipulator'
    navigator = Path_Planner(-0.1, -0.1, 2, 3)
    navigator.set_vehicle(mini_bot)
    navigator.only_point_movement = True
    # To move the bot to a point---->
    # navigator.move_to(3, 1)
    # generate circe points
    centre = (2, 2)
    radius = 2
    points = [(radius*math.cos(math.radians(theta*360/20))+centre[0], 
               radius*math.sin(math.radians(theta*360/20))+centre[1]) for theta in range(-5, 16)]
    print(points)
    
    # move bot
    try:
        for point in points:
            navigator.move_to(point[0], point[1])
    except (KeyboardInterrupt, rospy.ROSInterruptException):
        rospy.loginfo('Stopping bot :(')
        mini_bot.stop()
    
    rospy.on_shutdown(shutdown_callback)
    rospy.spin()