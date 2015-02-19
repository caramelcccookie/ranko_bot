from twython import Twython
#https://github.com/ryanmcgrath/twython
import webbrowser
import time
from lang3 import sentence
APP_KEY = 
APP_SECRET = 
OAUTH_TOKEN =
OAUTH_TOKEN_SECRET = 

#twitter = Twython(APP_KEY, APP_SECRET)
#auth = twitter.get_authentication_tokens(callback_url='naver.com')
#url = auth['auth_url']
#webbrowser.open(url)
#OAUTH_TOKEN = auth['oauth_token']
#OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
#print (auth['auth_url'])

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

sen = '..'

twitter.update_status(status='란코 봇 가동 시작')

while True:
    tmp=sentence()
    if sen==tmp:
        tmp += ' .'
        twitter.update_status(status=tmp)
    else:
        sen = tmp
        twitter.update_status(status=sen)
    time.sleep(3600)
twitter.update_status(status='란코 봇 가동 종료')

