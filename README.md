# simple_navigation_goals
A ROS node that will take as input a CSV file with coordinates, and go to each one consecutively.

#To run:
 - clone the repo in your catkin_ws
 - run catkin_make
 - cd catkin_ws/devel/lib/simple_navigation_goals/
 - add a CSV file named "file.csv", containing the (x,y,orientation) of the pathway you want the robot to travel
 - ./simple_navigation_goals
 
 
Note: The max number of points you can have with the default code is 25, but it can be easily modified by editing the MAX_POINTS, to whatever value you wish. Just don't forget to compile by running 'catkin_make'
