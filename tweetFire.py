import requests

URL = "http://iscaliforniaonfire.com/"

r = requests.get(url = URL)

responce = r.content

if "Yes" not in responce:
    print("California is NOT on FIRE")
else:
    print("Califoria is on fire")

