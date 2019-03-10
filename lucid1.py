from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class stdOutListener(StreamListener):
    def on_data(self, raw_data):
        pass
    def on_error(self, status_code):