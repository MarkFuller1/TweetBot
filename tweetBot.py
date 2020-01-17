import tweepy
import sys
import os

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  cfg = { 
    "consumer_key"        : os.environ['CONSUMER_KEY'],
    "consumer_secret"     : os.environ['CONSUMER_SECRET'],
    "access_token"        : os.environ['ACCESS_TOKEN'],
    "access_token_secret" : os.environ['ACCESS_TOKEN_SECRET']
    }

  api = get_api(cfg)
  tweet = ' '.join(sys.argv[1:])
  print(tweet)

  status = api.update_status(status=tweet) 

if __name__ == "__main__":
  main()
