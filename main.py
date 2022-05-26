import datetime
import time
import requests
from plyer import notification

response = None
try:
    response = requests.get(url="https://corona-rest-api.herokuapp.com/Api/pakistan")
except:
    # if data is fetched due to lack of internet
    print("Please check your internet connection")
if response != None:
    # converting the data in json format
    data = response.json()['Success']

# Repeating the loop for multiple times
while(True):
    notification.notify(
        # title of the notification,
        title="COVID19 Stats on {}".format(datetime.date.today()),
        # the body of the notification
        message="Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{"
                "active}".format(
            totalcases=data['cases'],
            todaycases=data['todayCases'],
            todaydeaths=data['todayDeaths'],
            active=data["active"]),
        # creating icon for the notification
        # we need to download a icon of ico file format
        app_icon="Paomedia-Small-N-Flat-Bell.ico",
        # the notification stays for 50sec
        timeout=50
    )
    # sleep for 4 hrs => 60*60*4 sec
    # notification repeats after every 4hrs
    time.sleep(5)
