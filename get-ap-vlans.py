import requests
import pprint
#pprint = pretty print


ip = input('Please input switch IP:')
#ip = '192.168.119.16'

untag = input('Desired untagged vlan:')   #Gör om input till korrekt format (int)!
untag = int(untag)
#untag = 1

tag = input('Desired tagged vlan:')  #Gör om input till korrekt format (int)!
tag = int(tag)
#tag = 119



url = 'http://' +ip +'/rest/v3/lldp/remote-device'



get_lldp = requests.get(url)

get_lldp_json = get_lldp.json()



# Checks for vlans on a given portid.
def get_vlan(portnr):
    vlanurl = 'http://' +ip +'/rest/v3/vlans-ports'
    # Missmatch checking:
    mismatch = 0
    get_vlans = requests.get(vlanurl)
    get_vlans_json = get_vlans.json()
    #pprint.pprint(get_vlans_json)

    vlanelements = get_vlans_json['vlan_port_element']
    for y in vlanelements:
        port = y['port_id']
        vlanid = y['vlan_id']
        portmode = y['port_mode']

        if portnr in port:
            #print('Portid:',port,'vlanid:',vlanid,'portmode:',portmode)   # Troubleshooting? print this...
            if vlanid != untag and portmode == 'POM_UNTAGGED':
                print('untag mismatch')
                print('Expecting untagged:',untag,'configured:', vlanid)
                mismatch = 1
            if vlanid != tag and portmode == 'POM_TAGGED_STATIC':
                print('tag mismatch')
                print('Expecting tagged:', tag, 'configured:', vlanid)
                mismatch = 1
    return mismatch


elements = get_lldp_json['lldp_remote_device_element']


# Checks lldp information and finds a port to wich a AP is plugged in then sends that portid to function for vlan checking.
for x in elements:
    #print("localport: {0} \t NAME: {1}".format(x['local_port'], x['system_name']))
    local = x['local_port']
    sysname = x['system_name']
    #print(local,sysname)
    # Currently checks for AP name, is subpar. Should check for lldp type information if possible.
    if 'AP' in sysname:
        print('\n In port:',local,'an AP is connected:',sysname ,'checking against desired vlans...')
        apport = x['local_port']
        #get_vlan(apport)
        miss = get_vlan(apport)
        #print(miss)
        if miss > 0:
            print('vlan mismatch for this AP')
        else:
            print('Vlans match for this AP')
