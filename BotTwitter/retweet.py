import tweepy
from time import sleep

#tokens da api do twitter
auth = tweepy.OAuthHandler(' ',' ')
auth.set_access_token(' ',' ')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

search = 'a fazenda' #irá procurar um tweet com essa palavra
numeroDeTweets = 300 #ele irá dar retweet até completar 300 retweets
contador = 0 #conta quantas vezes deu retweet

for tweet in tweepy.Cursor(api.search, search).items(numeroDeTweets):
    try:
        tweet.retweet()
        sleep(300) #intervalo de 5 min / 300s
        contador += 1
        print('tweet retuitado', contador)
    except tweepy.TweepError() as e: #caso houver erro
        print(e.reason)
    except StopIteration: #caso for parar
        break

