import twitter
import datetime
import csv
import random
import time

api_key = <consumer_key>
api_key_secret = <consumer_key_secret>
access_token = <access_token>
access_token_secret = <access_token_secret>

api = twitter.Api(api_key,
                  api_key_secret,
                  access_token,
                  access_token_secret)


def end_text(tweet):
    return tweet.lower().endswith("@shawnfrostebot")

def text(tweet, keyword):
    indice = tweet.lower().find(keyword)
    if indice==-1:
        return False
    elif indice+11<=len(tweet)-11:
        if tweet.lower()[indice+11]=='e':
            return False
        else:
            if 'RT' not in tweet:
                return True
    else:
        if 'RT' not in tweet:
            return True

def read_csv():
    ids = []
    with open("C:/Users/noabu/Documents/Twitter/code/id.csv", 'r', newline='') as f:
        for line in f:
            id_ligne = line.strip()
            ids.append(id_ligne)
    return ids

def deja_repondu(tweet_id):
    ids = read_csv()
    for id in ids:
        if tweet_id == id:
            return True
    return False

def deuxieme_personne(tweet):
    autre = ""
    fini = False
    n=0
    while fini == False:
        if tweet[n] == " ":
            fini = True
        else:
            autre += tweet[n]
        n+=1
    return autre

def reponse(update, id_user):
    api.PostUpdate(update, in_reply_to_status_id=id_user)

def search(date, keys, messages):
    searchResult = api.GetSearch(raw_query='q='+keys+'&result_type=recent&since='+str(date)[0:10]+'&count=50')
    for search  in searchResult:
        if text(search.text, keys) and deja_repondu(search.id_str)==False:
            with open("id.csv", "a+", newline="") as f:
                csv_writer = csv.writer(f, delimiter=';')
                csv_writer.writerow([search.id])
                message = random.choice(messages)
            reponse('@'+ search.user.screen_name + message, search.id)
            time.sleep(15)

def mentions(messages):
    searchResults = api.GetMentions()
    for search in searchResults:
        if end_text(search.text) and deja_repondu(search.id_str)==False:
            autre = deuxieme_personne(search.text)
            with open("id.csv", "a+", newline="") as f:
                csv_writer = csv.writer(f, delimiter=';')
                csv_writer.writerow([search.id])
                message = random.choice(messages)
            reponse('@'+ search.user.screen_name + ' ' + autre + message, search.id)
            time.sleep(15)

messages = [
    " Shawn Froste s'écrit avec un E bg !! Shawn Froste is spelled with an E !!",
    " Shawn Froste avec un E s'il te plait !! Shawn Froste with an E please !!",
    " SHAWN FROSTE !!!",
    " Shawn Froste sans E n'existe pas !! Shawn Froste without an E doesn't exist !!",
    " Ecrit le correctement bg : Shawn Froste !! Write it correctly plz : Shawn Froste",
    " Ça ne s'écrit pas Frost mais Froste ... It's not spelled Frost but Froste",
    " S'il te plait écrit le Froste mais pas Frost !! Please write it Froste but not Frost !!"
]

mentions(messages)
search(datetime.datetime.now(datetime.timezone.utc), "shawn frost", messages)
