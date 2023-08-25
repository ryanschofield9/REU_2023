# REU_2023
Project worked on during the REU program in 2023. Using ros2, control a pruning gripper with the use of two tof sensors 

# How to run test_tof_branch

1. Plug arduino into computer (arduino must be loaded with the tof code provided)
  
2. Use the following command to allow ros to see the arduino
```
sudo chmod 777 /dev/ttyACM0
```
3. Download test_tof_branch folder into a src folder 

4. Start the UR5e in Rviz
     Run the following commands in seperate terminal (make sure to source ros2 in each tutorial.
```
ros2 launch ur_robot_driver ur5e.launch.py robot_ip:=10.10.10.10 use_fake_hardware:=true
```
```
ros2 launch ur_moveit_config ur_moveit.launch.py ur_type:=ur5e
```  
5. In the rviz window move the robot to a sutable starting position
   
6. Use the following command in a new terminal to switch to the forward_position_controller 
```
ros2 control switch_controllers --activate forward_position_controller --deactivate scaled_joint_trajectory_controller
```
7. Use the following command to start the servos
```
ros2 service call /servo_node/start_servo std_srvs/srv/Trigger
```
8. Use the following command in a new terminal start reading the arduino code 
```
ros2 run test_tof_branch talker_arduino
```
9. Use the following command in the new terminal start reading the arduino average 
```
ros2 run test_tof_branch talker_arduino_avg
```
10. Use the following command in the new terminal to test the robots ability to move down with the arduino in control 
```
ros2 run test_tof_branch down
```
       
