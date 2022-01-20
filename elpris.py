import requests
import json
import time
import datetime


api_date_format = '%Y-%m-%dT%H:%M:%SZ'
now = datetime.datetime.now()
later = (datetime.timedelta(hours = 1)) + now

start_time = (now.strftime("%Y")+"-"+now.strftime("%m")+"-"+now.strftime("%d")+"T"+now.strftime("%H")+":00:00Z")
end_time = (later.strftime("%Y")+"-"+later.strftime("%m")+"-"+later.strftime("%d")+"T"+later.strftime("%H")+":00:00Z")

url = "https://data-api.energidataservice.dk/v1/graphql"

payload="{\"query\":\"{\\n  elspotprices (where:{HourDK:{_gte:\\\""+start_time+"\\\",_lt:\\\""+end_time+"\\\"},PriceArea:{_eq:\\\"DK2\\\"}},order_by:{HourDK:asc},limit:1,offset:0)  { HourDK,SpotPriceDKK }\\n}\",\"variables\":{}}"

headers = {
  'content-type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
f = open("value.json", "w")
f.write (response.text)
f.close()