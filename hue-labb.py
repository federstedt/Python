import requests
import pprint
import time

user = 'u4Hzj4ddNYAINf4e0RG6-du8kV8uYmgfNiKkdxdR'
baseurl = 'http://192.168.119.200/api/' + user
lightsurl = baseurl + '/lights'

def getLights():

    get_lights = requests.get(lightsurl)
    get_lights_json = get_lights.json()

    #Se alla lampor i en lista
    #pprint.pprint(get_lights_json)
    return get_lights_json

def getLight(lightnr = ''):
    # Hämta lampanr1 ur listan ovan
    lighturl = lightsurl +'/' + lightnr
    get_light = requests.get(lighturl)
    light = get_light.json()
    #pprint.pprint(light1)
    return light

'''
# Nedan gör samma sak 2 gång på olika sätt:
state = light1['state']['on']
print(state)

test = jsonlights['1']['state']['on']
print(test)
'''

def switchlight():
    puturl = lightsurl + '/1/state'

    light1 = getLight('1')
    test = light1['state']['on']

    if test == False:
        #payload = '{\"on\":true}'  nedan höjer även brightness
        payload = '{\"on\":true,\"bri\":254}'
        print('Trying to turn ON light...')
    elif test == True:
        #payload = '{\"on\":false}'   Nedan sätter även ned brightness
        payload = '{\"on\":false,\"bri\":67}'
        print('Trying to turn OFF light...')

    #print(puturl)
    #print(payload)


    config_light = requests.request("PUT", puturl, data=payload)
    #print(config_light)


    time.sleep(0.5)

    light1 = getLight('1')
    test = light1['state']['on']
    #print(test)
    #print(type(test))
    if test == True:
        print('Light is now ON')
    elif test == False:
        print('Light is now OFF')


jsonlights = getLights()
#pprint.pprint(jsonlights)

light1 = getLight('1')
#pprint.pprint(light1)

switchlight()
