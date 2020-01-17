import tweepy
import sys

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "MgINRSiEaQ9Qk88mMT5Xc2Y7l",
    "consumer_secret"     : "c0nuzzigPVyqUpebXeRbJIRKY1YzFUsxalS1NfrBcM99QteRHu",
    "access_token"        : "1216486167790735361-uuOFfoTAGnTzV95fCuugbuqrauEvIB",
    "access_token_secret" : "b9cJ3x7An6R4UIrctkCcng70umM4FC6Vn6OYSKshNYVGv" 
    }

  api = get_api(cfg)
  tweet = ' '.join(sys.argv[1:])
  print(tweet)
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
