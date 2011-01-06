import sys
from time import sleep

def updateServerAttributes(abIdent, nodeNum, environment):

   #--------------------------------------------------------------
   # set up globals
   #--------------------------------------------------------------

   global AdminConfig
   global AdminControl
   global AdminApp

   #---------------------------------------------------------
   # We assume that there is only one cell, and we are on it
   #---------------------------------------------------------

   print "updateOwnerServicesServerAttributes:updating ws-node" + nodeNum

   serverName = AdminConfig.getid("/Node:ws-node" + nodeNum + "/Server:owner-services-node" + nodeNum + '-' + abIdent + "1/")

   jvm = AdminConfig.list('JavaVirtualMachine', serverName)

   bdNameAttr = ['name', 'mvci.prop.base.dir']
   bdValueAttr = ['value', 'e:/websphere/mvciconfig']
   envNameAttr = ['name', 'mvci.prop.env']
   envValueAttr = ['value', 'e:/websphere/mvciconfig/' + environment + '.env.properties']

   attrs = []
   attrs.append(bdNameAttr)
   attrs.append(bdValueAttr)
   attrs.append(envNameAttr)
   attrs.append(envValueAttr)

   property = ['systemProperties', [attrs]]
   AdminConfig.modify(jvm, [property])

   print "saving"
   AdminConfig.save()


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 3):

   print "updateOwnerServicesServerAttributes: this script requires 3 parameters:"
   print "a/b identifier, node number and environment"
   print ""
   print "ex: updateOwnerServicesServerAttributes a 1 q2app01"


else:

   updateServerAttributes(sys.argv[0], sys.argv[1], sys.argv[2])

#endif
