
import rclpy
from rclpy.node import Node



class MoveitControlNode(Node):
    def __init__(self):
        super().__init__('moveit_control_node')

       
        

def main(args=None):
  
    rclpy.init(args=args)

    moveit_control_node = MoveitControlNode()
    rclpy.spin(moveit_control_node)
    

    
    
    