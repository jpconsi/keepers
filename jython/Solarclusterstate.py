#-----------------------------------------------------------------

# inc_start_servers.py 

#-----------------------------------------------------------------

# This script will start the SolarCluster cluster and the

# 

from time import sleep

#start subroutine

def start(solarGroup):   

                        # start SolarCluster cluster

                        cellName = AdminControl.getCell()
                        print cellName

                        cluster = AdminControl.queryNames('type=Cluster,cell=' + cellName + ',name=solar-cluster-' + solarGroup + ',*')

                        print cluster 

                        cName = AdminControl.getAttribute(cluster, 'clusterName')

                        print cName + " Cluster starting ",

                        clusterState = AdminControl.getAttribute(cluster, 'state')
                        
                        print clusterState

                        while (clusterState != "websphere.cluster.running"):

                          sleep(10)

                          clusterState = AdminControl.getAttribute(cluster, 'state')

                          print ".",

                        print

                        print cName + " Solar Cluster started"

                                                                 

#main

start(sys.argv[0])

 

