import twitter
import datetime
import time
import csv

api_key = <consumer_key>
api_key_secret = <consumer_key_secret>
access_token = <access_token>
access_token_secret = <access_token_secret>

api = twitter.Api(api_key,
                  api_key_secret,
                  access_token,
                  access_token_secret)


def text(tweet, keyword):
    if keyword in tweet.lower() and 'RT' not in tweet:
        return True
    else:
        return False

def read_csv():
    ids = []
    with open("id.csv", 'r', newline='') as f:
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

def reponse(update, id_user):
    api.PostUpdate(update, in_reply_to_status_id=id_user)

def search(date, keys):
    searchResult = api.GetSearch(raw_query='q='+keys+'&result_type=recent&since='+date+'&count=10')
    for search  in searchResult:
        if text(search.text, keys) and deja_repondu(search.id_str)==False:
            with open("id.csv", "a+", newline="") as f:
                csv_writer = csv.writer(f, delimiter=';')
                csv_writer.writerow([search.id])
            print(search.user.screen_name)
            reponse('@'+ search.user.screen_name +" Shawn Froste s'écrit avec un E bg !!", search.id)


search(datetime.date.today(, "shawn frost")
