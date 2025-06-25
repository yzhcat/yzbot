
环境
vmware 17
英文 ubuntu 22.04 ros humble

依赖
sudo apt install ros-humble-desktop-full

sudo apt install gazebo
sudo apt install ros-humble-gazebo-*

sudo apt install ros-humble-moveit
sudo apt install ros-humble-moveit-setup-assistant
sudo apt install ros-humble-moveit-*

sudo apt install ros-humble-controller-manager -y
sudo apt install ros-humble-joint-trajectory-controller ros-humble-joint-state-broadcaster -y

启动机械臂moveit
ros2 launch mybot demo.launch.py

启动机械臂moveit和gazebo仿真
ros2 launch mybot gazebo.launch.py
ros2 launch mybot my_moveit_rviz.launch.py

启动机械臂moveit和gazebo 底盘+机械臂+传感器仿真
ros2 launch mybot gazebo_world.launch.py
ros2 launch mybot my_moveit_rviz.launch.py

note:
moveit 配置时只以臂模型做参考，臂+底盘整体运行 moveit会出现link不匹配的Waring，规划会出错，但是可以执行动作，
可能需要把合并后的模型注释掉gazebo的部分重新通过moveit_setup_assistant 配置

TODO:
nav2
