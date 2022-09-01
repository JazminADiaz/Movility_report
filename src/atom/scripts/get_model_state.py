#!/usr/bin/env python

from unicodedata import name
from gazebo_msgs.srv import GetModelState
import rospy

class Robot:

    def __init__(self, name):
        self.name =name

class Positions:
    _robotListDict ={
        'robot_1': Robot('1'),
        'robot_2': Robot('2'),
    }




    def show_gazebo_models(self):
        try:
            model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
            for robot in self._robotListDict.values():
                robotName = "Robot" + str(robot.name)
                resp_coordinates = model_coordinates(robotName, "robot_footprint")
                print(robotName)
                print("Cube " + str(robot.name))
                print("Valeur de X : " + str(resp_coordinates.pose.position))
                print("Quaternion X : " + str(resp_coordinates.pose.orientation))

        except rospy.ServiceException as e:
            rospy.loginfo("Get Model State service call failed:  {0}".format(e))

if __name__ == '__main__':
    coor = Positions()
    coor.show_gazebo_models()