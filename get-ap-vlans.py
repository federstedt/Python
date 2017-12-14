import requests
import pprint
#pprint = pretty print

print('Please input switch IP:')
ip = input()


url = 'http://' +ip +'/rest/v3/lldp/remote-device'


get_lldp = requests.get(url)

get_lldp_json = get_lldp.json()



# Checks for vlans on a given portid.
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


# Checks lldp information and finds a port to wich a AP is plugged in then sends that portid to function for vlan checking.
for x in elements:
    #print("localport: {0} \t NAME: {1}".format(x['local_port'], x['system_name']))
    local = x['local_port']
    sysname = x['system_name']
    #print(local,sysname)
    # Currently checks for AP name, is subpar. Should check for lldp type infromation if possible.
    if 'AP' in sysname:
        print('I port:',local,'sitter en AP:',sysname)
        apport = x['local_port']
        get_vlan(apport)





