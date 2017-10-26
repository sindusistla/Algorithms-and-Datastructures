import tweepy
from tweepy import Cursor
from tweepy import Stream
import json
import re
from textblob import TextBlob;


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print(status_code)
        return False

    def on_data(self, raw_data):
        all_data = json.loads(raw_data)
        # Extract only the text data
        tweet = all_data["text"].encode("utf-8")
        tweet=" ".join(re.findall("[a-zA-Z]+",tweet))
        username = all_data["user"]["screen_name"]
        # strip removes leading spaces
        print(tweet,username)
        blob=TextBlob(tweet.strip())
        senti=0;
        positive=0
        negative=0
        compound=0
        for sen in blob.sentences:
            senti=senti+sen.sentiment.polarity
            if (sen.sentiment.polarity >= 0):
                # positive comment
                positive=positive+ sen.sentiment.polarity
            else:
                negative=negative+sen.sentiment.polarity
        compound=compound+senti

        return True

if __name__ == '__main__':
    MAX_TWEETS=100
    consumer_key="ycUcQ8UnUpo9Hce3jY7FfI41m"
    consumer_secret="A4tNBg4EbVtLW0TWR4EDt8Fgn0B8XoQ0zFZClnbe9N8np4r9JU"
    access_token="2368878074-2PJNIDsk4uohhRPRqkOsWta6yr7QzwDn82av1kV"
    access_token_secret="ha4kSMsLsBgVN5TQv1JPN7H7GO3ZTGhKCo34W61uuAZZX"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
    myStream.filter(track=['ThisIsOU'])

#api = tweepy.API(auth)
# Get User info
# data = api.search("Bahubali")

# for line in data:
  #  print(line)
#retrieve user
'''user = api.get_user('SindooriTumulur')

print (user.followers_count)
for friend in user.friends():
   print (friend.screen_name)'''


'''data = Cursor(api.search, q='miami').items(MAX_TWEETS)
for line in data:
     print(line)'''

# Streaming API
# ''' myStreamListener = MyStreamListener()
#myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener())
# myStream.filter(track=['python'])'''


