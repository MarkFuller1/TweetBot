import tweepy
import requests
import sys
import os

URL = "https://iscaliforniaonfire.com"

def getRecords():
    with open("records") as f:
        return f.read().split(' ', -1)

def writeRecords(current, overall):
    f = open("records", "w")
    f.write(current + " " + overall)
    f.close()

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def getFileData(fileName):
    with open(fileName) as f:
        return f.read()

def tweetText(api):
    text = ""
    if "-f" in sys.argv:
        fileName = sys.argv[2]
        content = getFileData(fileName)
        print(content)
        text = content

    elif "-c" in sys.argv:
        records = getRecords()
        print(records)

        current_record = records[0]
        record = records[1]

        raw = requests.get(url = URL)
        content = raw.content

        if "Yes" not in content:
            print("California is not on fire")
            text = "California is not on fire"

        else: 
            print ("California is on fire")
            text = "California is on fire"
            current_record = current_record + 1

        writeRecords(current_record, record)
        
    else:
        tweet = ' '.join(sys.argv[1:])
        print(tweet)
        text = tweet

    api.update_status(status=text)

def main():
  cfg = { 
    "consumer_key"        : os.environ['CONSUMER_KEY'],
    "consumer_secret"     : os.environ['CONSUMER_SECRET'],
    "access_token"        : os.environ['ACCESS_TOKEN'],
    "access_token_secret" : os.environ['ACCESS_TOKEN_SECRET']
    }

  api = get_api(cfg)

  tweetText(api)

  #status = api.update_status(status=tweet) 

if __name__ == "__main__":
  main()
