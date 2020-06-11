import requests
import json
import CaseCheck
from datetime import datetime

#get thailand's covid data from url as json file
url = requests.get('https://covid19.th-stat.com/api/open/cases/sum')

#make the url into python dictionary
cvd_Province = url.json()['Province']#dictionary of Province Of Confirmed Case In Thailand
cvd_Nation = url.json()['Nation']#dictionary of Nation Of Confirmed Case In Thailand

print('////////////////////////////////////////////////////////////')#first Seperator
#Show every Confirmed Case In Every Province in Thailand
for province in cvd_Province:
    print(f'{province} : {cvd_Province[province]}')
print('////////////////////////////////////////////////////////////')#Seperator
for nation in cvd_Nation:
    print(f'{nation} : {cvd_Nation[nation]}')

#End