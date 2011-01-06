import sys
from time import sleep
   

        Server= AdminControl.completeObjectName('cell=psm-cell,node=psm-node1,name=solar-node1-a1,type=Server,*')
   cluster = AdminControl.queryNames('type=Cluster,cell=' + cellName + ',name=solar-cluster-' + solarGroup + ',*')

   print server
   serverstate = AdminControl.getAttribute(server, 'state')
   print serverstate
    while (serverstate != "STARTED"):
       sleep(10)
    
    
   print "solar-node1-a1 is started"

