import requests
from bs4 import BeautifulSoup
from functools import reduce
import operator
import os
from os.path import dirname, abspath

def safe_mkdir(dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
        return True
    return False

def introduce():
    print("kocw 다운로드 프로그램.")
    print("대학교 자체 cdn 전용입니다.")
    print("url 수정은 소스코드를 직접 수정하세요.")

def main():
    introduce()

    init_uri = "http://www.kocw.net/home/cview.do?mty=p&kemId=1178264"
    videoUriFormat = "http://ocs.cau.ac.kr/contents/cau1000001/%s/contents/media_files/media/ssmovie.mp4"
    path = dirname(dirname(abspath(__file__)))
    pdfIncluded = True

    html = requests.get(init_uri).text
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table", class_="tbType01").tbody
    onclickStrings = [tag["onclick"] for tag in table.find_all("a") if tag.has_attr('onclick')]

    count = 0
    for line in onclickStrings:
        count += 1

        start = line.find("'") + 1
        end = line.find("'", start)
        uri = line[start:end]
        print(uri)

        if not pdfIncluded or count % 2 == 1:
            code = uri.split("/")[-1]
            safe_mkdir("%s/output/video" % path)
            print("%s 다운로드 중..." % (videoUriFormat % code))
            res = requests.get(videoUriFormat % code)
            with open("%s/output/video/%d.mp4" % (path, count), 'wb') as w:
                w.write(res.content)
        else:
            res = requests.get(uri)
            print("%s 다운로드 중..." % uri) 
            safe_mkdir("%s/output/pdf" % path)
            with open("%s/output/pdf/%d.pdf" % (path, count), 'wb') as w:
                w.write(res.content)

if __name__ == "__main__":
    main()

