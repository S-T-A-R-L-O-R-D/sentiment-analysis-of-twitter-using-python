import tweepy
from matplotlib import pyplot as plt
from textblob import TextBlob
import codecs

def percentage(part,whole):
    return 100*float(part)/float(whole)

consumer_key="CvFNEUlZP81P72ekyIXxGBdfw"
consumer_secret_key="wIU1HVQppKRn2IIvWIYRHMIwxPGalq9SDibNLXVqVbZS5ZF4fR"
access_token="1074979255535034368-qDWcYDg0Aq3rbU4s8vDAp014oIc6gz"
access_secret_token="eFYs7wlDjKmslNzs6TpgDHrPoK0qqrCQ0TbQNLvmfhKR5"
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_secret_token)
api=tweepy.API(auth)
searchTerm=input("Enter the term you want to search\n")
noOfSearchTerm=int(input("Enter the number of tweets you want to feed\n"))
tweets=tweepy.Cursor(api.search,searchTerm).items(noOfSearchTerm)
positive=0
negative=0
neutral=0
polarity=0
not_analysed=0
file=codecs.open("test2.txt","wb","utf-8-sig")
for tweet in tweets:
    data=tweet.text
    #data=data.encode('utf-8-sig')
    file.write(data)
    #print(tweet.text)
    analysis=TextBlob(tweet.text)
    polarity+=analysis.sentiment.polarity
    if analysis.sentiment.polarity==0:
        neutral+=1
    if analysis.sentiment.polarity<0.00:
        negative+=1
    if analysis.sentiment.polarity>0.00:
        positive+=1
not_analysed=noOfSearchTerm-(positive+negative+neutral)
not_analysed=percentage(not_analysed,noOfSearchTerm)
#print(f"{positive}{negative}{neutral}{not_analysed}")
positive=percentage(positive,noOfSearchTerm)
neutral=percentage(neutral,noOfSearchTerm)
negative=percentage(negative,noOfSearchTerm)
#print(f"{positive,negative,neutral}")
positive=format(positive,".2f")
neutral=format(neutral,".2f")
negative=format(negative,".2f")
file.close()
label=[f"positive {positive} %",f"negative{negative}%",f"neutral{neutral}",f"no. of tweets not available for analysis{not_analysed}%"]
sizes=[positive,negative,neutral,not_analysed]
color=["yellowgreen","red","gold","black"]

patches,texts=plt.pie(sizes,colors=color,startangle=90)
plt.legend(patches,label,loc="lower right")
plt.title(f"how people are reacting on {searchTerm} by analysing {noOfSearchTerm} tweets!")
plt.axis('equal')
plt.tight_layout()
plt.show()