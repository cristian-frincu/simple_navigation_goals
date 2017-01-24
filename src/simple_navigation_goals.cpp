#include <ros/ros.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <actionlib/client/simple_action_client.h>
#include <nav_msgs/Odometry.h>

#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <list>


using namespace std;

void split_line(string& line, string delim, list<string>& values)
{
    size_t pos = 0;
    while ((pos = line.find(delim, (pos + 1))) != string::npos) {
        string p = line.substr(0, pos);
        values.push_back(p);
        line = line.substr(pos + 1);
    }

    if (!line.empty()) {
        values.push_back(line);
    }
}



typedef actionlib::SimpleActionClient<move_base_msgs::MoveBaseAction> MoveBaseClient;


int main(int argc, char** argv){
  ros::init(argc, argv, "simple_navigation_goals");
  ros::NodeHandle n;


  //tell the action client that we want to spin a thread by default
  MoveBaseClient ac("move_base", true);

  //wait for the action server to come up
  while(!ac.waitForServer(ros::Duration(5.0))){
    ROS_INFO("Waiting for the move_base action server to come up");
  }

  move_base_msgs::MoveBaseGoal goal;



    ROS_INFO("Reading CSV File");
ifstream file ( "file.csv" );
 string value;
    list<string> values;
    while ( file.good() )
    {
        getline ( file, value, ',' ); // read a string until next comma: http://www.cplusplus.com/reference/string/getline/
        if (value.find('\n') != string::npos) {
            split_line(value, "\n", values);
        } else {
            values.push_back(value);
        }
    }

    list<string>::const_iterator it = values.begin();
    int selector=0;
    for (it = values.begin(); it != values.end(); it++) {
        string tmp = *it;
        selector++;
        double d;
        d = strtod(tmp.c_str(), NULL);
	ROS_INFO("%f",d);
    }


    ROS_INFO("Finished Reading CSV File");

  double goalX,goalY,goalW;
  for (int i =0; i <10;i++){
	  goalX = i;
	  goalY = i;
	  goalW = 1.0;
	  //we'll send a goal to the robot to move 1 meter forward
	  goal.target_pose.header.frame_id = "map";
	  goal.target_pose.header.stamp = ros::Time::now();

	  goal.target_pose.pose.position.x = goalX;
	  goal.target_pose.pose.position.y = goalY;
	  goal.target_pose.pose.orientation.w = goalW;

	  ROS_INFO("Sending goal, (%f,%f,%f)",goalX,goalY,goalW);
	  ac.sendGoal(goal);

	  ac.waitForResult();

	  if(ac.getState() == actionlib::SimpleClientGoalState::SUCCEEDED)
	    ROS_INFO("Hooray, reached point");
	  else{
	    ROS_INFO("The robot failed to go to %f,%f,%f",goalX,goalY,goalW);
	    ROS_INFO("Going to next point");
	  }	
  }

  return 0;
}
