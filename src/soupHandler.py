from bs4 import BeautifulSoup
from systemInfo import SystemInfo
from strParser import StrParser
import requests

class SoupHandler:
    def __init__(self, url):
        html = StrParser().parseUrl(url)
        self.soup = BeautifulSoup(html, SystemInfo.parserType)

    def findTable(self):
        table = self.soup.find("table", class_="tbType01").tbody
        return table

    def parseOnClick(self, table):
        return [tag["onclick"] for tag in table.find_all("a") if tag.has_attr('onclick')]