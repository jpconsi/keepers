import sys, java

def buildJmsTopicConnectionFactory(abIdent, endpointString):

   print ""
   print "buildJmsTopicConnectionFactory: create Flare JMS Topic Connection Factory"

   AdminTask.createSIBJMSConnectionFactory('flare-cluster-' + abIdent + '(cells/psm-cell/clusters/flare-cluster-' + abIdent + '|cluster.xml)', '[-name "Flare JMS Topic Connection Factory" -jndiName com.vacationclub.solar.usage.ed.EdJmsConnectionFactory -type topic -authDataAlias -category -description -xaRecoveryAuthAlias -busName "Flare Bus" -clientID -nonPersistentMapping ExpressNonPersistent -persistentMapping ReliablePersistent -durableSubscriptionHome "flare-cluster.000-Flare Bus" -readAhead Default -target -targetType BusMember -targetSignificance Preferred -targetTransportChain -providerEndPoints ' + endpointString + ' -connectionProximity Bus -tempTopicNamePrefix -shareDataSourceWithCMP false]')

   print ""
   print "buildJmsTopicConnectionFactory: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 2):

   print "buildJmsTopicConnectionFactory: this script requires 2 parameters:"
   print "a/b identifier, and endpoint string"
   print ""
   print "e.g.:     buildJmsTopicConnectionFactory a 'lalfimvd0app03:7280:BootstrapBasicMessaging'" 

else:

   buildJmsTopicConnectionFactory(sys.argv[0], sys.argv[1])

#endif