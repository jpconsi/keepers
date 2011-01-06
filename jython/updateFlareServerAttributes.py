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

   print "updateFlareServerAttributes:updating " + "psm-node" + nodeNum

   serverName = AdminConfig.getid('/Node:psm-node' + nodeNum + '/Server:flare-node' + nodeNum + '-' + abIdent + '1/')
 
   sbs = AdminConfig.list('StartupBeansService', serverName)
   AdminConfig.modify(sbs, [['enable', 'true']])
  
   jvm = AdminConfig.list('JavaVirtualMachine', serverName)
   AdminConfig.modify(jvm, [['initialHeapSize', '512'], ['maximumHeapSize', '1024'], ['genericJvmArguments', '-Duser.timezone=UTC']])
   
   ts = AdminConfig.list('TransactionService', serverName)
   AdminConfig.modify(ts, [['totalTranLifetimeTimeout', '0'], ['propogatedOrBMTTranLifetimeTimeout', '0']])
   
   ejbt = AdminConfig.list('EJBTimer', serverName)
   AdminConfig.modify(ejbt, [['datasourceJNDIName', 'com.vacationclub.solar.usage.datasource_jndi'], ['datasourceAlias', 'flare'], ['tablePrefix', 'SU_EJBTIMER_']])

   print "saving"
   AdminConfig.save()

#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 2):

   print "updateFlareServerAttributes: this script requires 2 parameters:"
   print "a/b identifier and number of nodes"

else:

   index=1

   while ("%s" % (index)) <= sys.argv[1]:

      updateServerAttributes(sys.argv[0], ("%s" % (index)))
      index=index + 1

   #endwhile

#endif
