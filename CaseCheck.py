import json
import requests
from datetime import datetime


#get thailand's covid data from url as json file
url = requests.get('https://covid19.th-stat.com/api/open/cases')

#make the url into python dictionary
cvd_case = url.json()

#get the yesterday date
now = datetime.now()
day = int(now.strftime('%d'))
date = now.strftime(f'%Y-%m-{day-1} 00:00:00')

#print out every item

for item in cvd_case['Data']:
    if item['ConfirmDate'] == date:
        print(item)  