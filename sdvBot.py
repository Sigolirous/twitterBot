import tweepy as tweepy
import random as r
import time as t
data = open('data.txt', 'r')
keys = data.readlines()
auth = tweepy.OAuthHandler(keys[1].strip(), keys[2].strip())
auth.set_access_token(keys[4].strip(), keys[5].strip())
api = tweepy.API(auth)
frases = [
    "Seguindo todo mundo de volta automaticamente.\n É automaticamente mesmo\n O UNF também é automático",
    "✔⏩☛me segue☚⏪✔\n 🔄sigo todos de volta🔃\n 💫➡sem unfollow⬅💫",
    "SDV\nSem UNF\nSdv na hora",
    "Conta nova\nJuntando novos seguidores e amigos\nSDV na hora\nSem UNF"
    "Seguindo todo mundo\nSDV na hora\nSem UNF",
    "Sdv, sem unf (povo chato q da unf nem vem)",
    "Me segue que eu te sigo"
]
def postTweet(listOfPhrases, cont, tagSDV):
    phraseToPost = r.randint(0, 5)
    print("\n\n%s\n%s\n%i" % (listOfPhrases[phraseToPost], tagSDV, cont))
    api.update_status("%s\n%s\n%i" % (listOfPhrases[phraseToPost], tagSDV, cont))
def checkSDV():
        followers = api.followers_ids(keys[7].strip())
        following = api.friends_ids(keys[7].strip())
        for follower in followers:
            euSigolo = follower in following
            if euSigolo == False :
                api.create_friendship(follower)
                print(f'Você vai seguir {follower}')
            else:
                print(f'Você já segue {follower}')            


tagSDV = input("Qual a tag SDV do dia?")
contador = 100
while True:
    postTweet(frases, contador, tagSDV)
    contador = contador +1
    listOfTime = [30, 40, 50, 60]
    timeToSleep = r.randint(0, 3)
    print(f"Próximo post em:{listOfTime[timeToSleep]}")
    t.sleep(listOfTime[timeToSleep])
