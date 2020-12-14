from ncclient import manager
     filter_loopback_Gig1='''
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <GigabitEthernet>
                    <name>1</name>
                </GigabitEthernet>
            </interface>
        </native>
       '''
with manager.connect(host='ios-xe-mgmt-latest.cisco.com',
                     port=10000,
                     username='developer',
                     password='C1sco12345',
                     hostkey_verify=False
                     ) as m:
     rpc_reply = m.get_config(source="running",filter=("subtree",filter_loopback_Gig1))
     print(rpc_reply) print(rpc_reply)
