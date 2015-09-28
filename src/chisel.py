import rospy;
from chisel_msgs import *;

class Chisel:
    """Wraps chisel_ros in a convenient interface"""
    
    def __init__(self, server_name='Chisel'):
        self.server_name = server_name;
        
   def start(self):
        print 'Waiting for ' + self.server_name + ' server ...';
        rospy.wait_for_service(self.server_name + '/' + 'Reset');
        print 'Found server.';
        self.reset = rospy.ServiceProxy(self.server_name + '/' + 'Reset', chisel_msgs.ResetService);
        self.toggle_paused = rospy.ServiceProxy(self.server_name + '/' + 'TogglePaused', chisel_msgs.PauseService);
        self.save_mesh = rospy.ServiceProxy(self.server_name + '/' + 'SaveMesh', chisel_msgs.SaveMeshService);
        self.get_all_chunks = rospy.ServiceProxy(self.server_name + '/' + 'GetAllChunks', chisel_msgs.GetAllChunksService);
