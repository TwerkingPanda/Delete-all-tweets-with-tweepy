import tweepy
auth = tweepy.OAuthHandler('###qVRjUcwrNsdfsdsdfsdfYGV3', '###B2dSasdfsadfhasjkdbuisahdfkasndfk8qcDLik5lA5Epo')
auth.set_access_token('2####537297028-ksdfadfasfdaElYGqG9RHQq9t9D5ctICY', '#####XgKaCadfsasdasdaRyWZMOxAyYhuR')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    
    
   
   
   

#Work done. suspending midway
