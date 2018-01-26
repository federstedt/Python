import requests
import pprint
#pprint = pretty print


switches = ['192.168.119.16'] #, '192.168.119.16']

untag = input('Desired untagged vlan:')   #make input correct format, int!
untag = int(untag)
#untag = 1

tag = input('Desired tagged vlan:')  #make input correct format, int!
tag = int(tag)
#tag = 119


# Function that checks for vlans on a given portid.
def get_vlan(portnr):
    vlanurl = baseurl + '/vlans-ports'
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




for ip in switches:
    baseurl = 'http://' +ip +'/rest/v4'
    # url example http://192.168.119.16/rest/v4/lldp/remote-device

    url = baseurl + '/lldp/remote-device'

    get_lldp = requests.get(url)
    get_lldp_json = get_lldp.json()
    elements = get_lldp_json['lldp_remote_device_element']

    print('\n', ip, 'info for this switch:')
    # Checks lldp information and finds a port to wich a AP is plugged in then sends that portid to function for vlan checking.
    for x in elements:
        # print("localport: {0} \t NAME: {1}".format(x['local_port'], x['system_name']))
         local = x['local_port']
         sysname = x['system_name']
         #This method also works
         #capabilities = x["capabilities_supported"]
         #isAP = capabilities["wlan_access_point"]
         isAP = x["capabilities_supported"]["wlan_access_point"]
         #print(sysname,isAP)
         #print(local,sysname)
        # Currently checks for AP name, is subpar. Should check for lldp type information if possible.
         if isAP == True:
             print('In port:',local,'an AP is connected:',sysname ,'checking against desired vlans...')
             apport = x['local_port']
             #get_vlan(apport)
             miss = get_vlan(apport)
             #print(miss)

    if miss > 0:
        print('vlan mismatch for this Switch')
    else:
        print('Vlans match for this Switch')
