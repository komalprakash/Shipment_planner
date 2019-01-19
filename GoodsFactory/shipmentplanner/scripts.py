import urllib.request
from .models import Shipments
import json
import requests

def getDist2():
        my_api = 'AIzaSyBcKLUkDkZTNUWbKIutopkOUFnbu-wk2C0'
        destinations=list(ship.destination for ship in Shipments.objects.all())
        places=''
        for s in range(len(destinations)-1):
            places +=destinations[s]+'|'
        places +=destinations[len(destinations)-1]

        url='https://maps.googleapis.com/maps/api/distancematrix/json?'+'origins='+places+'&destinations='+places+'&key='+my_api
        #print(url)
        try: json_obj = urllib.request.Request(url)
        except urllib.error.URLError as e:
            print(e.reason)
        #print("Hello")
        #print(json_obj)
        r = urllib.request.urlopen(json_obj).read()
        r = r.decode('utf-8')
        #print(r)
        data= json.loads(r)


        my_table=[]
        list1=data['rows']
        for i in list1:
            j=i['elements']

            my_row=[]
            for k in j:
                my_row.append(k['distance']['value'])
            my_table.append(my_row)
        #print(my_table)
        return my_table

def getDist():
    url = "http://www.mapquestapi.com/directions/v2/routematrix?key=3rLQ8aMFoRv1OWMnquXJwuAlIaSHPLRc"
    destinations=list(ship.destination for ship in Shipments.objects.all())
    params = {
      "locations": destinations,
      "options": {
        "allToAll": True
      }
    }
    response = requests.post(url,data=json.dumps(params))

    j=response.json()
    list1=j['distance']
    return list1

def getOrigin(origin):
    my_api = 'AIzaSyBcKLUkDkZTNUWbKIutopkOUFnbu-wk2C0'
    url='https://maps.googleapis.com/maps/api/geocode/json?address='+origin+'&key='+my_api
    try:
        json_obj = urllib.request.Request(url)
        #print(json_obj)
        r = urllib.request.urlopen(json_obj).read()
        r = r.decode('utf-8')
        #print(r)
        data= json.loads(r)
        ans= data["results"][0]["geometry"]["location"]
        return ans
    except Exception as e:
        #print(e.reason)
        return({'lat':51.5074,'lng':0.1278})
