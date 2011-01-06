import sys
from time import sleep

def modifyWebSphereVariables(nodes):

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
   # For each node, modify the WebSphere Oracle Variable
   # 
   #---------------------------------------------------------
   index = 1

   while ("%s" % (index)) <= nodes:

      varName = "ORACLE_JDBC_DRIVER_PATH"
      newVarValue = "D:/oracle/product/10.2.0/client_1/jdbc/lib"
      nodeName = "ws-node"+ ("%s" % (index))
      print ""
      print "modifyWebSphereVariables: Modifying " + varName + " for node " + nodeName
      node = AdminConfig.getid('/Node:' + nodeName +'/')
      
      varSubstitutions = AdminConfig.list("VariableSubstitutionEntry",node).split(java.lang.System.getProperty("line.separator"))

      for varSubst in varSubstitutions:

         getVarName = AdminConfig.showAttribute(varSubst, "symbolicName")

         if getVarName == varName:

            AdminConfig.modify(varSubst,[["value", newVarValue]])
            break

      index = index + 1
 
   #---------------------------------------------------------
   # save changes 
   # 
   #---------------------------------------------------------
   print "modifyWebSphereVariables: saving config changes."
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
      nodeName = "ws-node"+ ("%s" % (index))
      node = AdminConfig.getid("/Node:" + nodeName + "/")
      print "modifyWebSphereVariables: checking for the existence of a NodeSync MBean on node " + nodeName
      nodeSync = AdminControl.completeObjectName("type=NodeSync,node=" + nodeName + ",*")
      if len(nodeSync) == 0:
         print "modifyWebSphereVariables: Error -- NodeSync MBean not found for name " + nodeName
         return 
      enabled = AdminControl.getAttribute(nodeSync, "serverStartupSyncEnabled")
      if enabled == "false":
         print "modifyWebSphereVariables: Invoking synchronization for node " + nodeSync + " because serverStartupSyncEnabled is set to false..."
         AdminControl.invoke(nodeSync, "sync")
         sleep(20)
         print "modifyWebSphereVariables: Done with synchronization."

      index = index + 1  

#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 1):
   print "modifyWebSphereVariables: this script requires 1 parameter:"
   print "     number of nodes"
   print ""
   print "e.g.:     modifyWebSphereVariables 4" 
else:
   modifyWebSphereVariables(sys.argv[0])
