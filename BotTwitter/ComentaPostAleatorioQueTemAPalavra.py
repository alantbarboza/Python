import tweepy
from time import sleep

#tokens da api do twitter
auth = tweepy.OAuthHandler(' ',' ')
auth.set_access_token(' ',' ')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = 'cabelo' #irá procurar um tweet com essa palavra
numeroDeTweets = 300 #ele irá comentar até completar 300 comentários
contador = 0 #conta quantas vezes comentou em um post

for tweet in tweepy.Cursor(api.search, search).items(numeroDeTweets):
    try: #cria um comentario, em um post aleatório que tem a palavra
        api.update_status(status=" " + tweet.user.screen_name + " mensagem "  , in_reply_to_status_id = tweet.id_str , auto_populate_reply_metadata=True)
        contador += 1
        print("tweet ok " , contador)
        sleep(120) #intervalo de 2 min / 120s
    except tweepy.TweepError as e: #caso houver erro
        print(e.reason)
    except StopIteration: #caso for parar
        break