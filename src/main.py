from soupHandler import SoupHandler
from downloader import Downloader
from systemInfo import SystemInfo

class Main:
    def __init__(self):
        self.soupHandler = SoupHandler(SystemInfo.initUri)
        self.downloader = Downloader()

    def introduce(self):
        print("kocw 다운로드 프로그램.")
        print("대학교 자체 cdn 전용입니다.")
        print("url 수정은 소스코드를 직접 수정하세요.")
    
    def end(self):
        print("다운로드 완료 되었습니다.")

    def run(self):
        self.introduce()
        
        table = self.soupHandler.findTable()
        parsedOnClickStrings = self.soupHandler.parseOnClick(table)
        self.downloader.startIteratingDownload(parsedOnClickStrings)

        self.end()


if __name__ == "__main__":
    main = Main()
    main.run()
