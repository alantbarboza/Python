import tweepy
from time import sleep

#tokens da api do twitter
auth = tweepy.OAuthHandler(' ',' ')
auth.set_access_token(' ',' ')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = 'a' #irá procurar um tweet com essa palavra para ativar a ação do bot
numeroDeTweets = 300 #ele irá comentar até completar 300 comentários
contador = 0 #conta quantas vezes comentou em um post

for tweet in tweepy.Cursor(api.search, search).items(numeroDeTweets):
    try:
        #cria um comentario, em um post  específico
        #é só colocar o id  do post na 'in_reply_to_status_id' 
        #assim ele irá procurar uma palavra que está na variavel search para ativar a ação do bot
        #e depois irá comentar  na postagem especifica com o id em 'in_reply_to_status_id'
        api.update_status(status=" Olá " + tweet.user.screen_name + " outra mensagem "  , in_reply_to_status_id = 1278805869606637569 , auto_populate_reply_metadata=True) 
        contador += 1
        print("tweet ok " , contador)
        sleep(120) #intervalo de 2 min / 120s
    except tweepy.TweepError as e: #caso houver erro
        print(e.reason)
    except StopIteration: #caso for parar
        break