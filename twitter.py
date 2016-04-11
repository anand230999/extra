import oauth2 as oauth
import json
from sys import argv
count =0
CONSUMER_KEY = "3AftlqM1umGMroSjZkpXr3GUH"
CONSUMER_SECRET = "jchT7UAxWNcWlbyAFOkLgRSRcY56cDGuSLPMunAnW4ZouD91rm"
ACCESS_KEY = "172601787-hgzlSicp47ARWKzYFvrjiiSPDBBvKbxwoVuvL9Q5"
ACCESS_SECRET = "TznA0AKodZ2O7JI6lfz6PAM0lRDxtEtoHInP5ebU3sg37"
consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)
url= "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+str(argv[1])+"&count=10"
resp, data = client.request(url)
tweets = json.loads(data)
for tweet in tweets:
    print tweet['text']+"\n"
