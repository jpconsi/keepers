import sys
from time import sleep

def addCluster(appsrvName, nodes, abIdent, serversPerNode):

   #--------------------------------------------------------------
   # set up globals
   #--------------------------------------------------------------
   global AdminConfig
   global AdminControl
   global AdminApp

   #---------------------------------------------------------
   # We assume that there is only one cell, and we are on it
   #---------------------------------------------------------
   cellName = AdminControl.getCell()
   cell = AdminConfig.getid("/Cell:" + cellName + "/")
 
   #---------------------------------------------------------
   # Construct the attribute list to be used in creating a ServerCluster 
   # attribute.      
   #---------------------------------------------------------
   clusterName = appsrvName + "-cluster-" + abIdent 
   nameAttr = ["name", clusterName]
   descAttr = ["description", clusterName]
   prefAttr = ["preferLocal", "true"]
   stateAttr = ["stateManagement", [["initialState", "STOP"]]]
   attrs = []
   attrs.append(nameAttr)
   attrs.append(descAttr)
   attrs.append(prefAttr)
   attrs.append(stateAttr)
  
   #---------------------------------------------------------
   # Create the server cluster 
   #---------------------------------------------------------


   print "addCluster: creating the ServerCluster " + clusterName
   cluster = AdminConfig.create("ServerCluster", cell, attrs)


   #---------------------------------------------------------
   # For each node, create the required number of servers
   # 
   #---------------------------------------------------------
   index = 1
   while ("%s" % (index)) <= nodes:
      nodeName = "psm-node" + ("%s" % (index))

      node = AdminConfig.getid("/Node:" + nodeName + "/")
      loop = 0
      while ("%s" % (loop)) != serversPerNode:
         uid1 = "-node%s-" % (index)
         uid2 = "%s" % (loop+1)
         servName = appsrvName + uid1 + abIdent + uid2
     	 nameAttr = ["memberName", servName]
         weightAttr = ["weight", "10"]
         attrs = []
         attrs.append(nameAttr)
         attrs.append(weightAttr)
         print "addCluster: creating server " + servName + " on node " + nodeName
         server = AdminConfig.createClusterMember(cluster, node, attrs)
         loop = loop + 1
      index = index + 1
 
   #---------------------------------------------------------
   # save changes 
   # 
   #---------------------------------------------------------
   print "addCluster: saving config changes."
   AdminConfig.save()

   #---------------------------------------------------------
   # Ask the ClusterMgr to refresh its list of clusters 
   # 
   #---------------------------------------------------------
   clusterMgr = AdminControl.completeObjectName("type=ClusterMgr,cell=" + cellName + ",*")
   if len(clusterMgr) == 0:
      print "addCluster: Error -- clusterMgr MBean not found for cell " + cellName
      return 
   AdminControl.invoke(clusterMgr, "retrieveClusters")

   #---------------------------------------------------------
   # For each node, invoke a sync if necessary 
   #     -- Is a nodeSync MBean available on this node? 
   #     -- Find out if serverStartupSyncEnabled is true for this node
   #        We just created this server, so if this attribute is set to
   #        "false" we have to perform a sync.  If we do not, the node we
   #        are installing on may have an out-of-date copy of the config
   #        data. 
   #---------------------------------------------------------
   index = 1
   while ("%s" % (index)) <= nodes:
      node = AdminConfig.getid("/Node:" + nodeName + "/")
      print "addCluster: checking for the existence of a NodeSync MBean on node " + nodeName
      nodeSync = AdminControl.completeObjectName("type=NodeSync,node=" + nodeName + ",*")
      if len(nodeSync) == 0:
         print "addCluster: Error -- NodeSync MBean not found for name " + nodeName
         return 
      enabled = AdminControl.getAttribute(nodeSync, "serverStartupSyncEnabled")
      if enabled == "false":
         print "addCluster: Invoking synchronization for node " + nodeSync + " because serverStartupSyncEnabled is set to false..."
         AdminControl.invoke(nodeSync, "sync")
         sleep(20)
         print "addCluster: Done with synchronization."

      index = index + 1  
   #---------------------------------------------------------
   # Ask the Cluster MBean to start the cluster
   # 
   #---------------------------------------------------------
   # cluster = AdminControl.completeObjectName("type=Cluster,name=" + clusterName + ",*")
   # print "addCluster: Invoking start for cluster " + clusterName
   # AdminControl.invoke(cluster, "start")


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 4):

   print "addCluster: this script requires 4 parameters: appserv name, "
   print "     number of nodes, cluster a/b identifier, number of"
   print "     servers per node"
   print ""
   print "e.g.:     addCluster  solar 4 b 1" 

else:

   addCluster(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])

#endif