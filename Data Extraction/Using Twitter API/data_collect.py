import tweepy 
from tweepy import OAuthHandler
import json

def authenticate():
	consumer_key = ''
	consumer_secret = ''
	access_token = ''
	access_secret = ''

	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)

	api = tweepy.API(auth)
	return api

def get_data():
	screenname = input("Enter Twitter User: ")
	#n = input("Enter Number of Tweets: ")
	return (screenname)

def get_all__tweets(api, screenname):
	all__tweets = []
	tweets = api.user_timeline(screen_name = screenname)
	all__tweets.extend(tweets)
	oldest = all__tweets[-1].id-1
	while len(tweets) > 0:
		tweets = api.user_timeline(screen_name = screenname, count = 200, max_id = oldest)
		all__tweets.extend(tweets)
		oldest = all__tweets[-1].id - 1
		print ("...%s tweets downloaded do far"%(len(all__tweets)))
	return all__tweets

#def write2file(all__tweets):
#	file = open('tweets.json', 'wb')
#	for status in all__tweets:
#		json.dump(status._json, file, sort_keys = True, indent = 4)
#	print ("Done")
# 	file.close()

if __name__ == '__main__':
	api = authenticate()
	users = api.friends_ids()
	user = api.get_user(users[0])
	screenname = get_data()
	#screenname = user.screen_name
	print ("Fetching Tweets of "+screenname)
	all__tweets = get_all__tweets(api, screenname)
	#write2file(all__tweets)
