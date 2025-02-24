import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mscrobotics2425laptop27/Documents/University/robotic_systems_design_project/manipulator_work/manipulator_ros2_workspace/install/manipulator_package'
