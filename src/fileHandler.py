from systemInfo import SystemInfo
import os

class FileHandler:
    def __init__(self):
        self.path = SystemInfo.path

    def safeMkdir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
            return True
        return False
    
    def saveBinaryFile(self, blob, type, name, ext):
        with open("%s/output/%s/%s.%s" % (self.path, type, name, ext), 'wb') as w:
            w.write(blob)