from snscrape.modules.twitter import TwitterUserScraper
import json
from datetime import datetime

# Definiert den Benutzernamen des Twitter-Accounts, von dem die Tweets gesucht werden sollen. Dient auch als Speichername
user_name = "HSGStGallen"

# Sucht nach Tweets auf der Twitter-Seite, die dem Benutzernamen entspricht und speichert diese in der 'search'-Liste
search = TwitterUserScraper(user_name).get_items()

# Definiert das Datum, ab dem Tweets gesucht werden sollen (Von: https://stackoverflow.com/questions/73662237/scraping-hourly-tweets-for-a-given-time-period-with-snsscrape)
datetime_str = '2015-01-01 00:00:01'
datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

# Erstellt eine Zählvariable für die Anzahl der gefundenen Tweets
tweet_count = 0

# Erstellt eine Liste
dictionary = []

# Für jeden gefundenen Tweet...
for item in search:
    # Die Zeitzone entfernen, um Werte zu vergleichen (Von: https://stackoverflow.com/questions/10944047/how-can-i-remove-a-pytz-timezone-from-a-datetime-object#:~:text=The%20solution%20is%20to%20convert,that%20you%20cannot%20compare%20datetime.)
    item.date = item.date.replace(tzinfo=None)
    datetime_item = datetime.strptime(str(item.date), '%Y-%m-%d %H:%M:%S')
    # Wenn das Datum des aktuellen Tweets grösser oder gleich dem angegebenen Datum ist, wird der Tweet ausgegeben und zur Liste hinzugefügt. Andernfalls wird der Tweet übersprungen
    if datetime_item >= datetime_object:
        print({
            "Datum": item.date,
            "Tweet Inhalt": item.rawContent,
            "URL": item.url,
        })
        # Diese Elemente der Liste hinzugefügen (Von: https://stackoverflow.com/questions/36108824/how-to-add-elements-to-a-list-in-python)
        dictionary.append({
            "Datum": str(item.date),
            "Tweet Inhalt": item.rawContent,
            "URL": item.url
        })
    else:
        pass

    # Die Anzahl der gefundenen Tweets um 1 erhöhen
    tweet_count += 1

    # Jedes Mal eine Fortschrittsanzeige ausgegeben, wenn die Anzahl der gefundenen Tweets durch 10 teilbar ist
    if tweet_count % 10 == 0:
        print(f'{tweet_count} Tweets gefunden...')

# Speichert die 'dictionary' Liste als JSON-Datei, benannt nach dem eingegebenen Username (Von: https://stackoverflow.com/questions/45791891/reading-and-writing-json-through-python)
with open(f'{user_name}.json', 'w') as outfile:
    json.dump(dictionary, outfile, indent=4)

# Gibt aus, wie viele Tweets insgesamt gefunden wurden und ob erfolgreich eine JSON-Datei erstellt wurde
print(f'{tweet_count} Tweets gefunden und als JSON-Datei gespeichert.')