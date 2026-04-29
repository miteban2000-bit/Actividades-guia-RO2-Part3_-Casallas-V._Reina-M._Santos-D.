from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    pkg_path = os.path.join(
        os.getenv('HOME'),
        'ros2_ws/src/Actividades_guia_RO2_Part3/dif_bot_description/activity5'
    )
    urdf_file = os.path.join(pkg_path, 'urdf/dif_bot_description.urdf')
    rviz_config = os.path.join(pkg_path, 'rviz/dif_bot.rviz')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': open(urdf_file).read()}],
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config],
        ),
    ])
