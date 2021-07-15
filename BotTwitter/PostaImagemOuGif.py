import tweepy

#tokens da api do twitter
auth = tweepy.OAuthHandler(' ',' ')
auth.set_access_token(' ',' ')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# caso for imagem
#upload_result = api.media_upload('/Users/Samsung/Documents/bots/imagem.jpg')

# caso for gif 
#upload_result = api.media_upload('/Users/Samsung/Documents/bots/atee.gif') 

#postar
#api.update_status(status="mensagem", media_ids=[upload_result.media_id_string]) 