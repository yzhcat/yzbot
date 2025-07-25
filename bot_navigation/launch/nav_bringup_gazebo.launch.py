#!/usr/bin/python3

# Copyright (c) 2022, www.guyuehome.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import ExecuteProcess



def generate_launch_description():
    navigation2_dir = get_package_share_directory('bot_navigation')
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    map_yaml_file = "map.yaml"

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    map_yaml_path = LaunchConfiguration('map',default=os.path.join(navigation2_dir,f'maps/{map_yaml_file}'))
    nav2_param_path = LaunchConfiguration('params_file',default=os.path.join(navigation2_dir,'param','originbot_nav2.yaml'))
    slam = LaunchConfiguration('slam', default='False')  
    rviz_config_dir = os.path.join(nav2_bringup_dir,'rviz','nav2_default_view.rviz')
    # slam = LaunchConfiguration('slam', default='True')

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time',default_value=use_sim_time,description='Use simulation (Gazebo) clock if true'),
        DeclareLaunchArgument('params_file',default_value=nav2_param_path,description='Full path to param file to load'),
        DeclareLaunchArgument("map", default_value=map_yaml_path, description='Full path to map file to load'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([nav2_bringup_dir,'/launch','/bringup_launch.py']),
            launch_arguments={
                'map': map_yaml_path,
                'use_sim_time': use_sim_time,
                'params_file': nav2_param_path,
                'slam': slam,}.items(),
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_dir],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen'),

        # # sleep(5) # 等待一段时间，等待地图加载完成
        # ExecuteProcess(
        #     cmd=['sleep', '5'],
        #     output='screen'
        # ),
        # ExecuteProcess(
        #     cmd=['ros2', 'lifecycle', 'set', '/map_server', 'configure'],
        #     output='screen'
        # ),
        # ExecuteProcess(
        #     cmd=['ros2', 'lifecycle', 'set', '/map_server', 'activate'],
        #     output='screen'
        # ),
    ])
