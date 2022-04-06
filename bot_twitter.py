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

def end(message, name):
    return message.strip().endswith(f'@shawnfrostebot {name}')

def text(tweet, keyword):
    if ( (' ' + keyword.lower() + ' ') in (' ' + tweet.lower() + ' ') or (' ' + keyword.lower() + '\n') in (' ' + tweet.lower() + ' ') ) and 'RT' not in tweet:
        return True
    else:
        return False

def read_csv():
    ids = []
    with open(id.csv, 'r', newline='') as f:
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

def choix_message(tweet, keyword):
    if "adore" in tweet:
        messages = [" Moi aussi j'adore " + keyword + "e mais avec un E bg 👍",
                    " Gouts de roi mais " + keyword + "e bg 👍",
                    " Ici on l'adore aussi mais avec un E " + keyword]
        message = random.choice(messages)
    elif "préféré" in tweet:
        messages = [" Moi aussi c'est un de mes persos pref mais c'est " + keyword + "e bg 👍", 
                    " Moi aussi Shawn FROSTE* c'est un de mes persos prefs",
                    " Perso ici on préfère " + keyword + "e"]
        message = random.choice(messages)
    elif "bipolaire" in tweet:
        messages = [" Pour info bg le bipolaire en question s'appelle " + keyword + "e !", 
                    " Certes c'est un taré dans la S2 mais juste pour info c'est " + keyword + "e 👍",
                    " Le bipolaire d'Inazuma Eleven c'est " + keyword + "e avec un E bg 👍"]
        message = random.choice(messages)
    else:
        messages = [" Il est dans quel série ce personnage ?? Inazuma Twelve ?? Car dans Inazuma Eleven c'est " + keyword + "e bg 👍", 
                    " Je ne connais pas ce personnage mais " + keyword + "e oui bg 👍",
                    " " + keyword + "e sans le E est une fraude mais parce contre avec c'est un GOAT",
                    " Je connais aucun " + keyword + " mais par contre " + keyword + "e quel masterclass !!",
                    " Le joueur d'Alpin s'appelle " + keyword + "e et non Frost bg 👍",
                    " On est tous fans de la même oeuvre donc je me permet de te dire que c'est " + keyword + "e",
                    " Un lien pour regarder Inazuma Twelve ?? Car " + keyword + " n'existe pas mais " + keyword + "e oui 👍"]
        message = random.choice(messages)
    return message
    


def reponse(update, id_user):
    api.PostUpdate(update, in_reply_to_status_id=id_user)


def search(date, keys):
    searchResult = api.GetSearch(raw_query='q='+keys.lower()+'&result_type=recent&since='+str(date)[0:10]+'&count=50&lang=fr')
    for search  in searchResult:
        if text(search.text, keys) and deja_repondu(search.id_str) == False and search.user.screen_name != "shawnfrostebot":
            with open("id.csv", "a+", newline="") as f:
                csv_writer = csv.writer(f, delimiter=';')
                csv_writer.writerow([search.id])
                message = choix_message(search.text, keys)
            reponse(f"@{search.user.screen_name} {message}", search.id)
            time.sleep(15)

def mentions():
    searchResults = api.GetMentions()
    for search in searchResults:
        if end(search.text.lower(), "aiden") and deja_repondu(search.id_str) == False:
            autre = search.text.split(None, 1)
            with open("id.csv", "a+", newline="") as f:
                csv_writer = csv.writer(f, delimiter=';')
                csv_writer.writerow([search.id])
                message = choix_message(search.text, 'Aiden Frost')
            reponse(f"{autre[0]} @{search.user.screen_name} {message}", search.id)
            time.sleep(15)
        elif end(search.text.lower(), "shawn") and deja_repondu(search.id_str) == False:
            autre = search.text.split(None, 1)
            with open("id.csv", "a+", newline="") as f:
                csv_writer = csv.writer(f, delimiter=';')
                csv_writer.writerow([search.id])
                message = choix_message(search.text, 'Shawn Frost')
            reponse(f"{autre[0]} @{search.user.screen_name} {message}", search.id)
            time.sleep(15)


search(datetime.datetime.now(datetime.timezone.utc), "Shawn Frost")
search(datetime.datetime.now(datetime.timezone.utc), "Aiden Frost")
mentions()
