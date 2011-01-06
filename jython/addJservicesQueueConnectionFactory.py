import sys, java

def buildJservicesQueueConnectionFactory(abIdent):

   print ""
   print "buildJservicesQueueConnectionFactory: create Jservices Queue Connection Factory"

   AdminTask.createSIBJMSConnectionFactory('jservices-cluster-' + abIdent + '(cells/psm-cell/clusters/jservices-cluster-' + abIdent + '|cluster.xml)', '[-name "jsbus-qcf" -jndiName jms/jsbus-qcf -type queue -authDataAlias -category -description -xaRecoveryAuthAlias -busName "jsbus" -nonPersistentMapping ExpressNonPersistent -persistentMapping ReliablePersistent -readAhead Default -target -targetType BusMember -targetSignificance Preferred -targetTransportChain -connectionProximity Bus -tempQueueNamePrefix -shareDataSourceWithCMP false]')

   print ""
   print "buildJservicesQueueConnectionFactory: saving the configuration"
   AdminConfig.save()
 
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if (len(sys.argv) != 1):

   print "buildJservicesQueueConnectionFactory: this script requires 1 parameter:"
   print "a/b identifier"
   print ""
   print "e.g.:     buildJmsQueueConnectionFactory a"

else:

   buildJservicesQueueConnectionFactory(sys.argv[0])

#endif