import requests
from Search_Movie.Movie_Link import Search_Link
from Search_Score.Score import Search_Score
userInput=input("Enter Name of Movie to search its IMBD Score: ").strip().lower()
url="https://www.imdb.com/find?q={}&ref_=nv_sr_sm".format(userInput)
result_content= requests.get(url).content
link_obj=Search_Link(result_content,userInput)
link=link_obj.Link
# print(link)
if link==None:
    print("This name of movie is'nt Availabele!")
else:
    score_content=requests.get(link).content
    score_obj=Search_Score(score_content)
    score=score_obj.Score
    print("--------------------------------------------------------------------------------")
    print("Name of Movie: {}\nIMDb score: {}/10".format(userInput.title(), score))
    print("--------------------------------------------------------------------------------")












