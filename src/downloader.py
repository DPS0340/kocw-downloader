from systemInfo import SystemInfo
from fileHandler import FileHandler
from strParser import StrParser
import requests

class Downloader:
    def __init__(self):
        self.path = SystemInfo.path
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
                self.fileHandler.safeMkdir("%s/output/video" % self.path)
                downloadUri = self.videoUriFormat % code
                print("%s 다운로드 중..." % (downloadUri))
                res = requests.get(downloadUri)
                self.fileHandler.saveBinaryFile(res.content, "video", count, "mp4")
            else:
                print("%s 다운로드 중..." % uri) 
                res = requests.get(uri)
                self.fileHandler.safeMkdir("%s/output/pdf" % self.path)
                self.fileHandler.saveBinaryFile(res.content, "pdf", count, "pdf")
