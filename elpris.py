import requests
import json
import datetime

# Define Function
def GetPrice():
  now = datetime.datetime.now()
  later = (datetime.timedelta(hours = 1)) + now
  start_time = (now.strftime("%Y")+"-"+now.strftime("%m")+"-"+now.strftime("%d")+"T"+now.strftime("%H")+":00:00Z")
  end_time = (later.strftime("%Y")+"-"+later.strftime("%m")+"-"+later.strftime("%d")+"T"+later.strftime("%H")+":00:00Z")
  url = "https://data-api.energidataservice.dk/v1/graphql"
  
  headers = {
    'content-type': 'application/json'
  }

  payload="{\"query\":\"{\\n  elspotprices (where:{HourDK:{_gte:\\\""+start_time+"\\\",_lt:\\\""+end_time+"\\\"},PriceArea:{_eq:\\\"DK2\\\"}},order_by:{HourDK:asc},limit:1,offset:0)  { HourDK,SpotPriceDKK }\\n}\",\"variables\":{}}"

  response = requests.request("POST", url, headers=headers, data=payload)

  jsonObject = json.loads(response.text)
  SpotPriceDKK = int(jsonObject['data']['elspotprices'][0]['SpotPriceDKK'])/1000*3

  return SpotPriceDKK


# Run Function Example
print (GetPrice())