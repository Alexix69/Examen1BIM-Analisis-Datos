import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "BRCIEJ2hHObBHUyw6KRn8Uj6u"
csecret = "vBNwCpbPWMeTgwVvqL9NGNoanlsIsMnZoatKvBRhclY5aEWkCF"
atoken = "1251569508222935046-8Z1IGuTg8V51QltWaR9O6C19AhbrTk"
asecret = "n4pvp29RDvGrtzVexKPYvguVzQEZR0zlucdGEi7nuknzm"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://alexis:.-261727-.@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('juegosolimpicosnagano')
except:
    db = server['juegosolimpicosnagano']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[137.910101,36.460702,138.318899,36.835734])  
#twitterStream.filter(track=['fortnite','freefire'])