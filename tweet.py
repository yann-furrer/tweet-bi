from ast import Str
import tweepy
import pandas as pd
import env
# assuming twitter_authentication.py contains each of the 4 oauth elements (1 per line)
# from twitter_authentication import , API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

API_KEY = env.api_key
API_SECRET = env.api_secret
ACCESS_TOKEN = env.access_token
ACCESS_TOKEN_SECRET = env.access_token_secret
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

query = 'Ukraine'
max_tweets = 2
all_tweets = []
df = {}

searched_tweets = [status for status in tweepy.Cursor(api.search_tweets, q=query, tweet_mode="extended").items(max_tweets)]
for page in searched_tweets:
            
            hashtag_sort = []
            
            parsed_tweet = {}
            parsed_tweet['lang'] = page._json["lang"]
            parsed_tweet['author'] = page._json["user"]["name"]
            parsed_tweet["date"] = page._json["created_at"]
            for hashtag in page._json["entities"]["hashtags"]:
                           
                                                      
                            del hashtag["indices"]  
                           
                            hashtag_sort.append(hashtag["text"])
            parsed_tweet["hashtag"] =  ','.join(hashtag_sort)
            hashtag_sort = []         
            parsed_tweet['text'] = page._json["full_text"]
            parsed_tweet['number_of_likes'] = page._json["user"]["favourites_count"]
            parsed_tweet['number_of_follower'] = page._json["user"]["followers_count"]
            parsed_tweet['number_of_retweets'] = page._json["retweet_count"]
            # parsed_tweet['number_of_retweets'] = page._json["retweet_count"]
            df = pd.DataFrame(all_tweets)
            
        #  # Revome duplicates if there are any
            all_tweets.append(parsed_tweet)
            # df = df.drop_duplicates("text", keep='first')
            df = pd.DataFrame(all_tweets)
           
            df.to_csv('../tweet_bi/Data/tweet.csv')
    # Create dataframe 