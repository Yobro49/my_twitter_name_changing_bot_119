import tweepy
import os

def create_api():
  consumer_key = os.getenv('consumer_key')
  consumer_secret =os.getenv('consumer_secret')
  access_token = os.getenv('access_token')
  access_token_secret = os.getenv('access_token_secret')

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print("API created")
  return api
  
  # Complete code

def folllower_count(user):
  emoji_numbers = {0: "0", 1:"1", 2:"2", 3:"3", 4:"4", 
                  5:"5", 6:"6", 7:"7", 8:"8", 9:"9" }
  uf_split = [int(i) for i in str(user.folllower_count)]

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()])
  return emoji_followers

api  = create_api()
 
while True:
   user = api.get_user('DeveloperIdot')
   api.update_profile(name = f'Pranshu|{folllower_count(user)} Followers')
   print(f'Updating twitter name : PRANSHU|{folllower_count(user)} Followers')
   print('waiting to refresh')
   time.sleep(60)
  
