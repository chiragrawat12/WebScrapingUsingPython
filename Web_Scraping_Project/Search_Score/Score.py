from getLocator.locator import Locator
from bs4 import BeautifulSoup

class Search_Score:
    def __init__(self,score_content):
        self.soupS = BeautifulSoup(score_content, "html.parser")
    @property
    def Score(self):
        Slocator=Locator.Slocator
        score=self.soupS.select_one(Slocator).string
        return score
