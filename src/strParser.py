from bs4 import BeautifulSoup
import requests

class StrParser:
    def __init__(self):
        pass

    def parseUrl(self, url):
        return requests.get(url).text
    
    def findSubStr(self, line, startStr, endStr):
        start = line.find(startStr) + len(startStr)
        end = line.find(endStr, start)
        return line[start:end]