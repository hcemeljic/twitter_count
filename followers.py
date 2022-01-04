import json
import time
import tweepy


def get_twitter_followers(args, twitter_handle):
    credentials_json = json.loads(open(args.credentials_path).read())
    twitter_token = credentials_json.get('twitter_api_token')

    twitter = tweepy.Client(bearer_token=twitter_token)
    try:
        followers = twitter.get_user(username=twitter_handle, user_fields=["public_metrics"]).data.public_metrics['followers_count']
        print(twitter_handle, followers)
        time.sleep(1)
        return followers
    except:
        pass
