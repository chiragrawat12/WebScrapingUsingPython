from getLocator.locator import Locator
from bs4 import BeautifulSoup

class Search_Link:
    def __init__(self,re,userInput):
        self.soup=BeautifulSoup(re,"html.parser")
        self.userInput=userInput
    @property
    def Link(self):
        Nlocator=Locator.Mlocator
        name=self.soup.select_one(Nlocator).string.lower()
        if name.strip()==self.userInput:
            Mlocator=Locator.Mlocator
            link="https://www.imdb.com{}".format(self.soup.select_one(Mlocator).attrs['href'].strip())
            return link
        else:
            return None