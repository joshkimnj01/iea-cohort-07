import requests
import datetime
import  json
from requests.auth import HTTPBasicAuth
from datetime import timedelta
import sys
#import argparse

def get_observer_location():
    """Returns the longitude and latitude for the location of this machine.
    Returns:
    str: latitude
    str: longitude"""

    #mylocurl= 'https://api.ipify.org?format=json'
    #myloc= requests.get(mylocurl)

    #url= "https://ip-api.com/json/"+myloc.json()['ip']
    url='http://ip-api.com/json/?fields=61439'

    output= requests.get(url) #,headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)"\
                              #           " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102"\
                              #           Safari/537.36',  'Accept': 'application/json'})

    #if output.status_code== 200:
    #    dict_obj = output.content

    data=output.json()
    outdata= data['lat'], data['lon'],data['query']

    #print(outdata)
        # NOTE: Replace with your real return values!
    return outdata[0], outdata[1]


def get_sun_position(latitude, longitude):
    """Returns the current position of the sun in the sky at the specified location
Parameters:
latitude (str)
longitude (str)
Returns:
float: azimuth
float: altitude

"""

    login= {"applicationId":"ea70a803-e1e3-4cf5-b842-072b95ac54c9", 
            "applicationSecret":"bf0a1c85026c6e0746ed234b24294b31918ad27785784c726247fd0828484b83a7aa"\
                     "a320ebae1a8f2a61b8891309575d3de09acbe391ddce4db54e453ceeb368cf4be7504c201d80b1"\
                     "ef95a2c7be700791ee87130ba39a482529139160871f7297ae39b7f306fcd01033debf78d9dbf2"}
    today = datetime.datetime.now()
    now_date = str(today).split()[0]

    #yesterday = today - timedelta(days = 1)
    #yes_date=(str(yesterday).split())[0]
    yesterday = today - timedelta(hours = 1)
    yes_date=(str(yesterday).split())[0]
    yes_time = str(yesterday).split()[1][0:8]
    body="saturn"

    #url ="https://api.astronomyapi.com/api/v2/bodies"
    url = "https://api.astronomyapi.com/api/v2/bodies/positions/"+body

    querystring = {"latitude":latitude,"longitude":longitude,"from_date":yes_date,"to_date":now_date,"elevation":"50","time":yes_time}

    response = requests.request("GET", url,  params=querystring,  auth=HTTPBasicAuth(login['applicationId'],login['applicationSecret']))

    data_sun= json.loads(response.content)

    sun_loc= data_sun['data']['table']['rows'][0]['cells'][0]['position']['horizonal']

    sun_alt=float(sun_loc['altitude']['degrees'])
    sun_azi=float(sun_loc['azimuth']['degrees'])
    distance = data_sun['data']['table']['rows'][0]['cells'][0]['distance']['fromEarth']['km']
    magnitude = data_sun['data']['table']['rows'][0]['cells'][0]['extraInfo']['magnitude']
    #data_sun
    print (f"Distance from earth to {body} is {distance} Km and Magnitude is {magnitude}")

    return sun_alt, sun_azi, body

def print_position(azimuth, altitude,body):
    """Prints the position of the sun in the sky using the supplied coordinates
    Parameters:
    azimuth (float)
    altitude (float)"""
    #body="Sun"
    print(f"The {body} is currently at: azimuth of ** {azimuth}  and altitude of ** {altitude}")


#if __name__ == "__main__":
#n = len(sys.argv)

if sys.argv[1] !=None :
    body=sys.argv[1]

newloc = (sys.argv[2],sys.argv[3])
print(newloc)

if newloc == "":
    latitude, longitude = get_observer_location()
    azimuth, altitude, body= get_sun_position(latitude, longitude)
else:
    azimuth, altitude, body= get_sun_position(newloc)
print_position(azimuth, altitude,body)
print ("My local machine is  at", latitude, longitude, )