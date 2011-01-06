import xml.dom.minidom
import sys
from com.ibm.ws.scripting import ScriptingException
from time import sleep


def get_document (name="E:/lalfimvd0app07.xml"):

   return xml.dom.minidom.parse(name)

#enddef

def find_element(doc, name):

    element = None

    for i in doc.childNodes:

        if i.nodeType == i.ELEMENT_NODE and i.localName == name:

            element = i
            break

        #endif

    #endfor
        
    return element

#enddef


def addCluster(buildType, appsrvName, nodes, abIdent, serversPerNode):

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

      nodeName = buildType + "-node" + ("%s" % (index))
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

      #endwhile

      index = index + 1

   #endwhile
 
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

   #endif

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

      #endif

      enabled = AdminControl.getAttribute(nodeSync, "serverStartupSyncEnabled")
      
      if enabled == "false":
         
         print "addCluster: Invoking synchronization for node " + nodeSync + " because serverStartupSyncEnabled is set to false..."
         AdminControl.invoke(nodeSync, "sync")
         sleep(20)
         print "addCluster: Done with synchronization."

      #endif

      index = index + 1

   #endwhile
      
   #---------------------------------------------------------
   # Ask the Cluster MBean to start the cluster
   # 
   #---------------------------------------------------------
   
   # cluster = AdminControl.completeObjectName("type=Cluster,name=" + clusterName + ",*")
   # print "addCluster: Invoking start for cluster " + clusterName
   # AdminControl.invoke(cluster, "start")

#enddef


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

if (len(sys.argv) != 2):

   print "addClusters: this script requires 2 parameter:"
   print "     hostname and number of nodes"
   print ""
   print "e.g.:     addCluster lalfimvd0app07 4" 

else:

   if sys.argv[0][-2:-1] != "0" and sys.argv[0][-2:-1] != "6":

      print "addClusters: Unknown host type - not web(0) or solar(6)"

   else:

      if sys.argv[0][-2:-1] == "0": 

         type = "ws"

      elif sys.argv[0][-2:-1] == "6":

         type = "psm"

      #endif

      doc=get_document()
      root=find_element(doc, sys.argv[0])


      for i1 in root.childNodes:
 
         if i1.nodeType == i1.ELEMENT_NODE and i1.localName == "cluster":

            for i2 in i1.childNodes:

               if i2.localName == "name":

                  try:
                   
                     name = i2.childNodes[0].nodeValue
                     clusterName = AdminConfig.getid("/Cell:" + type + "-cell/ServerCluster:" + name + "-cluster-a")

                     if clusterName == "":

                        addCluster(type, name, sys.argv[1], "a", "1")
                        print "addClusters: " + name + "cluster-a added"

                     else:

                        print "addClusters: " + name + " cluster-a already exists."

                     #endif

                     clusterName = AdminConfig.getid("/Cell:" + type + "-cell/ServerCluster:" + name + "-cluster-b")

                     if clusterName == "":

                        addCluster(type, name, sys.argv[1], "b", "1")
                        print "addClusters: " + name + "cluster-b added"

                     else:

                        print "addClusters: " + name + " cluster-b already exists."

                     #endif



                     break
                
                  except IndexError:

                     name = ""
                     print "addClusters: XML ERROR. Cluster name is empty. Stopping execution."

                  #endtry
                  
               #endif

            #endfor

         #endif 

      #endfor

      clusterList=AdminConfig.list('ServerCluster', AdminConfig.getid( '/Cell:' + type + '-cell/'))
      arrayClusterList = clusterList.split(lineSeparator)

      for i in arrayClusterList:

         p = i.find("-cluster")
         print i[0:p]

      #endfor

   #endif

#endif













#clusterList=AdminConfig.list('ServerCluster', AdminConfig.getid( '/Cell:psm-cell/')) 
#arrayClusterList = clusterList.split(lineSeparator)

#for i in arrayClusterList:

#   print i
#   p = i.find("-")
#   print i[0:p]
