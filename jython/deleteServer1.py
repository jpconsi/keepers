import sys
from time import sleep

def delS1(nodes, abident):

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
   # For each node, delete server1
   # 
   #---------------------------------------------------------
   index = 1
   while ("%s" % (index)) <= nodes:
      nodeName = "psm-node" + ("%s" % (index))

      AdminTask.deleteServer('[-serverName server1 -nodeName ' + nodeName + ']') 

      index = index + 1
 
   #---------------------------------------------------------
   # save changes 
   # 
   #---------------------------------------------------------
   print "deleteServer1: saving config changes."
   AdminConfig.save()

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
      print "deleteServer1: checking for the existence of a NodeSync MBean on node " + nodeName
      nodeSync = AdminControl.completeObjectName("type=NodeSync,node=" + nodeName + ",*")
      if len(nodeSync) == 0:
         print "deleteServer1: Error -- NodeSync MBean not found for name " + nodeName
         return 
      enabled = AdminControl.getAttribute(nodeSync, "serverStartupSyncEnabled")
      if enabled == "false":
         print "deleteServer1: Invoking synchronization for node " + nodeSync + " because serverStartupSyncEnabled is set to false..."
         AdminControl.invoke(nodeSync, "sync")
         sleep(20)
         print "deleteServer1: Done with synchronization."

      index = index + 1  

#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 2):
   print "deleteServer1: this script requires 2 parameters: number of nodes," 
   print "and cluster a/b identifier"
   print ""
   print "e.g.:     deleteServer1  4 b" 
else:
   delS1(sys.argv[0], sys.argv[1])
