from systemInfo import SystemInfo
from fileHandler import FileHandler
from strParser import StrParser
import requests

class Downloader:
    def __init__(self):
        self.path = SystemInfo.path
        self.name = SystemInfo.name
        self.videoUriFormat = SystemInfo.videoUriFormat
        self.fileHandler = FileHandler()
        self.strParser = StrParser()

    def startIteratingDownload(self, parsedOnclicks):
        count = 0
        for line in parsedOnclicks:
            count += 1

            uri = self.strParser.findSubStr(line, "'", "'")
            print(uri)

            if not SystemInfo.pdfIncluded or count % 2 == 1:
                code = uri.split("/")[-1]
                self.fileHandler.safeMkdir("%s/output/%s/video" % (self.path, self.name))
                downloadUri = self.videoUriFormat % code
                print("%s 다운로드 중..." % (downloadUri))
                res = requests.get(downloadUri)
                if SystemInfo.pdfIncluded:
                    number = (count + 1) // 2    
                self.fileHandler.saveBinaryFile(res.content, "video", number, "mp4")
            else:
                print("%s 다운로드 중..." % uri) 
                res = requests.get(uri)
                self.fileHandler.safeMkdir("%s/output/%s/pdf" % (self.path, self.name))
                number = (count + 1) // 2
                self.fileHandler.saveBinaryFile(res.content, "pdf", number, "pdf")
