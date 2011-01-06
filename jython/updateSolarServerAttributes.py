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

   print "updateSolarServerAttributes:updating psm-node" + nodeNum

   serverName = AdminConfig.getid("/Node:psm-node" + nodeNum + "/Server:solar-node" + nodeNum + '-' + abIdent + "1/")

   osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")

   AdminConfig.modify(osr, [['rolloverType', 'TIME']])

   esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")

   AdminConfig.modify(esr, [['rolloverType', 'TIME']])

   jvm = AdminConfig.list('JavaVirtualMachine', serverName)

   nameAttr = ['name', 'com.ibm.websphere.ejbcontainer.allowEarlyInsert']
   valueAttr = ['value', 'true']

   attrs = []
   attrs.append(nameAttr)
   attrs.append(valueAttr)

   property = ['systemProperties', [attrs]]
   AdminConfig.modify(jvm, [property])

   ts = AdminConfig.list('TransactionService', serverName)
   AdminConfig.modify(ts, [['totalTranLifetimeTimeout', '0'], ['clientInactivityTimeout', '600'], ['propogatedOrBMTTranLifetimeTimeout', '1200']])

   print "saving"
   AdminConfig.save()

   print "updateSolarServerAttributes:updating psm-node" + nodeNum

   serverName = AdminConfig.getid("/Node:psm-node" + nodeNum + "/Server:solarsupport-node" + nodeNum + '-' + abIdent + "1/")

   osr = AdminConfig.showAttribute(serverName, "outputStreamRedirect")

   AdminConfig.modify(osr, [['rolloverType', 'TIME']])

   esr = AdminConfig.showAttribute(serverName, "errorStreamRedirect")

   AdminConfig.modify(esr, [['rolloverType', 'TIME']])
 
   jvm = AdminConfig.list('JavaVirtualMachine', serverName)

   nameAttr = ['name', 'com.ibm.websphere.ejbcontainer.allowEarlyInsert']
   valueAttr = ['value', 'true']

   attrs = []
   attrs.append(nameAttr)
   attrs.append(valueAttr)

   property = ['systemProperties', [attrs]]
   AdminConfig.modify(jvm, [property])

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
