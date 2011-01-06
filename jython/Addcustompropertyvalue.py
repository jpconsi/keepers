import sys
from time import sleep
def updateServerAttributes(abIdent, nodeNum):
#--------------------------------------------------------------
# set up globals
#--------------------------------------------------------------
   global AdminConfig
   global AdminControl
   global AdminApp
#---------------------------------------------------------
# We assume that there is only one cell, and we are on it
#---------------------------------------------------------
   print "updateServerAttributes:updating owner-services server attributes on node " + nodeNum 
   serverName = AdminConfig.getid("/Node:psm-node" + nodeNum + "/Server:jservices-node" + nodeNum + '-' + abIdent + "1/")
   print serverName
   wc = AdminConfig.list('WebContainer', serverName)
   nameAttr = ['name', 'com.ibm.ws.webcontainer.ChannelWriteType']
   valueAttr = ['value', 'sync']
   attrs = []
   attrs.append(nameAttr)
   attrs.append(valueAttr)
   property = ['properties', [attrs]]
   AdminConfig.modify(wc, [property])
   print "saving"
   AdminConfig.save()
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 2):
   print "updateSolarServerAttributes: this script requires 2 parameters:"
   print "a/b identifier and number of nodes"
else:
   index=1
   while ("%s" % (index)) <= sys.argv[1]:
    updateServerAttributes(sys.argv[0], ("%s" % (index)))
    index=index + 1
#endwhile
#endif
 