from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, FindExecutable
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('turtlesim_ns', default_value='turtlesim1'),
        DeclareLaunchArgument('new_background_r', default_value='200'),
        Node(
            package='turtlesim',
            namespace=LaunchConfiguration('turtlesim_ns'),
            executable='turtlesim_node',
            name='sim'
        ),
    ])
