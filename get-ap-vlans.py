import requests
import pprint
#pprint = pretty print

print('Please input switch IP:')
ip = input()


url = 'http://' +ip +'/rest/v3/lldp/remote-device'


get_lldp = requests.get(url)

get_lldp_json = get_lldp.json()

#print(type(get_lldp_json))

#pprint.pprint(get_lldp_json)

#Gör om så du tar emot portid nedan och skriver ut vilka vlan som är på porten som skickas
def get_vlan(portnr):
    vlanurl = 'http://' +ip +'/rest/v3/vlans-ports'

    get_vlans = requests.get(vlanurl)
    get_vlans_json = get_vlans.json()
    #pprint.pprint(get_vlans_json)

    vlanelements = get_vlans_json['vlan_port_element']
    for y in vlanelements:
        port = y['port_id']
        vlanid = y['vlan_id']
        portmode = y['port_mode']

        if portnr in port:
            print('Portid:',port,'vlanid:',vlanid,'portmode:',portmode)




elements = get_lldp_json['lldp_remote_device_element']



for x in elements:
    #print("localport: {0} \t NAME: {1}".format(x['local_port'], x['system_name']))
    local = x['local_port']
    sysname = x['system_name']
    #print(local,sysname)
    if 'AP' in sysname:
        print('I port:',local,'sitter en AP:',sysname)
        apport = x['local_port']
        get_vlan(apport)


#Gör om så du skickar porten där en AP sitter till funktionen nedan för att sortera ut vlan på den porten


