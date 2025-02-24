from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution

def generate_launch_description():
     ld = LaunchDescription()
      

     px150_simulation = IncludeLaunchDescription(  # Launches premade interbox Gz_classic simulation which interacts moveit2
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('interbotix_xsarm_moveit_interface'),
                    'launch',
                    'xsarm_moveit_interface.launch.py'
                ])
            ]),
            launch_arguments={
                'robot_model': 'px150',
                'hardware_type': 'gz_classic',
                'use_moveit_interface_gui':'false',
                
            }.items()
        )
     moveit_control_node = LaunchDescription([Node(output = 'screen',
                                                   emulate_tty = True,
                                                   package = 'manipulator_package',
                                                   executable='moveit_control_node',
                                                   name='moveit_control_node')])
     
    

     
     ld.add_action(px150_simulation)
     ld.add_action(moveit_control_node)

     return ld