import tweepy
import requests
import sys
import os

URL = "http://iscaliforniaonfire.com"

def getRecords():
    with open("records") as f:
        return f.read().split(' ', -1)

def writeRecords(current, overall):

    f = open("records", "w")
    f.write(str(current) + " " + str(overall))
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

        current_record = int(records[0])
        record = int(records[1])

        raw = requests.get(url = URL)
        requestData = raw.content

        if "Yes" not in str(requestData):
            print("California is not on 🔥")
            text = "California is not on 🔥"

        else: 
            print ("California is on 🔥")
            text = "California is on 🔥"
            current_record += 1


        if current_record > record:
            record = current_record

        writeRecords(current_record, record)

        text += "\n\nCurrent Streak: " + str(current_record) + " \nRecord: " + str(record)
        
    else:
        tweet = ' '.join(sys.argv[1:])
        print(tweet)
        text = tweet

    print(text) 
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
