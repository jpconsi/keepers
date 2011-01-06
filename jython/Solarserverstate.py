#-----------------------------------------------------------------

# inc_start_servers.py 

#-----------------------------------------------------------------

# This script will start the SolarCluster cluster and the

# 

from time import sleep

#start subroutine

def start(solarGroup):   

                        # start Solarserver 

                        cellName = AdminControl.getCell()
                        print cellName

                        server = AdminControl.queryNames('type=Server,node=psm-node1,name=solar-node1-a1,*')

                        print server

                        

                        serverState = AdminControl.getAttribute(server, 'state')
                        
                        print serverState

                        while (serverState != "STARTED"):

                          sleep(10)

                          serverState = AdminControl.getAttribute(server, 'state')

                          print ".",

                        print

                        print  " solar-node1-a1 server started"

                                                                 

#main

start(sys.argv[0])

 

