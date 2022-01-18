import os
import yaml
import requests
from datetime import date

today = date.today()
path = '/home/cron/scripts/usernameChecker/'
logPath = path + 'logs/'  + today.strftime("%y%m%d") + 'AvailableUsernames' + '.txt'
websitePath = path + 'websites.yml'
#print('Logpath: ' + logPath)
#print('Websitepath: ' + websitePath)

username = 'chowdoe'

def checker():
    with open(websitePath) as f:
        data = yaml.safe_load(f)
        links = data['sites']
    weblinks = ["{}{}".format(i,username) for i in links]
    f = open(logPath, "w")
    for url in weblinks:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
        if r.status_code != 200:
            f.write('Available for: ' + url + '\n')
    f.close()

def main():
    checker()

main()