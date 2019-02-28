import praw
import random
import requests
from PIL import Image
import tweepy
import time

#Fill in the codes loacated in your Twitter app details
consumer_key = 'key'
consumer_secret = 'secret'
access_token = 'accesstoken'
access_token_secret = 'accesstokensecret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

reddit = praw.Reddit(client_id='youclientid',
                     client_secret='yourclientsecret',
                     user_agent='yourappname',
                     username='yourusername',
                     password='yourpw') #Fill in the following information in order to authorize your script for Reddit

subreddit = reddit.subreddit('subreddit') #The subreddit your gonna use

secinterval = 15 #Seconds
mininterval = 60 * 15 #Minutes
hrinterval = 60 * 60 * 1 #Hours

while True:
    random_submission = reddit.subreddit('subreddit').random() #Name the subreddit
    url = random_submission.url
    img = Image.open(requests.get(url, stream=True).raw)
    extension = url.split(".")
    if extension[-1] == "jpg":
        print(random_submission.title)  # Output: the submission's title
        print(url)
        img.save("filename.jpg") #Name the file (dont change the extension)
        api.update_with_media("filename.jpg", status=random_submission.title) #uploads the image
    elif extension[-1] == "png":
        print(random_submission.title)  # Output: the submission's title
        print(url)
        img.save("filename.png") #Name the file (dont change the extension)
        api.update_with_media("filename.png", status=random_submission.title) #uploads the image
    else:
        print("no image/supported extension")
        api.update_status(random_submission.title + " " + url) #if no image, post with url
    time.sleep(mininterval) #use the variables that were defined before this while loop
