import tweepy as tweepy
# trocar por nada depois
apiKey = input("Enter your consumer API key: ")
apiSecret = input("Enter your consumer API secret: ")
auth = tweepy.OAuthHandler(apiKey, apiSecret)
redirect_url = auth.get_authorization_url()
print(redirect_url)
verifier = input('Pin:')
auth.get_access_token(verifier)
print(f"Key:{auth.access_token}\nSecret:{auth.access_token_secret}")
userName = input("Insert your @: ")
userKey = auth.access_token
userSecret = auth.access_token_secret
data = open('data.txt', 'w')
data.write(f'=======================CONSUMER=======================\n{apiKey}\n{apiSecret}\n=======================USER=======================\n{userKey}\n{userSecret}\n=======================USER @=====================\n{userName}')