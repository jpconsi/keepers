import sys, java

def buildJmsQueueConnectionFactory(abIdent, endpointString):

   print ""
   print "buildJmsQueueConnectionFactory: create Flare Dynamic Service Queue Connection"

   AdminTask.createSIBJMSConnectionFactory('flare-cluster-' + abIdent + '(cells/psm-cell/clusters/flare-cluster-' + abIdent + '|cluster.xml)', '[-name "Flare Dynamic Service Queue Connection" -jndiName com.vacationclub.solar.usage.manager.DynamicServiceQueue -type queue -authDataAlias -category -description -xaRecoveryAuthAlias -busName "Flare Bus" -nonPersistentMapping ExpressNonPersistent -persistentMapping ReliablePersistent -readAhead Default -target -targetType BusMember -targetSignificance Preferred -targetTransportChain -providerEndPoints ' + endpointString + ' -connectionProximity Bus -tempQueueNamePrefix -shareDataSourceWithCMP false]')

   print ""
   print "buildJmsQueueConnectionFactory: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 2):

   print "buildJmsQueueConnectionFactory: this script requires 2 parameters:"
   print "a/b identifier, and enpoint string"
   print ""
   print "e.g.:     buildJmsQueueConnectionFactory a lalfimvq9app60:17279:BootstrapBasicMessaging" 

else:

   buildJmsQueueConnectionFactory(sys.argv[0], sys.argv[1])

#endif