import pylsl
from pylsl import StreamInfo, StreamOutlet
import configparser
import os, sys

class LSL_controller():

    outlet = None
    path = None

    def __init__(self):

        self.path = os.path.dirname(sys.modules['__main__'].__file__)
        
        if not os.path.isfile(self.path + "/config.ini"):
            self.create_ini()
            print ("no config file \nCreating new file")
            print("stream name = " + 'LSLMarkerStream')
        
            
        config = configparser.ConfigParser()
        config.read(self.path + "/config.ini")

        stream_name = config['LSL_stream']['Name'].strip()
        self.startOutletStream(stream_name)

            

    def startOutletStream(self,Name):
        lslInfo = StreamInfo(Name, 'Markers', 1, 0, 'string', 'LSL marker')  
        self.outlet = StreamOutlet(lslInfo)
        

    def send_marker(self, marker):

        if len(marker) != 1 :
            print("invalid marker")

        else:
            self.outlet.push_sample(str(marker))



    def create_ini(self):

        config = configparser.ConfigParser()

        config['LSL_stream'] = {'Name' : 'LSLMarkerStream'}

        

        with open(self.path + "/config.ini", 'w') as configfile:
            config.write(configfile)



