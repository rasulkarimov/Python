from ncclient import manager
     config_data='''
       <config>
         <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
           <interface>
             <GigabitEthernet>
               <name>1</name>
               <ip>
                 <address>
                   <primary>
                     <address>10.0.0.1</address>
                     <mask>255.255.255.0</mask>
                   </primary>
                 </address>
               </ip>
             </GigabitEthernet >
           </interface>
         </native>
       </config>
       '''
with manager.connect(host='ios-xe-mgmt-latest.cisco.com',
                     port=10000,
                     username='developer',
                     password='C1sco12345',
                     hostkey_verify=False
                     ) as m:
     rpc_reply = m.edit_config(target="running",config=config_data)
     print(rpc_reply)
