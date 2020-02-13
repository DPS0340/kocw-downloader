from os.path import dirname, abspath

class __SystemInfo__:
    def __init__(self):
        self.initUri = "http://www.kocw.net/home/cview.do?mty=p&kemId=1178264" # 가져올 kocw url
        self.videoUriFormat = "http://ocs.cau.ac.kr/contents/cau1000001/%s/contents/media_files/media/ssmovie.mp4" # 가져올 강의 cdn url
        self.name = "고급 C 프로그래밍" # output에 저장될 폴더 이름
        self.path = dirname(dirname(abspath(__file__))) # 프로그램의 경로
        self.parserType = "html.parser" # soup 파서
        self.pdfIncluded = True # 강의자료에 pdf 포함 여부

SystemInfo = __SystemInfo__()