import urllib, json
import requests
from time import sleep

url = "" #json url e.g https://mapi.mobilelegends.com/api/icon

response = urllib.urlopen(url)
data = json.loads(response.read())

n=0
for objectName in data: #objectName is json objects name
    link = data[objectName] #loops through json objects data
    if "https://" in link: #if json object includes https
        try:
            #gets the file from url e.g img
            myfile = requests.get(link)
            #saves the file
            open('','wb').write(myfile.content) #first parameter includes path to folder or simple just the file name + extension
            n+=1
            print(n) #count of downloaded files
        except:
            print("connection refused by server")
            print("retrying...")
            sleep(5)
            continue